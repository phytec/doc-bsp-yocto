.. This file is used as a template for creating a new BSP Manual for a new
   family of SoCs. For existing BSP Manuals it is probably easier to copy the
   existing one and updating some content in it.

.. The following section defines substitutions used throughout the various BSP
   manual files. This is done so that there exists a central place to define all
   the important variables. Use the free space after the replace:: to write the
   definition. If unsure what to fill out, you can also look at existing
   documents.


.. Download links

.. Link to Support->BSP-Download Section for this release on PHYTEC Website
.. |dlpage-bsp| replace::
.. _dlpage-bsp:
.. Link to PHYTEC Website Downloads Section for this product
.. |dlpage-product| replace::
.. _dl-sdk:
.. _dl-server:
.. Link to the downloadable image used in this documentation
.. |link-image| replace::
.. |link-partup-package| replace::
.. |link-boot-tools| replace::
.. _releasenotes:


.. General  substitutions

.. Address value used for ATF_LOAD_ADDR
.. |atfloadaddr| replace::
.. Name of the PHYTEC Kit
.. |kit| replace::
.. Kit RAM size; Example:
   2GiB
.. |kit-ram-size| replace::
.. Name of the PHYTEC Single Board Computer without the SoM; Example:
   phyBOARD-Pollux
.. |sbc| replace::
.. Name of the SoC used on the System on Module
.. |soc| replace::
.. Name of the family of SoCs this SoC is part of; e.g. i.MX 8
.. |socfamily| replace::
.. Name of the PHYTEC System on Module; e.g. phyCORE-|soc|
.. |som| replace::
.. debug uart on the board; Example: ttymxc0
.. |debug-uart| replace::
.. serial uart on the board used for e.g. RS232; Example: ttymxc0
.. |serial-uart| replace::


.. Linux Kernel
.. Name for the SoC as being used in e.g Kernel source files; Example: imx8mp
.. |kernel-socname| replace::
.. Tag name of the final commit used with this release in the Linux Kernel.
.. |kernel-tag| replace::


.. Devicetree

.. name of the devicetree file represnting the carrier board without the file
   ending
.. |dt-carrierboard| replace::
.. name of the devicetree file represnting the som without the file ending
.. |dt-som| replace::


.. Yocto
.. Name PHYTEC uses to identify all BSP Yocto releases for this SoC.
   Example: BSP-Yocto-IMX8MP
.. |yocto-bsp-name| replace::
.. _yocto-bsp-name:
.. Codename of the Yocto release used in this manual;
   Example: kirkstone
.. |yocto-codename| replace::
.. Name of the distribution used in this manual as found in the DISTRO variable
   in Yocto's local.conf
.. |yocto-distro| replace::
.. Name of the image;
   Example: phytec-qt5demo-image
.. |yocto-imagename| replace::
.. Name of the machine as defined in Yocto's "machine" variable;
   Example: phyboard-pollux-imx8mp-3
.. |yocto-machinename| replace::
.. Name of the manifest file used with the Repo tool to build the supported
   release images
.. |yocto-manifestname| replace::
.. Name of the Yocto Reference manual accompanying this BSP release.
.. |yocto-manifestname-y| replace::
.. Name of the existing y manifest of the current development state of
   Yocto BSP.
.. |yocto-ref-manual| replace::
.. _yocto-ref-manual:


.. ref substitutions
   Note that for all labels you have to substitute "sbc-release" with the actual
   product and release this template is used for. E.g. "imx8mm-pd22.1.0". The
   goal is to make this label unique for the whole project.
   Also note that no :ref: role is required here, the document will build
   perfectly fine if you decide to mention the referenced section by name only.

.. Internal link to building the bsp section
.. Descriptor for the bootmode switch
.. |ref-bootswitch| replace:: :ref:`bootmode switch switch <sbc-release-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <sbc-release-building-bsp>`
.. Name of the connector for the debug interface.
.. |ref-debugusbconnector| replace:: :ref:`name <sbc-release-components>`
.. Reference device tree section
.. |ref-dt| replace:: :ref:`device tree <sbc-release-device-tree>`
.. Reference to network section
.. |ref-network| replace:: :ref:`network <sbc-release-network>`
.. Name of the USB OTG connector on the board with an internal link
.. |ref-usb-otg| replace:: :ref:`name-of-connector <sbc-release-components>`


.. The rest of this file is used to assemble the content needed for the BSP
   documentation. This can be a mix of include directives and text. Some content
   may already be present in the project. The best chance of finding content to
   reuse is by checking in the source/bsp/ directory. Content from platform
   specific content may also apply to new documentation but the chance of it
   being compatible is slimmer.

======================
BSP documentation name
======================

.. include:: /bsp/intro.rsti


.. Getting Started

.. include:: /bsp/getting-started.rsti


.. Building BSP

.. _sbc-release-building-bsp:
.. include:: /bsp/building-bsp.rsti

.. _sbc-release-device-tree:
.. include:: /bsp/device-tree.rsti


.. Accessing Peripherals

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/peripherals/leds.rsti

.. include:: /bsp/peripherals/rtc.rsti

USB Host
--------

.. include:: /bsp/peripherals/usb-host.rsti

.. include:: /bsp/peripherals/usb-otg.rsti

.. include:: /bsp/peripherals/pcie.rsti

Audio
-----

.. include:: /bsp/peripherals/audio.rsti

.. include:: /bsp/peripherals/video.rsti

.. include:: /bsp/peripherals/watchdog.rsti


.. BSP Extensions

.. include:: /bsp/bsp-extensions.rsti
