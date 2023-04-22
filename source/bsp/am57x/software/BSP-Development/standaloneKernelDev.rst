.. _kerneldev-57:

Standalone Kernel Development
=============================

Building the BSP in its entirety has a fairly large learning curve and significantly larger system requirements on the Host Machine when compared to building just the individual components of the image. For these reasons (and others), the Yocto Project can be very cumbersome to use as your primary means of developing things like the Linux kernel. When possible, it is best to clone the kernel repo independently of the overall BSP in order to customize it for your application requirements.

The goal of this guide is to provide you with a quick reference for setting up and building the stock PD20.1.3 kernel independently, without The Yocto Project. This can then serve as a starting point for kernel development.

.. note::
    Eventually, you will have a set of patches that modify the Linux kernel such that the phyCORE-AM57x SOM is able to meet your unique application requirements. This collection of patches should eventually be consolidated into a custom Meta-Layer specific to your system and added in a modular way to the BSP so that they are incorporated into the production-ready software image automatically. Instructions for doing this specifically with the phyCORE-AM57x BSP are not yet available but general resources for doing this can be found in various places online right now! Feel free to contact support@phytec.com if you need some help!
    
Requirements
------------

In order to build the kernel repository independently of the overall BSP, you will need to install a compatible toolchain for the phyCORE-AM57x. You may have already done this if you followed the :ref:`BuildTheBSP-57` guide, in which case you can just run the last two commands that export the environment variables you need.

.. code-block:: none
    :caption: Host (Ubuntu)

    wget https://developer.arm.com/-/media/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz
    mkdir /opt/PHYTEC_BSPs
    tar -Jxvf gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz -C /opt/PHYTEC_BSPs
    rm gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz

    export CROSS_COMPILE=/opt/PHYTEC_BSPs/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf/bin/arm-linux-gnueabihf-
    export ARCH=arm

The installation of a cross-compilation toolchain is also covered in :ref:`InstallSDK-57` and that toolchain could also be used instead (the toolchain is configured the same as the one used in the :ref:`BuildTheBSP-57`, but if you have heavily modified your rootfs it is advisable to generate a new one yourself and use that instead).

Clone the Linux kernel
----------------------

Clone the PHYTEC kernel repository using the release tag corresponding to the BSP PD20.1.3:

.. code-block:: none
    :caption: Host (Ubuntu)

    cd ~
    git clone https://stash.phytec.com/scm/pub/linux-phytec-ti.git -b BSP-Yocto-TISDK-AM57xx-PD20.1.3
    cd linux-phytec-ti

Make
----

The kernel build system leverages various environment variables and makefiles to build the kernel and it's components for a specific target architecture. Reference the following commands when building for the phyCORE-AM57x:

.. code-block:: none
    :caption: Host (Ubuntu)

    #to set kernel config (note this will overwrite .config settings and set to default PHYTEC kernel configuration):
    make am57xx_phycore_kit_defconfig
 
    #To build everything (includes the zImage, DTB, and kernel modules per the default config):
    make

    #to make kernel config changes (enable/disable drivers):
    make menuconfig
 
    #to save kernel config changes from .config to a file named "defconfig":
    make savedefconfig
 
    #To only build a specific dtb (saves time):
    make <dtb name>, example: "make am57xx-phycore-kit.dtb"
 
 
    #To only build the kernel:
    make zImage
 
 
    # To install kernel modules (which get built with the "make" command above):
    make modules_install INSTALL_MOD_PATH=<path to /rootfs/ on sd card>
 
Please reference the steps in Create a Bootable SD card for copying the new kernel components to a bootable SD Card.