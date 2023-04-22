Offloading Computation to DSPs
------------------------------

This guide describes a sequence of steps to offload heavy computation from your ARM Cortex to the C66x DSPs featured on the phyCORE-AM57x.

A DSP or Digital Signal Processor is a specialized CPU intended to perform math operations efficiently. A conventional microprocessor can perform heavy algorithms successfully but it isn't well suited for it since it often won't be able to meet low latency requirements in real time applications and microprocessors aren't as power efficient. 

Dispatching computations from the host microprocessor to a compute device like a DSP requires some amount of overhead so dispatching individual, small computations will not result in a speed improvement. You really see DSPs shine when they are responsible for performing large computations on a stream of data. Even so, it can still be beneficial to free up the CPU to perform other tasks by offloading work the DSP can handle. 

In order to program our DSPs we will leverage the OpenCL API framework which is included by default in the fully featured arago-core-tisdk-image which is the default that is included with the phyCORE-AM57x Development Kit (See the BSP Development for more information). When your application involves a large computations you could face something like long loading times or buffering and OpenCL gives you an API to write software that distributes the work load to more CPUs to save you time. These "slave" CPUs are referred to as compute devices.

.. note::
    You can basically rewrite your "matrix_multiply( )" function, perhaps in some hypothetical C/C++ program, such that it conforms to the OpenCL API which is implemented to support a number of different compute devices. The new OpenCL compliant version of the "matrix_multiply( )" function is called an OpenCL kernel and is compiled and deployed to the compute device at runtime. Optimizations such as deploying a pre-compiled OpenCL Kernel can be implemented but this lies outside the scope of this guide.

In this guide we will only explore DSPs but compute devices could include GPUs or other CPUs. Since every compute device is structured differently (different number of compute units or cores for example) it is important to note that OpenCL kernels are not performance portable and should be written specifically for the compute device being used and the application it is intended for.

.. note::
    This guide was intended to be a quickstart for offloading computation to DSPs. For further resources pertaining to compilation, optimization, and memory usage please visit The TI OpenCL User's Guide, which this guide was adapted from: http://downloads.ti.com/mctools/esd/docs/opencl/offload.html#matmul-ocl-kernel-obj

Step-by-step Guide
------------------

Lets first take a look at an example where we multiply two 100x100 Matrices:

.. code-block:: none
    :caption: "matmul_arm.cpp"

    #include <cassert>
    #include <cstdlib>
    #include <iostream>

    using namespace std;

    const int DIM       = 100;
    const int mat_N     = DIM;
    const int mat_K     = DIM;
    const int mat_M     = DIM;

    void mat_mpy(const float *A, const float *B, float *C, int mat_N, int mat_K, int mat_M)
    {
        for (int col = 0; col < mat_M; ++col)
            for (int row = 0; row < mat_N; ++row)
            {
                C[row*mat_M+col] = 0;
                for (int i = 0; i < mat_K; ++i)
                    C[row*mat_M+col] += A[row*mat_K+i] * B[i*mat_M+col];
            }
    }

    int main(int argc, char *argv[])
    {
        size_t mat_size = DIM * DIM * sizeof(float);

        // Allocate matrices
        float *A      = (float *) malloc(mat_size);
        float *B      = (float *) malloc(mat_size);
        float *C      = (float *) malloc(mat_size);
        // Ensure memory was successfully allocated 
        assert(A != nullptr && B != nullptr && C != nullptr && C != nullptr);

        // Initialize matrices
        srand(time(0));
        for (int i=0; i < mat_N * mat_K; ++i) A[i] = rand() % 5 + 1;
        for (int i=0; i < mat_K * mat_M; ++i) B[i] = rand() % 5 + 1;
        for (int i=0; i < mat_N * mat_M; ++i) C[i] = 0.0;

        // Multiply matrices C = A x B
        mat_mpy(A, B, C, mat_N, mat_K, mat_M);

        free(A);
        free(B);
        free(C);

        return 0;
    }

Go ahead and copy/paste this into a file on your phyCORE-AM57x if you'd like.

