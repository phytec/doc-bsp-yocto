.. _hello-57:

Hello World
-----------

This guide will walkthrough the creation and cross-compilation of a Hello World executable intended to run on the phyCORE-AM57x Development kit.

.. note::
    In order to follow this guide, you must first :ref:`InstallSDK-57` and source the cross compilation environment.

First, create your project folder: 

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    mkdir ~/helloworld
    cd ~/helloworld

Use the Vi Text Editor to write our project code

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    vi hello.c

Fill in the contents of hello.c with the following: 

.. code-block:: none
    :caption: "hello.c"

    #include <stdio.h>
 
    int main()
    {
        printf("Hello World!\n");
    }

Now cross-compile the project into a dynamically linked executable:

.. code-block:: none
    :caption: "Host (Ubuntu)"

    $CC -O hello.c -o hello

And now you should have generated an executable! And its name is "hello"!

Remember that this executable was compiled to run on your phyCORE-AM57x, so you won't be able to run it on your Ubuntu Host machine. Go ahead and try (it will error)! We can verify the architecture it is compiled for using the following command:

.. code-block:: none
    :caption: "Host (Ubuntu)"

    file hello

We can see that this executable is meant to be run on the Cortex-A15 of the phyCORE-AM57x:

.. code-block:: none
    :caption: "Example Output"

    hello: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, for GNU/Linux 3.2.0, not stripped

Transfer the executable to the phyCORE-AM57x while it is booted into Linux. I recommend just copying the "hello" file to the development kit's bootable SD Card. Be sure to ``poweroff`` the development kit before removing the SD Card and to safely eject the card from your host after you drag and drop the file.

Once the file has been transferred to the phyCORE-AM57x, run the file with the following command: 

.. code-block:: none
    :caption: "Host (Ubuntu)"

    cd /<path>/<to>/<file>/
    ./hello