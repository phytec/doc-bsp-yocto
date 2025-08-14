.. Download links
.. _`static-pdf-dl`: ../_static/master.pdf

.. Yocto
.. |yocto-codename| replace:: Unstable
.. |yocto-ref-manual| replace:: Yocto Reference Manual
.. |distro| replace:: ampliphy
.. _layerindex: https://layers.openembedded.org/layerindex/branch/master/layers/

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

.. include:: ../phytec_documentation.rsti

On top of these standard manuals and guides, PHYTEC will also provide Product
Change Notifications, Application Notes, and Technical Notes. These will be done
on a case-by-case basis. Most of the documentation can be found in the
applicable download page of our products.

Compatible Linux Distributions
==============================

To build *Yocto* you need a compatible *Linux* host development machine. The
list of supported distributions can be found in the reference manual:
https://docs.yoctoproject.org/dev/ref-manual/system-requirements.html#supported-linux-distributions

.. include:: include/bsp_introduction.rsti

.. include:: include/prebuilt_images.rsti

.. include:: include/bsp_workspace_installation.rsti

.. include:: include/phylinux_documentation.rsti

.. include:: include/build_container.rsti

.. include:: include/working_with_poky_and_bitbake.rsti

.. include:: include/troubleshooting.rsti

.. include:: include/yocto_documentation.rsti
