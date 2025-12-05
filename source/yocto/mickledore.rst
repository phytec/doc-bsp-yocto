.. Download links
.. _`static-pdf-dl`: ../_static/mickledore.pdf

.. Yocto
.. |yocto-branch| replace:: mickledore
.. |yocto-codename| replace:: Mickledore
.. |yocto-ref-manual| replace:: Yocto Reference Manual
.. |distro| replace:: ampliphy-vendor-xwayland

.. References
.. |ref-gen-source-mirrors| replace:: :ref:`mickledore_gen-source-mirrors`
.. |ref-temporary-method| replace:: :ref:`mickledore_temporary-method`
.. |ref-phylinux-advanced-usage| replace:: :ref:`mickledore_phylinux-advanced-usage`

.. _layerindex: https://layers.openembedded.org/layerindex/branch/mickledore/layers/
.. _Bitbake: https://docs.yoctoproject.org/bitbake/2.4/index.html
.. _Toaster: https://docs.yoctoproject.org/4.2.4/toaster-manual/index.html
.. _megamanual: https://docs.yoctoproject.org/4.2.4/singleindex.html
.. _manual: https://docs.yoctoproject.org/4.2.4/dev-manual/index.html
.. _Supported Distributions: https://docs.yoctoproject.org/4.2.4/ref-manual/system-requirements.html#supported-linux-distributions
.. _Yocto Board Support Package: https://docs.yoctoproject.org/4.2.4/bsp-guide/index.html
.. _Quick Build: https://docs.yoctoproject.org/4.2.4/brief-yoctoprojectqs/index.html
.. _meta-security: https://layers.openembedded.org/layerindex/branch/mickledore/layer/meta-security/
.. _Yocto Documentation - Customizing Yocto builds: https://docs.yoctoproject.org/4.2.4/singleindex.html#user-configuration
.. _Creating Layers: https://docs.yoctoproject.org/4.2.4/dev-manual/layers.html#understanding-and-creating-layers
.. _Yocto - Devtool: https://docs.yoctoproject.org/4.2.4/sdk-manual/extensible.html#using-devtool-in-your-sdk-workflow
.. _Devtool Quick Reference: https://docs.yoctoproject.org/4.2.4/ref-manual/devtool-reference.html
.. _Autotools-Based Projects: https://docs.yoctoproject.org/4.2.4/singleindex.html#autotools-based-projects
.. _Yocto - Kernel Development Manual: https://docs.yoctoproject.org/4.2.4/kernel-dev/index.html
.. _Yocto - Development Manual: https://docs.yoctoproject.org/4.2.4/dev-manual/index.html

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-------------------------------------------------------------+
| |yocto-ref-manual|                                          |
+=======================+=====================================+
| Document Title        | |yocto-ref-manual| |yocto-codename| |
+-----------------------+-------------------------------------+
| Document Type         | Yocto Manual                        |
+-----------------------+-------------------------------------+
| Release Date          | XXXX/XX/XX                          |
+-----------------------+-------------------------------------+
| Is Branch of          | |yocto-ref-manual|                  |
+-----------------------+-------------------------------------+

+----------------------------------+------------------+------------------+------------+
| Compatible BSPs                  | BSP Release Type | BSP Release Date | BSP Status |
+==================================+==================+==================+============+
| BSP-Yocto-NXP-i.MX93-PD24.1.0    | Major            | 05.02.2024       | released   |
+----------------------------------+------------------+------------------+------------+
| BSP-Yocto-NXP-i.MX93-PD24.1.1    | Minor            | 08.05.2024       | released   |
+----------------------------------+------------------+------------------+------------+


This manual applies to all |yocto-codename| based PHYTEC releases.

.. _yocto-man-mickledore:

.. include:: ../phytec-documentation.rsti

On top of these standard manuals and guides, PHYTEC will also provide Product
Change Notifications, Application Notes, and Technical Notes. These will be done
on a case-by-case basis. Most of the documentation can be found in the
applicable download page of our products.

.. include:: include/yocto-introduction.rsti

Compatible Linux Distributions
==============================

To build *Yocto* you need a compatible *Linux* host development machine. The
list of supported distributions can be found in the reference manual:
`Supported Distributions`_

.. include:: include/bsp-introduction.rsti

.. include:: include/prebuilt-images.rsti

BSP Workspace Installation
==========================

Setting Up the Host
-------------------

You can set up the host or use one of our build-container to run a Yocto build.
You need to have a running *Linux* distribution. It should be running on a
powerful machine since a lot of compiling will need to be done.

If you want to use a build-container, you only need to install following
packages on your host

.. code-block:: console

   host:~$ sudo apt install wget git