The above represents a naive approach to implementing a Matrix Multiplication function. The code will compile and execute but the issue is that it will be executed by the ARM cortex that is also running Linux! The ARM cortex is already spread thin since Linux manages various system services and tasks behind the scenes so adding another task to its to-do list is not ideal.

Optional: Try the following to compile and run the code. It doesn't have any print statements so its not very exciting, this is provided as reference if you would like to compare runtimes.

.. code-block:: none
    :caption: "Target (Linux)"

    g++ -std=c++11 matmul_arm.cpp -o matmul_arm
    ./matmul_arm

Let's look at that matrix multiplication function again but this time we will re-write it as an OpenCL kernel.  

.. code-block:: none
    :caption: OpenCL kernel

    const std::string kernelSrc = R"(
        kernel void ocl_matmpy(const global float *a, const global float *b, global float *c, int mat_K, int mat_N)
        {
            int col    = get_global_id(0);
            int mat_M  = get_global_size(0);

            for (int row = 0; row < mat_N; ++row)
            {
                c[row * mat_M + col] = 0;
                for (int i = 0; i < mat_K; ++i)
                    c[row * mat_M + col] += a[row*mat_K+i] * b[i*mat_M+col];
            }
        }
    )";

The OpenCL-C Kernel is written in “OpenCL-C”. It's good old C that we know and love but its been adapted to suit the device model that OpenCL expects which includes things like contiguous memory buffers that reside in a well-defined hierarchy and the use of “kernel” to signify the execution entry point instead of "main".  OpenCL-C also promotes parallelism in the form of vector types that leverage multi-core architectures and introduces new concepts like work groups/items to synchronize the work done by multiple compute devices.

We can define our OpenCL-C Kernel in this string (which is the source of the OpenCL-C Kernel) right in the main .cpp file of our project. 

.. note::
    This is the perfect opportunity to reiterate that OpenCL-C Kernel are not performance portable! This means that if you write your OpenCL kernel for one type of DSP is won't perform the same when you run the same kernel on a different DSP. The above OpenCL-C Kernel will work as expected but it's memory usage isn't optimized for speed and it doesn't leverage more than 1x DSP (the AM57x has two). Visit the following link for more information on getting the best performance possible: http://downloads.ti.com/mctools/esd/docs/opencl/index.html

Now that we have the source of our OpenCL-C Kernel defined, how do we compile and execute it? GREAT QUESTION! We will use the OpenCL API to create a runtime environment for our OpenCL-C Kernel directly within our main .cpp file. Here is what we will need to do...

* **Define a Context** - What compute device are we hoping to use? DSP, GPU, CPU!?

  .. note::
    TI's OpenCL implementation doesn't support CPU or GPU devices yet.

* **Define a Queue** - This will organize the commands and data we want to feed to this compute device.
* **Build the OpenCL-C Kernel** - This step has to take into account the compute device you specified in order to use the correct instruction set for it. 
* **Load our Queue with the Kernel and data**
* **Submit the Queue to the device and Wait until its done!**

Lets see what our new program looks like with the above implemented: 

