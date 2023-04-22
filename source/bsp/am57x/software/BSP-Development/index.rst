.. _BSPDev-57:

BSP Development
===============

This section of the developer wiki contains guides for common BSP development tasks. These common tasks relate to modifying the standard development kit's software as well as modifying the BSP to add support for custom systems built around the phyCORE-AM64x SOM.

As for suggested workflow, most developers working with PHYTEC SOMs will want to start in one of these two ways:

* Generally, the best place to start is to :ref:`BuildTheBSP-57` in its entirety. Doing so will build the bootloader, kernel, rootfilesystem, and many utilities that make up the base Linux distro. Building the BSP gives you access to the source code for all of these components and can serve as a starting point for generating customized production software images.
* If you only need to modify the kernel, you can do so by following the :ref:`kerneldev-57` guide in order to leverage a pre-built SDK to build and then modify your Linux kernel independently. This is much faster than building the BSP in its entirety (you can eventually just export your changes as patches that the BSP can then apply automatically when you are ready).

.. toctree::
   :maxdepth: 1

   buildBSP.rst
   standaloneKernelDev.rst