Continue with the next step :ref:`mickledore_git-config` after that.
The documentation for using build-container can be found in this manual after
:ref:`mickledore_phylinux-advanced-usage` of phyLinux.

Else *Yocto* needs a handful of additional packages on your host. For *Ubuntu*
you need

.. code-block:: console

   host:~$ sudo apt install gawk wget git diffstat unzip texinfo \
         gcc build-essential chrpath socat cpio python3 python3-pip \
         python3-pexpect xz-utils debianutils iputils-ping python3-git \
         python3-jinja2 libegl1-mesa libsdl1.2-dev \
         python3-subunit mesa-common-dev zstd liblz4-tool file locales


For other distributions you can find information in the *Yocto* Quick Build:
`Quick Build`_

.. _mickledore_git-config:

Git Configuration
-----------------

The BSP heavily utilizes *Git*. *Git* needs some information from
you as a user to identify who made changes. Create a ``~/.gitconfig`` with the
following content, if you do not have one

.. code-block:: kconfig

   [user]
       name = <Your Name>
       email = <Your Mail>
   [core]
       editor = vim
   [merge]
       tool = vimdiff
   [alias]
       co = checkout
       br = branch
       ci = commit
       st = status
       unstage = reset HEAD --
       last = log -1 HEAD
   [push]
       default = current
   [color]
       ui = auto

You should set ``name`` and ``email`` in your *Git* configuration, otherwise,
*Bitbake* will complain during the first build. You can use the two commands to
set them directly without editing ``~/.gitconfig`` manually

.. code-block:: console

   host:~$ git config --global user.email "your_email@example.com"
   host:~$ git config --global user.name "name surname"

site.conf Setup
---------------

Before starting the *Yocto* build, it is advisable to configure the development
setup. Two things are most important: the download directory and the cache
directory. PHYTEC strongly recommends configuring the setup as it will reduce
the compile time of consequent builds.

A download directory is a place where *Yocto* stores all sources fetched from
the internet. It can contain tar.gz, *Git* mirror, etc. It is very useful to set
this to a common shared location on the machine. Create this directory with 777
access rights. To share this directory with different users, all files need to
have group write access. This will most probably be in conflict with default
*umask* settings. One possible solution would be to use ACLs for this
directory

.. code-block:: console

   host:~$ sudo apt-get install acl
   host:~$ sudo setfacl -R -d -m g::rwx <dl_dir>

If you have already created a download directory and want to fix the permissions
afterward, you can do so with

.. code-block:: console

   host:~$ sudo find /home/share/ -perm /u=r ! -perm /g=r -exec chmod g+r \{\} \;
   host:~$ sudo find /home/share/ -perm /u=w ! -perm /g=w -exec chmod g+w \{\} \;
   host:~$ sudo find /home/share/ -perm /u=x ! -perm /g=x -exec chmod g+x \{\} \;

The cache directory stores all stages of the build process. *Poky* has quite an
involved caching infrastructure. It is advisable to create a shared directory,
as all builds can access this cache directory, called the shared state cache.

Create the two directories on a drive where you have approximately 50 GB of
space and assign the two variables in your ``build/conf/local.conf``::

   DL_DIR ?= "<your_directory>/yocto_downloads"
   SSTATE_DIR ?= "<your_directory>/yocto_sstate"

If you want to know more about configuring your build, see the documented
example settings

.. code-block::

   sources/poky/meta-yocto/conf/local.conf.sample
   sources/poky/meta-yocto/conf/local.conf.sample.extended

phyLinux Documentation
======================

The phyLinux script is a basic management tool for PHYTEC *Yocto* BSP releases
written in *Python*. It is mainly a helper to get started with the BSP
structure. You can get all the BSP sources without the need of interacting with
*Repo* or *Git*.

The phyLinux script has only one real dependency. It requires the *wget* tool
installed on your host. It will also install the `Repo tool
<https://source.android.com/docs/setup/download>`_ in a global path
(/usr/local/bin) on your host PC. You can install it in a different location
manually. *Repo* will be automatically detected by phyLinux if it is found in
the PATH. The *Repo* tool will be used to manage the different *Git*
repositories of the *Yocto* BSP.

Get phyLinux
------------

The phyLinux script can be found on the PHYTEC download server:
https://download.phytec.de/Software/Linux/Yocto/Tools/phyLinux

Basic Usage
-----------

For the basic usage of phyLinux, type

.. code-block:: console

   host:~$ ./phyLinux --help

which will result in

.. code-block::

   usage: phyLinux [-h] [-v] [--verbose] {init,info,clean} ...

   This Programs sets up an environment to work with The Yocto Project on Phytecs
   Development Kits. Use phyLinx <command> -h to display the help text for the
   available commands.

   positional arguments:
     {init,info,clean}  commands
       init             init the phytec bsp in the current directory
       info             print info about the phytec bsp in the current directory
       clean            Clean up the current working directory

   optional arguments:
     -h, --help         show this help message and exit
     -v, --version      show program's version number and exit
     --verbose

