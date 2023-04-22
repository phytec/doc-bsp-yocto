Software Development
====================

When beginning to consider the phyCORE-AM64x SOM as a part of your system design, it can be a little difficult to know where to start. Here is a suggested work flow:

* Work through the :ref:`Quickstart-57` first to boot the development kit and then head over to Peripherals-57 to help you exercise the hardware. Depending on your system requirements, this might be all you need to begin scripting and developing the basic functionality of your system directly on the target.
* If you are ready to begin writing custom applications on your target hardware, checkout the :ref:`ApplicationDev-57` guides to help you get your projects started.
* Once you have identified any limitations with the default phyCORE-AM64x development kit and BSP, the next step is to modify the hardware and software to meet your project requirements. Head over to the :ref:`BSPDev-57` page to begin working on your production image. Once built, you are free to modify it in order to support your custom design (phyCORE-AM64x SOM + custom carrier board).

This Linux BSP is built using `The Yocto Project <https://www.yoctoproject.org/>`_. Yocto is a powerful toolset that allows OEMs to create production ready software images for custom hardware. The BSP is configured by default to support the phyCORE-AM64x development kit and using tools provided by the `OpenEmbedded <https://www.openembedded.org/wiki/Main_Page>`_ build system, support for custom hardware built around the phyCORE-AM64x SOM can be easily integrated in a modular fashion into PHYTEC's base BSP. 

.. toctree::
   :maxdepth: 1

   releasenotes/index.rst
   ApplicationDevelopment/index.rst
   BSP-Development/index.rst
   prebuiltbinaries/PreBuiltBinaries.rst

.. note:: 
    For technical support, please visit `PHYTEC's Support Portal <http://support.phytec.com/>`_!
