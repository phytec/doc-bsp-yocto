.. _BuildTheBSP-57:

Build the BSP
==============

.. note::
  Custom SOMs 
  
  If you have purchased a SOM that is not a standard configuration (ie it was customized specifically at your request by PHYTEC), there may be additional steps required to build this BSP release for your configuration. For each SOM configuration there may be a required change to Linux, the bootloader, or the MACHINE configuration in Yocto. Please reach out to PHYTEC support for more information.

This BSP Development Guide provides you with the tools and know-how to install and work with the Linux Board Support Package (BSP) for the phyCORE-AM57x Development Kit. The guide will walk-through how to install the appropriate tools and source, build custom kernels, deploy the OS, and how to exercise the software and hardware. Please refer to the phyCORE-AM57xx Hardware Manual for specific information on board-level features such as jumper configuration, memory mapping and pin layout for the phyCORE-AM57xx System on Module (SOM) and Carrier Board. Additionally, gain access to the SOM and baseboard schematics for the phyCORE-AM57xx kit by registering at the following: http://phytec.com/support/registration/.

.. note::
  See the :ref:`ReleaseNotes-57` for a list of the supported SOM's and carrier board versions supported in this release.

Requirements
------------

The following system requirements are necessary to successfully follow this BSP Development Guide. Deviations from these requirements may or may not have other workarounds:

* Ubuntu 18.04 LTS, 64-bit Host Machine with root permission.
 
  * If using a virtual machine, VMWare Workstation, VMWare Player, and VirtualBox are all viable solutions.
* At least 500GB disk space free
* At least 8GB of RAM
* At least 4x processing cores available to the Host Machine
* Active Internet connection
* SD Card reader operational under Linux

Host Setup
----------

Yocto development requires certain packages to be installed on the host machine to satisfy the build requirements. Run the following commands to ensure these are installed:

.. code-block:: none
    :caption: Host (Ubuntu)

    sudo apt-get update
    sudo apt-get install git build-essential python python3 diffstat texinfo gawk chrpath dos2unix wget unzip socat doxygen bison flex lzop libssl-dev u-boot-tools curl vim gcc-multilib g++-multilib

Verify that the preferred shell for your Host PC is ''bash'' and not ''dash'' (This step is **required** and is often missed):

.. code-block:: none
    :caption: Host (Ubuntu)

    sudo dpkg-reconfigure dash 
    # Respond "No" to the prompt asking "Install dash as /bin/sh?"

Install the 'repo' tool:

.. code-block:: none
  :caption: Host (Ubuntu)

  mkdir -p ~/.bin
  PATH="${HOME}/.bin:${PATH}"
  curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
  chmod a+rx ~/.bin/repo

.. note::
  These steps are crucial for building the BSP. Following the steps explicitly will save you from some puzzling build errors later in this guide. 
  Are you having build errors? Double check all recommended packages are installed and that you have your shell set for bash. 

Toolchain Installation
~~~~~~~~~~~~~~~~~~~~~~

Run the following commands to install the ARM toolchain to a dedicated *TOOLCHAIN* directory, needed by the Host Machine to compile the BSP for the target architecture. You can choose to set this up in another location as long as you have the appropriate user permissions in that location:

.. code-block:: none
    :caption: Host (Ubuntu)

    wget https://developer.arm.com/-/media/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz

    sudo mkdir -p /opt/bin
    # /opt/ directory has root permission, change the permissions so your user account can access this folder. In the following replace <user> with your specific username
    sudo chown -R <user>: /opt/bin

    tar -Jxvf gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz -C /opt/bin
    rm gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz

We will need the absolute path to the *~/TOOLCHAIN* directory we just created for later, run the following to help you get the absolute path:

.. code-block:: none
    :caption: Host (Ubuntu)

    cd ~/TOOLCHAIN
    pwd

Note the output of the 'pwd' command for later use. The absolute path will be something like */home/<user>/TOOLCHAIN* where <user> is replaced with your unique user account on your Ubuntu Host Machine. If you chose a custom location, be sure to get that path instead.

Git Setup
~~~~~~~~~

If you have not yet configured your git environment on the Host Machine, please execute the following commands to set your username and email address:

.. code-block:: none
    :caption: Host (Ubuntu)

    git config --global user.email "your@email.com" 
    git config --global user.name "Your Name"
    git config --global http.sslcainfo /etc/ssl/certs/ca-certificates.crt