Initialization
--------------

Create a fresh project folder

.. code-block:: console

   host:~$ mkdir ~/yocto

Calling phyLinux will use the default Python version. Starting with Ubuntu 20.04
it will be Python3. If you want to initiate a BSP, which is not compatible with
Python3, you need to set Python2 as default (temporarily) before running
phyLinux

.. code-block:: console

   host:~$ ln -s \`which python2\` python && export PATH=`pwd`:$PATH

Now run phyLinux from the new folder

.. code-block:: console

   host:~$ ./phyLinux init

A clean folder is important because phyLinux will clean its working directory.
Calling phyLinux from a directory that isn't empty will result in the following
**warning**::

   This current directory is not empty. It could lead to errors in the BSP
   configuration process if you continue from here. At the very least, you
   have to check your build directory for settings in bblayers.conf and
   local.conf, which will not be handled correctly in all cases. It is
   advisable to start from an empty directory of call:
   $ ./phyLinux clean
   Do you really want to continue from here?
   [yes/no]:

On the first initialization, the phyLinux script will ask you to install the
*Repo* tool in your */usr/local/bin* directory. During the execution of the
*init* command, you need to choose your processor platform (SoC), PHYTEC's BSP
release number, and the hardware you are working on

.. code-block::

   ***************************************************
   * Please choose one of the available SoC Platforms:
   *
   *   1: am335x
   *   2: am57x
   *   3: am62ax
   *   4: am62x
   *   5: am64x
   *   6: am68x
   *   7: imx6
   *   8: imx6ul
   *   9: imx7
   *   10: imx8
   *   11: imx8m
   *   12: imx8mm
   *   13: imx8mp
   *   14: imx8x
   *   15: imx93
   *   16: nightly
   *   17: rk3288
   *   18: stm32mp13x
   *   19: stm32mp15x
   *   20: topic

   # Exemplary output for chosen imx93
   ***************************************************
   * Please choose one of the available Releases:
   *
   *   1: BSP-Yocto-NXP-i.MX93-ALPHA1
   *   2: BSP-Yocto-NXP-i.MX93-PD24.1-rc1
   *   3: BSP-Yocto-NXP-i.MX93-PD24.1.0
   *   4: BSP-Yocto-NXP-i.MX93-PD24.1.1-rc1
   *   5: BSP-Yocto-NXP-i.MX93-PD24.1.1-rc2
   *   6: BSP-Yocto-NXP-i.MX93-PD24.1.1-rc3
   *   7: BSP-Yocto-NXP-i.MX93-PD24.1.1

   # Exemplary output for chosen BSP-Yocto-NXP-i.MX93-PD24.1.1
   *********************************************************************
   * Please choose one of the available builds:
   *
   no:                 machine: description and article number
                                distro: supported yocto distribution
                                target: supported build target

   1: phyboard-nash-imx93-1:  PHYTEC phyBOARD-Nash i.MX93
                              2 GB RAM, eMMC
                              PB-04729-001, PCL-077-23231211I
                              distro: ampliphy-vendor
                              target: phytec-headless-image
   2: phyboard-nash-imx93-1:  PHYTEC phyBOARD-Nash i.MX93
                              2 GB RAM, eMMC
                              PB-04729-001, PCL-077-23231211I
                              distro: ampliphy-vendor-rauc
                              target: phytec-headless-bundle
   3: phyboard-nash-imx93-1:  PHYTEC phyBOARD-Nash i.MX93
                              2 GB RAM, eMMC
                              PB-04729-001, PCL-077-23231211I
                              distro: ampliphy-vendor-wayland
                              target: -c populate_sdk phytec-qt6demo-image
                              target: phytec-qt6demo-image
   4: phyboard-segin-imx93-2: PHYTEC phyBOARD-Segin i.MX93
                              1 GB RAM, eMMC, silicon revision A1
                              PB-02029-001, PCL-077-11231010I
                              distro: ampliphy-vendor
                              target: phytec-headless-image
   5: phyboard-segin-imx93-2: PHYTEC phyBOARD-Segin i.MX93
                              1 GB RAM, eMMC, silicon revision A1
                              PB-02029-001, PCL-077-11231010I
                              distro: ampliphy-vendor-rauc
                              target: phytec-headless-bundle
   6: phyboard-segin-imx93-2: PHYTEC phyBOARD-Segin i.MX93
                              1 GB RAM, eMMC, silicon revision A1
                              PB-02029-001, PCL-077-11231010I
                              distro: ampliphy-vendor-wayland
                              target: phytec-qt6demo-image

If you cannot identify your board with the information given in the selector,
have a look at the invoice for the product. After the configuration is done,
you can always run

.. code-block:: console

   host:~$ ./phyLinux info

   # Exemplary output
   **********************************************
   * The current BSP configuration is:
   *
   * SoC:  refs/heads/imx93
   * Release:  BSP-Yocto-NXP-i.MX93-PD24.1.1
   * Machine:  phyboard-segin-imx93-2
   *
   **********************************************

to see which SoC and Release are selected in the current workspace. If
you do not want to use the selector, phyLinux also supports command-line
arguments for several settings

.. code-block:: console

   host:~$ MACHINE=phyboard-segin-imx93-2 ./phyLinux init -p imx93 -r BSP-Yocto-NXP-i.MX93-PD24.1.1

or view the help command for more information

.. code-block:: console

   host:~$ ./phyLinux  init --help

   usage: phyLinux init [-h] [--verbose] [--no-init] [-o REPOREPO] [-b REPOREPO_BRANCH] [-x XML] [-u URL] [-p PLATFORM] [-r RELEASE]

   options:
     -h, --help          show this help message and exit
     --verbose
     --no-init           dont execute init after fetch
     -o REPOREPO         Use repo tool from another url
     -b REPOREPO_BRANCH  Checkout different branch of repo tool
     -x XML              Use a local XML manifest
     -u URL              Manifest git url
     -p PLATFORM         Processor platform
     -r RELEASE          Release version

After the execution of the *init* command, phyLinux will print a few important
notes as well as information for the next steps in the build process.

.. _mickledore_phylinux-advanced-usage:

Advanced Usage
--------------

phyLinux can be used to transport software states over any medium. The state of
the software is uniquely identified by *manifest.xml*. You can create a
manifest, send it to another place and recover the software state with

.. code-block:: console

   host:~$ ./phyLinux init -x manifest.xml

You can also create a *Git* repository containing your software states. The
*Git* repository needs to have branches other than master, as we reserved the
master branch for different usage. Use phyLinux to check out the states

.. code-block:: console

   host:~$ ./phyLinux -u <url-of-your-git-repo>

.. include:: include/build-container.rsti

Working with Poky and Bitbake
=============================

.. include:: include/poky-bitbake/start-the-build.rsti
.. include:: include/poky-bitbake/images.rsti
.. include:: include/poky-bitbake/development-states.rsti
.. include:: include/poky-bitbake/bsp-features.rsti

.. _mickledore_bsp-customization:

BSP Customization
-----------------

To get you started with the BSP, we have summarized some basic tasks from the
*Yocto* official documentation. It describes how to add additional software to
the image, change the kernel and bootloader configuration, and integrate
patches for the kernel and bootloader.

Minor modifications, such as adding software, are done in the file
*build/conf/local.conf*. There you can overwrite global configuration variables
and make small modifications to recipes.

There are 2 ways to make major changes:

1. Either create your own layer and use *bbappend* files.
2. Add everything to PHYTEC's Distro layer *meta-ampliphy*.

Creating your own layer is described in the section Create your own Layer.

.. include:: include/poky-bitbake/bsp-customization/disable-qtdemo.rsti
.. include:: include/poky-bitbake/bsp-customization/framebuffer-console.rsti
.. include:: include/poky-bitbake/bsp-customization/provided-tools.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-software.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-layers.rsti
.. include:: include/poky-bitbake/bsp-customization/create-layer.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-recipe.rsti
.. _yocto-man-mickledore-kernel-and-bootloader-conf:
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-config.rsti
.. _mickledore_temporary-method:
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-patch-devtool.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-patch-tmp.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-localconf.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-software-sustainable.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-firmware-rootfs.rsti
.. include:: include/poky-bitbake/bsp-customization/change-ubootenv-bbappend.rsti
.. include:: include/poky-bitbake/bsp-customization/change-bareboxenv-bbappend.rsti
.. _mickledore_changing-net-config:
.. include:: include/poky-bitbake/bsp-customization/change-network-conf.rsti
.. include:: include/poky-bitbake/bsp-customization/change-wireless-network-conf.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-opencv.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-php-webruntime.rsti

Common Tasks
------------

.. include:: include/poky-bitbake/common-tasks/debugging-apps.rsti
.. _mickledore_gen-source-mirrors:
.. include:: include/poky-bitbake/common-tasks/gen-source-mirrors.rsti
.. include:: include/poky-bitbake/common-tasks/toolchains.rsti
.. include:: include/poky-bitbake/common-tasks/kernel-modules.rsti

.. include:: include/troubleshooting.rsti

.. include:: include/yocto-documentation.rsti
