.. Download links
.. _`static-pdf-dl`: ../_static/master.pdf

.. Yocto
.. |yocto-branch| replace:: master
.. |yocto-codename| replace:: Unstable
.. |yocto-ref-manual| replace:: Yocto Reference Manual
.. |distro| replace:: ampliphy

.. References
.. |ref-gen-source-mirrors| replace:: :ref:`master_gen-source-mirrors`
.. |ref-temporary-method| replace:: :ref:`master_temporary-method`

.. _layerindex: https://layers.openembedded.org/layerindex/branch/master/layers/
.. _Bitbake: https://docs.yoctoproject.org/bitbake/dev/index.html
.. _Toaster: https://docs.yoctoproject.org/dev/toaster-manual/index.html
.. _megamanual: https://docs.yoctoproject.org/dev/singleindex.html
.. _manual: https://docs.yoctoproject.org/dev/dev-manual/index.html
.. _Supported Distributions: https://docs.yoctoproject.org/dev/ref-manual/system-requirements.html#supported-linux-distributions
.. _Yocto Board Support Package: https://docs.yoctoproject.org/dev/bsp-guide/index.html
.. _Quick Build: https://docs.yoctoproject.org/dev/brief-yoctoprojectqs/index.html
.. _meta-security: https://layers.openembedded.org/layerindex/branch/master/layer/meta-security/
.. _Yocto Documentation - Customizing Yocto builds: https://docs.yoctoproject.org/dev/singleindex.html#user-configuration
.. _Creating Layers: https://docs.yoctoproject.org/dev/dev-manual/layers.html#understanding-and-creating-layers
.. _Yocto - Devtool: https://docs.yoctoproject.org/dev/sdk-manual/extensible.html#using-devtool-in-your-sdk-workflow
.. _Devtool Quick Reference: https://docs.yoctoproject.org/dev/ref-manual/devtool-reference.html
.. _Autotools-Based Projects: https://docs.yoctoproject.org/dev/singleindex.html#autotools-based-projects
.. _Yocto - Kernel Development Manual: https://docs.yoctoproject.org/dev/kernel-dev/index.html
.. _Yocto - Development Manual: https://docs.yoctoproject.org/dev/dev-manual/index.html
.. _FEATURES: https://docs.yoctoproject.org/dev/ref-manual/features.html#features

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-------------------------------------------------------------+
| |yocto-ref-manual|                                          |
+=======================+=====================================+
| Document Title        | |yocto-ref-manual| |yocto-codename| |
+-----------------------+-------------------------------------+
| Document Type         | Yocto Manual                        |
+-----------------------+-------------------------------------+
| Is Branch of          | |yocto-ref-manual|                  |
+-----------------------+-------------------------------------+

.. _yocto-man-master:

.. include:: include/yocto-introduction.rsti

Compatible Linux Distributions
==============================

To build *Yocto* you need a compatible *Linux* host development machine. The
list of supported distributions can be found in the reference manual:
https://docs.yoctoproject.org/dev/ref-manual/system-requirements.html#supported-linux-distributions

.. include:: include/bsp-introduction.rsti

.. include:: include/prebuilt-images.rsti

.. include:: include/bsp-workspace-installation.rsti

.. include:: include/phylinux-documentation.rsti

.. include:: include/build-container.rsti

Working with Poky and Bitbake
=============================

.. include:: include/poky_bitbake/start_the_build.rsti
.. include:: include/poky_bitbake/images.rsti
.. include:: include/poky_bitbake/development_states.rsti
.. include:: include/poky_bitbake/bsp_features.rsti

.. _master_bsp-customization:

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

.. include:: include/poky_bitbake/bsp_customization/features.rsti
.. include:: include/poky_bitbake/bsp_customization/disable_qtdemo.rsti
.. include:: include/poky_bitbake/bsp_customization/framebuffer_console.rsti
.. include:: include/poky_bitbake/bsp_customization/provided_tools.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_software.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_layers.rsti
.. include:: include/poky_bitbake/bsp_customization/create_layer.rsti
.. include:: include/poky_bitbake/bsp_customization/kernel_bootloader_recipe.rsti
.. _yocto-man-master-kernel-and-bootloader-conf:
.. include:: include/poky_bitbake/bsp_customization/kernel_bootloader_config.rsti
.. _master_temporary-method:
.. include:: include/poky_bitbake/bsp_customization/kernel_bootloader_patch_devtool.rsti
.. include:: include/poky_bitbake/bsp_customization/kernel_bootloader_patch_tmp.rsti
.. include:: include/poky_bitbake/bsp_customization/kernel_bootloader_localconf.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_software_sustainable.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_firmware_rootfs.rsti
.. include:: include/poky_bitbake/bsp_customization/change_ubootenv_bbappend.rsti
.. include:: include/poky_bitbake/bsp_customization/change_bareboxenv_bbappend.rsti
.. _master_changing-net-config:
.. include:: include/poky_bitbake/bsp_customization/change_network_conf.rsti
.. include:: include/poky_bitbake/bsp_customization/change_wireless_network_conf.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_opencv.rsti
.. include:: include/poky_bitbake/bsp_customization/adding_php_webruntime.rsti

Common Tasks
------------

.. include:: include/poky_bitbake/common_tasks/debugging_apps.rsti
.. _master_gen-source-mirrors:
.. include:: include/poky_bitbake/common_tasks/gen_source_mirrors.rsti
.. include:: include/poky_bitbake/common_tasks/toolchains.rsti
.. include:: include/poky_bitbake/common_tasks/kernel_modules.rsti

.. include:: include/troubleshooting.rsti

.. include:: include/yocto-documentation.rsti
