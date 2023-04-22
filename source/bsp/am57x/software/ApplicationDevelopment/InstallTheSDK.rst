.. _InstallSDK-57:

Install The SDK
===============

 The SDK includes a cross-compilation toolchain and sysroots directory for building your applications against, allowing your software that is built on your Ubuntu Host Machine to be executed on the phyCORE-AM57x SOM. This guide walks through the installation of the SDK and how to use it to cross-compile a basic Hello World example for running on the phyCORE-AM57x's Cortex-A15 cores.

 .. note::
    This guide will walkthrough the SDK installation using a the pre-built SDK installer, but head over to the :ref:`BuildTheBSP-57` guide if you require building your own.

Requirements
------------

The following system requirements are recommended to successfully install the SDK and to eventually build the BSP in its entirety. Deviations from these requirements may suffice if you don't intend to use the same machine for building the BSP:

* Ubuntu 18.04 LTS, 64-bit Host Machine with root permission
  
  * If using a virtual machine, VMWare Workstation, VMWare Player, and VirtualBox are all viable solutions.

* 500GB free disk space or greater (can be smaller if you don't intend to build the BSP)
  
* 8GB of RAM or greater
  
* 4x processing cores available to the Ubuntu Host Machine or greater
  
* SD card reader operational under Linux
  
* Active Internet connection

Host Setup
----------

To meet the general requirements for working with the pre-built SDK, as well as for building the BSP, install the following packages to the Ubuntu Host Machine:

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    sudo apt-get update
    sudo apt-get install git build-essential python python3 diffstat texinfo gawk chrpath dos2unix wget unzip socat doxygen libc6:i386 libncurses5:i386 libstdc++6:i386 libz1:i386 bison flex lzop libssl-dev u-boot-tools curl

Download the Pre-Built SDK
--------------------------

First, navigate to a directory containing the SDK installer. If you built it yourself, it will be found at *$BUILDDIR/arago-tmp-external-arm-toolchain/deploy/images/<MACHINE>* (checkout the :ref:`BuildTheBSP-57` guide for more information on how to do that):

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    cd ~/Downloads

Use the following command to download the pre-built SDK installer to the current working directory:

.. code-block:: none
    :caption: "Host (Ubuntu)"

    wget https://artifactory.phytec.com/artifactory/am57xx-images-released-public/BSP-Yocto-TISDK-AM57xx-PD20.1.3/processor-sdk-linux-bundle-am57xx-phycore-kit.tar.xz

.. note::
    Links for downloading the pre-built SDK installer, along with other pre-built binaries, can be found on the :ref:`PreBuilts-57` page.

Setup the SDK
-------------

Create a directory to house the SDK and then unpack the SDK into it: 

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    mkdir ~/Downloads/AM5_PSDK
    tar -Jxvf processor-sdk-linux-bundle-am57xx-phycore-kit.tar.xz -C ~/Downloads/AM5_PSDK
    rm processor-sdk-linux-bundle-am57xx-phycore-kit.tar.xz

Run the SDK installer:

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    cd ~/Downloads/AM5_PSDK
    ./sdk-install.sh

Source the Cross-Compilation Environment
----------------------------------------

Run the following command to automatically export variables pointing to the cross-compilation toolchain:

.. code-block:: none
    :caption: "Host (Ubuntu)"
    
    source ~/Downloads/AM5_PSDK/linux-devkit/environment-setup

.. note::
    You will need to source this cross-compilation environment every time you want to cross-compile using a new terminal session on your host machine.

Now you can leverage the cross-compilation toolchain in your project!

.. code-block:: none
    :caption: "Example Output"
    
    [linux-devkit]:~/Downloads/AM5_PSDK> which $CC
    /home/user/Downloads/AM5_PSDK/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-linux-gnueabihf-gcc

Now head over to the Hello World guide to walk through an example using it.