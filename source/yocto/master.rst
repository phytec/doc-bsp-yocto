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
.. |ref-build-container| replace:: :ref:`using build-container <master_build-container>`
.. |ref-phylinux-advanced-usage| replace:: :ref:`master_phylinux-advanced-usage`

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

.. include:: include/bsp-workspace-installation.rsti

.. include:: include/phylinux-documentation.rsti
   :end-before: .. phylinux-advanced-usage-marker

.. _master_phylinux-advanced-usage:

.. include:: include/phylinux-documentation.rsti
   :start-after: .. phylinux-advanced-usage-marker

.. _master_build-container:

.. include:: include/build-container.rsti

Working with Poky and Bitbake
=============================

.. include:: include/poky-bitbake/start-the-build.rsti
.. include:: include/poky-bitbake/images.rsti
.. include:: include/poky-bitbake/development-states.rsti
.. include:: include/poky-bitbake/bsp-features.rsti

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

.. include:: include/poky-bitbake/bsp-customization/features.rsti
.. include:: include/poky-bitbake/bsp-customization/disable-qtdemo.rsti
.. include:: include/poky-bitbake/bsp-customization/framebuffer-console.rsti
.. include:: include/poky-bitbake/bsp-customization/provided-tools.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-software.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-layers.rsti
.. include:: include/poky-bitbake/bsp-customization/create-layer.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-recipe.rsti
.. _yocto-man-master-kernel-and-bootloader-conf:
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-config.rsti
.. _master_temporary-method:
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-patch-devtool.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-patch-tmp.rsti
.. include:: include/poky-bitbake/bsp-customization/kernel-bootloader-localconf.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-software-sustainable.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-firmware-rootfs.rsti
.. include:: include/poky-bitbake/bsp-customization/change-ubootenv-bbappend.rsti
.. include:: include/poky-bitbake/bsp-customization/change-bareboxenv-bbappend.rsti
.. _master_changing-net-config:
.. include:: include/poky-bitbake/bsp-customization/change-network-conf.rsti
.. include:: include/poky-bitbake/bsp-customization/change-wireless-network-conf.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-opencv.rsti
.. include:: include/poky-bitbake/bsp-customization/adding-php-webruntime.rsti

Common Tasks
------------

.. include:: include/poky-bitbake/common-tasks/debugging-apps.rsti
.. _master_gen-source-mirrors:
.. include:: include/poky-bitbake/common-tasks/gen-source-mirrors.rsti
.. include:: include/poky-bitbake/common-tasks/toolchains.rsti
.. include:: include/poky-bitbake/common-tasks/kernel-modules.rsti

.. include:: include/troubleshooting.rsti

.. include:: include/yocto-documentation.rsti
