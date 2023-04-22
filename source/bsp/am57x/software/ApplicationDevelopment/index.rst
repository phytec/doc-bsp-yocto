.. _ApplicationDev-57:

Application Development
=======================
.. note:: 
   This section of the product wiki contains guides for common development tasks associated with application development for the phyCORE-AM57x SOM.

Embedded application development for systems running Linux can generally be approached in two ways; Native and Cross-Platform application development.

**Native** application development involves writing and compiling applications directly on the system the application is intended to run. In practice, this would look like:

* Boot a PHYTEC development kit into Linux (these will typically be dual Cortex-A15s with 2GBs of RAM).
* Use Serial or SSH to gain access to the target system's shell (a shell allows users to directly interact with an operating system via a command line interface).
* Write your application directly on the target system using text editors included within the target's operating system distribution.
* Compile your application using a toolchain included within the target's operating system distribution.
* Run the application directly on the target system.

Native application development is a great option for small, quick-turn prototypes or projects where you want to try out something quickly. 

However, you'll find as your projects grow in complexity that the compute resources available to your resource-constrained embedded device may be insufficient; this can culminate in projects taking a very long time to compile. Furthermore, you may find the development tools available on embedded systems to be limiting. An easy example is that you won't have any graphical text editors available!

**Cross-Platform** application development (generally) involves leveraging a second, more powerful "Host Machine" or "Build Server" with access to greater compute resources and development tools. In practice, this would look like:

* Boot up a Linux Host Machine (A good example of this could be a x86 desktop computer with 16 cores, 32GB of RAM and operates at 5GHz+. This also could be much much more if setup in the cloud!)
* Install a SDK or standalone cross-compilation toolchain. Cross-compilation toolchains work on one kind of system architecture (x86 in our example), and compile applications to run on another architecture (in this case our target system would be the phyCORE-AM57x's ARM Cortex-A15s).
* Write and cross-compile the application on the Host Machine.
* Transfer the cross-compiled binary to the target system and then run it (attempting to run cross-compiled binaries on the Host Machine will not work).

Cross-compilation development environments usually take a little more work upfront to initially setup but can ultimately provide more compute resources and development tools to developers.

.. toctree::
   :maxdepth: 1
 
   ./InstallTheSDK.rst
   ./hello.rst
   ./dsp.rst