The git protocol changed permanently on March 15th (see https://github.blog/2021-09-01-improving-git-protocol-security-github/) and thus some components called for in the BSP will require this additional git config in order to fetch properly:

.. code-block:: none
    :caption: Host (Ubuntu)

    echo -e '[url "https://github.com/"]\n  insteadOf = "git://github.com/"' >> ~/.gitconfig

.. note:: 
    New to git? See here for more information about getting started with git: https://git-scm.com/

Yocto Build Steps
-----------------

Firstly, dedicate a directory on your Host Machine for housing the BSP and navigate there:

.. code-block:: none
    :caption: Host (Ubuntu)

    mkdir ~/BSP-Yocto-TISDK-AM57xx-PD20.1.3
    cd ~/BSP-Yocto-TISDK-AM57xx-PD20.1.3

Download the BSP Meta Layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yocto based Linux BSPs are comprised of many meta-layers each containing recipes for fetching, building and packaging various components destined for the bootable software image. Some meta-layers are provided by the Linux community, such as meta-python for example. Other meta-layers are more platform specific and are made available by PHYTEC or the silicon vendor (Texas Instruments in the case of the AM57x Soc). All of these meta-layers can be setup using the repo tool:

.. code-block:: none
    :caption: Host (Ubuntu)

    repo init -u https://stash.phytec.com/scm/pub/manifests-phytec.git -b am57xx -m PD20.1.3.xml
    repo sync

Initialize the BSP Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source the build environment in order to automatically setup a *build* directory (a *$BUILDDIR* environment variable will be automatically exported here and it will reflect the path to the *build* directory):

.. code-block:: none
    :caption: Host (Ubuntu)

    TEMPLATECONF=`pwd`/sources/meta-phytec/meta-phytec-ti/conf source sources/oe-core/oe-init-build-env build

.. note::
  Once you have run the above once, you won't need to ever again. All new terminal sessions in the future can source the build environment simply by running the following commands:

  .. code-block:: none
    :caption: Host (Ubuntu)

    cd ~/BSP-Yocto-TISDK-AM57xx-PD20.1.3
    source sources/oe-core/oe-init-build-env

Configure the Build
~~~~~~~~~~~~~~~~~~~

We'll need to make some small changes to the build's configuration file manually, many more are possible here however. Open the build's configuration file using your favorite text editor. This guide will use 'vi' in order to modify the file directly in the terminal:

.. code-block:: none
    :caption: Host (Ubuntu)

    vi conf/local.conf

.. note:: 
    vi/vim is perhaps the most popular command line text editor in Linux but it's not the only way to modify text files. You could also try 'nano', which is a little more beginner friendly.

    The vi text editor begins in "Command Mode" and you must first hit the 'i' key in order to enter "Insert Mode". Using the arrow keys to navigate, make the necessary changes and then hit ESC to go back to "Command mode". Now enter ":wq" to write the file and quit.

Modify *conf/local.conf* after considering the following:

* Select a specific machine to target the build with.

  .. code-block:: none
    :caption: conf/local.conf

    MACHINE ?= "am57xx-phycore-kit"

  .. note::
    You can replace MACHINE=am57xx-phycore-kit in all of the build instructions with the appropriate MACHINE for your SOM configuration. The SOM-specific MACHINE targets can be found in the Yocto Machine Configuration Table section of the latest phyCORE-AM57x Linux BSP release notes. However, the am57xx-phycore-kit MACHINE target will produce images that work for all phyCORE-AM57x SOMs, assuming the SOM's onboard EEPROM is properly flashed. See Using the PHYTEC EEPROM Flashtool for more information.  

* Maximize the build's efficiency by modifying the BB_NUMBER_THREADS and PARALLEL_MAKE variables to suit your host development system. By default, these are set to 4 in build/conf/local.conf but can be increased or decreased according to the available resources of the Host Machine (these values directly impact build time):
  
  .. code-block:: none
    :caption: conf/local.conf

    # Parallelism options - based on cpu count
    BB_NUMBER_THREADS ?= "4"
    PARALLEL_MAKE ?= "-j 4"

* Add the following to a new line at the end of the file to set the TOOLCHAIN_BASE variable to point to where you extracted the toolchain in the steps above:

  .. code-block:: none
    :caption: conf/local.conf

    TOOLCHAIN_BASE = "/opt/bin"

* Be sure to save your changes to the local.conf file before closing the file.

Start the Build
---------------

Before we can start the build, increase the limit on open file descriptors in your bash shell from the default of 1024 to 8192:

.. code-block:: none
  :caption: Host (Ubuntu)

  ulimit -n 8192

.. note::
  Having trouble changing ulimit?

  You may need to modify some system configuration files in order to increase the limit. 

  Use your favorite text editor to modify the /etc/systemd/user.conf and /etc/systemd/system.conf files. Here is an example using vi:

  .. code-block:: none
    :caption: Host (Ubuntu)

    sudo vi /etc/systemd/user.conf

  Then set (or uncomment) the following line in the file (this line is commented out by default):

  .. code-block:: none
    :caption: /etc/systemd/user.conf

    DefaultLimitNOFILE=8192

  Repeat this in the /etc/systemd/system.conf file before rebooting the system like so:

  .. code-block:: none
    :caption: Host (Ubuntu)

    reboot

  Upon rebooting, you'll need to navigate to the ~/BSP-Yocto-TISDK-AM57xx-PD20.1.3 directory and re-source your build environment with the following commands to get back to where you were before the reboot:

  .. code-block:: none
    :caption: Host (Ubuntu)

    cd ~/BSP-Yocto-TISDK-AM57xx-PD20.1.3
    source sources/oe-core/oe-init-build-env

  You should now be able to successfully increase the open file descriptor limit to 8192 and continue with the rest of this guide.

The setup is complete and you now have everything ready to start a build. This BSP has been tested with the arago-core-tisdk-bundle and it is suggested that you start with this image before building other images. Alternate images are located in various meta layers at yocto_ti/sources/meta*/recipes*/images/*.bb. They can be found using the command bitbake-layers show-recipes "*-image*" in $BUILDDIR.

.. note::
  The default build target is arago-core-tisdk-bundle, which includes all TISDK demos and support.

  In the interest of creating a smaller image, we recommend using arago-base-tisdk-image. PHYTEC offers arago-base-tisdk-image binaries on Artifactory.

  * If building for am5726 or am5716 MACHINE targets, the video and graphics support will be removed from the output regardless of the image target as am57x6 hardware does not support these features.

The following will start a build from scratch. By default this build target will generate a bootloader, Linux kernel, root filesystem images, and a SDK by default.

.. code-block:: none
    :caption: Host (Ubuntu)

    cd $BUILDDIR
    bitbake arago-core-tisdk-bundle

.. note:: 
    Depending on the resources available on the Host Machine, this build process can take a long time to complete the first time. Subsequent builds introducing incremental changes can be completed MUCH faster because the build system can intelligently re-build only what is necessary. 

    Ideally, the BSP is built on a dedicated build server with a high core/thread count and a lot of RAM.

Components of a Built BSP
-------------------------

All generated images deployed during the build can be found in the *$BUILDDIR/arago-tmp-external-arm-toolchain/deploy/images/<MACHINE>* directory.

**Bootloader**:               MLO, u-boot.img
**Kernel**:                   zImage
**Kernel device tree file**:  am5728-phycore-kit-41300111i.dtb
**Root Filesystem**:          tisdk-rootfs-image-am57xx-phycore-kit.tar.xz
**SDK**:                      processor-sdk-linux-bundle-am57xx-phycore-kit.tar.xz 

Source Locations
----------------
**Kernel**: $BUILDDIR/arago-tmp-external-arm-toolchain/work/<MACHINE>-linux-gnueabi/linux-phytec-ti/4.19.79+git_v4.19.79-phy3-r7a/git/

.. note::
  The default device tree file to modify within the linux kernel source is: am5728-phycore-kit-41300111i.dts and its included dtsi files.

**U-boot**: $BUILDDIR/arago-tmp-external-arm-toolchain/work/<MACHINE>-linux-gnueabi/u-boot-phytec/2019.01+git_v2019.01-phy5-r0/git/

Build Time Optimizations
------------------------

The build time will vary depending on the package selection and Host performance. Beyond the initial build, after making modifications to the BSP, a full build is not required. Use the following as a reference to take advantage of optimized build options and reduce the build time.

To force U-boot to recompile before redeploying:

.. code-block:: none
    :caption: Host (Ubuntu)

    bitbake u-boot-phytec -f -c compile && bitbake u-boot-phytec

To force the Linux kernel to recompile before redeploying:

.. code-block:: none
    :caption: Host (Ubuntu)

    bitbake linux-phytec-ti -f -c compile && bitbake linux-phytec-ti

The Yocto project's Bitbake User Manual provides useful information regarding build options: http://www.yoctoproject.org/docs/2.6/bitbake-user-manual/bitbake-user-manual.html

The SDK
~~~~~~~

Once you have successfully followed the steps outlined above for building the BSP, you will find that a SDK has already been built for you (look above in the Built Images section to see its name and location). This will contains example applications and a standalone toolchain based on the Linux distribution built with Yocto.

Checkout :ref:`ApplicationDev-57` to get started with the SDK.

.. note:: 
    For technical support, please visit `PHYTEC's Support Portal <http://support.phytec.com/>`_!
