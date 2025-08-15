.. Download links
.. _`static-pdf-dl`: ../_static/master.pdf

.. Yocto
.. |yocto-branch| replace:: master
.. |yocto-codename| replace:: Unstable
.. |yocto-ref-manual| replace:: Yocto Reference Manual
.. |distro| replace:: ampliphy

.. References
.. |ref-gen-source-mirrors| replace:: :ref:`master_gen-source-mirrors`

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

+-----------------+------------------+------------------+------------+
| Compatible BSPs | BSP Release Type | BSP Release Date | BSP Status |
+=================+==================+==================+============+
|                 |                  |                  |            |
+-----------------+------------------+------------------+------------+


This manual applies to all |yocto-codename| based PHYTEC releases.

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
https://docs.yoctoproject.org/dev/ref-manual/system-requirements.html#supported-linux-distributions

.. include:: include/bsp-introduction.rsti

.. include:: include/prebuilt-images.rsti

.. include:: include/bsp-workspace-installation.rsti

.. include:: include/phylinux-documentation.rsti

.. include:: include/build-container.rsti

.. include:: include/working_with_poky_and_bitbake.rsti

.. include:: include/troubleshooting.rsti

.. include:: include/yocto-documentation.rsti