.. code-block:: none
    :caption: "matmul_arm.cpp"

    #include <iostream>
    #include <cstdlib>
    #include <assert.h>
    #include <utility>
    #include "ocl_util.h"

    #define __CL_ENABLE_EXCEPTIONS
    #include <CL/cl.hpp>
    /******************************************************************************
    * C[N][M] = A[N][K] * B[K][M];
    ******************************************************************************/
    using namespace cl;

    using std::cout;
    using std::cerr;
    using std::endl;

    const int DIM       = 100;
    const int mat_N     = DIM;     
    const int mat_K     = DIM;     
    const int mat_M     = DIM;     

    const std::string kernelSrc = R"(
    	kernel void ocl_matmpy(const global float *a, const global float *b, global float *c, int mat_K,int mat_N)
    	{
        	int col    = get_global_id(0);
        	int mat_M  = get_global_size(0);

        	for (int row = 0; row < mat_N; ++row)
        	{
            	c[row * mat_M + col] = 0;
            	for (int i = 0; i < mat_K; ++i)
                	c[row * mat_M + col] += a[row*mat_K+i] * b[i*mat_M+col];
        	}
    	}
    )";

    void mat_mpy_ocl(float *A, float *B, float *C, int mat_N, int mat_K, int mat_M, std::size_t mat_size)
    {
       try 
       {
         // Initialize context and command queue
         Context context(CL_DEVICE_TYPE_ACCELERATOR); 
         std::vector<Device> devices = context.getInfo<CL_CONTEXT_DEVICES>();
         CommandQueue Q (context, devices[0]);

         // Build the OpenCL program
         Program::Sources source(1, std::make_pair(kernelSrc.c_str(), kernelSrc.length()));
         Program P = Program(context, source);
         P.build(devices); 

         // Create buffers from memory allocated via __malloc_ddr
         Buffer bufA(context, CL_MEM_READ_ONLY|CL_MEM_USE_HOST_PTR,   mat_size, A);
         Buffer bufB(context, CL_MEM_READ_ONLY|CL_MEM_USE_HOST_PTR,   mat_size, B);
         Buffer bufC(context, CL_MEM_WRITE_ONLY|CL_MEM_USE_HOST_PTR,  mat_size, C);

         // Create kernel and set up arguments
         Kernel K(P, "ocl_matmpy");
         K.setArg(0, bufA);
         K.setArg(1, bufB);
         K.setArg(2, bufC);
         K.setArg(3, mat_K);
         K.setArg(4, mat_N);

         // Run the kernel and wait for completion
         Event E;
         Q.enqueueNDRangeKernel(K, NullRange, NDRange(mat_M), NDRange(1), NULL, &E);
         E.wait();
       }
       catch (Error err) 
       {
         cerr << "ERROR: " << err.what() << "(" << err.err() << ", " << ocl_decode_error(err.err()) << ")" << endl;
         exit(-1);
       }
    }

    int main(int argc, char *argv[])
    {
       std::size_t mat_size = DIM * DIM * sizeof(float);

       // Allocate matrices
       float *A      = (float *) __malloc_ddr(mat_size);
       float *B      = (float *) __malloc_ddr(mat_size);
       float *C      = (float *) __malloc_ddr(mat_size);

       assert(A != nullptr && B != nullptr && C != nullptr && C != nullptr);

       // Initialize matrices
       srand(42);
       for (int i=0; i < mat_N * mat_K; ++i) A[i] = rand() % 5 + 1;
       for (int i=0; i < mat_K * mat_M; ++i) B[i] = rand() % 5 + 1;
       for (int i=0; i < mat_N * mat_M; ++i) C[i] = 0.0;

       // Multiple matrices C = A x B
       mat_mpy_ocl(A, B, C, mat_N, mat_K, mat_M, mat_size);

       // Free the matrices
       __free_ddr(A);
       __free_ddr(B);
       __free_ddr(C);

       return 0;
    }

Go ahead and copy/paste this into a file on your phyCORE-AM57x if you'd like.

Notice that our main function didn't change much! We did however have to use a special memory allocator "__malloc_ddr" since the Cortex-A15s of the AM57x use contiguous memory buffers stored on DDR3 to communicate with the DSPs.

Optional: Again, try the following to compile and run the code. It doesn't have any print statements so its not very exciting, this is provided as reference if you would like to compare runtimes.

.. code-block:: none
    :caption: "Target (Linux)"

    g++ -O3 -std=c++11 matmul_dsp.cpp -lOpenCL -locl_util -o matmul_dsp
    ./matmul_dsp

What's Next?
------------

Navigate to /usr/share/ti/examples/opencl in Linux on your phyCORE-AM57x Development Kit to explore more OpenCL examples. You can do this with the following commands:

.. code-block:: none
    :caption: "Target (Linux)"

    cd /usr/share/ti/examples/opencl
    ls

For instance, if you are interested in the demo "<demo>", use the following commands to build and execute it: 

.. code-block:: none
    :caption: "Target (Linux)"

    cd <demo>
    make
    ./<demo>

The description for these examples can be found here:
http://downloads.ti.com/mctools/esd/docs/opencl/examples/index.html