.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX95-ALPHA1
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-95-fpsc/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/
.. _dl-sdk: none
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/phytec-qt6demo-image-imx95-libra-fpsc-1.rootfs.wic.xz
.. |link-partup-package| replace:: none
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/imx-boot-tools/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx95
.. _`static-pdf-dl`: ../../../_static/imx95-fpsc-alpha1.pdf


.. General Substitutions
.. |doc-id| replace:: ALPHA1
.. |kit| replace:: **phyCORE-i.MX 95 FPSC Kit**
.. |kit-ram-size| replace:: 8GiB
.. |sbc| replace:: Libra FPSC
.. |soc| replace:: i.MX 95
.. |socfamily| replace:: i.MX 9
.. |som| replace:: phyCORE-|soc| FPSC
.. |debug-uart| replace:: ttyLP6
.. |serial-uart| replace:: ttyLP7
.. |bluetooth-uart| replace:: UART3
.. |expansion-connector| replace:: X56


.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx95
.. |kernel-tag| replace:: v6.6.52-2.2.0-phy13
.. |emmcdev| replace:: mmcblk0

.. Bootloader
.. |u-boot-defconfig| replace:: imx95-libra-fpsc_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://git.phytec.de/u-boot-phytec-imx
.. |emmcdev-uboot| replace:: mmc 0
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX95 specific
.. |u-boot-socname-config| replace:: IMX95_LIBRA_FPSC
.. |u-boot-tag| replace:: v2024.04_2.0.0-phy14


.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM


.. Devicetree
.. |dt-carrierboard| replace:: imx95-libra-rdk-fpsc
.. |dt-som| replace:: imx95-phycore-fpsc
.. |dtbo-peb-av-10| replace:: imx95-libra-rdk-fpsc-lvds-ph128800t006-zhc01.dtbo

.. IMX95 specific
.. |dt-somnetwork| replace:: :linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L229`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`scarthgap`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX95
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: scarthgap
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: imx95-libra-fpsc-1
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX95-ALPHA1
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX95-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX95-PD25.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (scarthgap) <yocto-man-scarthgap>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-scarthgap-kernel-and-bootloader-conf>`
.. |yocto-sdk-rev| replace::  5.0.x
.. |yocto-sdk-a-core| replace:: cortexa55-crypto

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx95-fpsc-alpha1-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx95-fpsc-alpha1-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X14) <imx95-fpsc-alpha1-components>`
.. |ref-dt| replace:: :ref:`device tree <imx95-fpsc-alpha1-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx95-fpsc-alpha1-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx95-fpsc-alpha1-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx95-fpsc-alpha1-development>`
.. |ref-usb-otg| replace:: :ref:`X18 (upper connector) <imx95-fpsc-alpha1-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx95-fpsc-alpha1-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx95-fpsc-alpha1-format-sd>`


.. IMX95 specific
.. |sbc-network| replace::
   The device tree set up for the ethernet where the PHY is populated on the |sbc|
   can be found here:
   :linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L109`.

.. |ref-serial| replace:: :ref:`X27 <imx95-fpsc-alpha1-components>`
.. |ref-S5| replace:: :ref:`S5 <imx95-fpsc-alpha1-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx95-fpsc-alpha1-ubootexternalenv>`

.. _imx95-fpsc-alpha1-bsp-manual:

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-----------------------+----------------------+
| |doc-id| |soc| BSP    |                      |
| Manual                |                      |
+-----------------------+----------------------+
| Document Title        | |doc-id| |soc| BSP   |
|                       | Manual               |
+-----------------------+----------------------+
| Document Type         | BSP Manual           |
+-----------------------+----------------------+
| Article Number        | |doc-id|             |
+-----------------------+----------------------+
| Yocto Manual          | Scarthgap            |
+-----------------------+----------------------+
| Release Date          | 2025/06/02           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| BSP   |
|                       | Manual               |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

============================== ================ ================= ==============
Compatible BSPs                BSP Release Type BSP Release  Date BSP Status

============================== ================ ================= ==============
BSP-Yocto-NXP-i.MX95-ALPHA1    Alpha            2025/06/02        Released
============================== ================ ================= ==============


.. include:: /bsp/intro.rsti

Supported Hardware
------------------

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname| `download <dlpage-bsp_>`_.

If you choose a specific **Machine Name** in the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware

.. _imx95-fpsc-alpha1-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-alpha1-getting-started:
.. include:: getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the
   following position:

.. image:: images/SD_Card_Boot.png

*  Insert the SD card
*  Connect the target and the host with **USB-C** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx95-fpsc-alpha1-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx95.bin**: ARM Trusted Firmware binary
*  **lpddr5_dmem_qb_v202311.bin,
   lpddr5_dmem_v202311.bin,
   lpddr5_imem_qb_v202311.bin,
   lpddr5_imem_v202311.bin**: DDR PHY firmware images
*  **oei-m33-ddr.bin,
   oei-m33-tcm.bin**: OEI images
*  **m33_image-mx95libra.bin**: System Manager image
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which
   is bootable.
*  **fitImage**: Linux kernel FIT image
*  **fitImage-its\*.its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx95-libra-rdk-fpsc*.dtb**: Kernel device tree file
*  **imx95-phycore-fpsc\*.dtbo,
   imx95-libra-rdk-fpsc\*.dtbo**: Kernel device tree overlay files
*  **phytec-qt6demo-image\*.tar.gz**: Root file system
*  **phytec-qt6demo-image\*.rootfs.wic.xz**: compressed SD card image

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx95-fpsc-alpha1-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/imx-common/installing-os.rsti
   :end-before: .. flash-emmc-from-usb-stick-in-uboot-marker

.. include:: /bsp/imx-common/installing-os.rsti
   :start-after: .. flash-emmc-from-sdcard-marker
   :end-before: .. flash-emmc-from-sdcard-in-linux-marker

.. note::
   There is no partup support in imx95 ALPHA1 release yet.

.. include:: /bsp/imx-common/installing-os.rsti
   :start-after: .. flash-emmc-from-sdcard-in-linux-marker
   :end-before: .. flash-spi-nor-flash-marker

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-alpha1-development:

Development
===========

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti
   :end-before: .. get-sdk-marker

Build the SDK
.............

You can build the SDK yourself with Yocto:

*  Move to the Yocto build directory:

   .. code-block:: console
      :substitutions:

      host:~$ source sources/poky/oe-init-build-env
      host:~$ bitbake -c populate_sdk |yocto-imagename| # or another image

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti
   :start-after: .. install-sdk-marker

.. _imx95-fpsc-alpha1-development-build-uboot:
.. include:: development/standalone_build_u-boot_imxmkimage.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: /bsp/imx-common/development/uuu.rsti
   :end-before: .. uuu-flash-emmc-marker

.. include:: /bsp/imx-common/development/host_network_setup.rsti

.. warning::

   Using netboot with standardboot and static IPs does not work yet in this
   release. Standardboot will always use dhcp.

.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. _imx95-fpsc-alpha1-format-sd:

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-alpha1-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   |dtbo-peb-av-10|
   imx95-libra-rdk-fpsc-lvds-etml1010g3dra.dtbo


.. _imx95-fpsc-alpha1-ubootexternalenv:
.. include:: /bsp/dt-overlays.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the lpuart7 device in
|dt-som|.dtsi:

.. code-block::

   pinctrl_lpuart7: lpuart7grp {
           fsl,pins = <
                   IMX95_PAD_GPIO_IO37__LPUART7_RX	0x31e	/* UART3_RXD */
                   IMX95_PAD_GPIO_IO36__LPUART7_TX	0x31e	/* UART3_TXD */
           >;
   };

The first part of the string IMX95_PAD_GPIO_IO37__LPUART7_RX names the pad
(in this example IMX95_PAD_GPIO_IO37). The second part of the string
(LPUART7_RX) is the desired muxing option for this pad. The pad setting value
(hex value on the right) defines different modes of the pad, for example, if
internal pull resistors are activated or not. In this case, the internal
resistors are enabled.

The device tree representation for UART1 pinmuxing:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L438`

.. _imx95-fpsc-alpha1-network:

Network
-------

|sbc|-|soc| provides three ethernet interfaces. A gigabit Ethernet is provided
by our module and board. Additionally there is a 10Gbit Ethernet. Currently
only the one Gigabit Ethernet ports are supported (ETH0 and ETH1).

.. include:: /bsp/imx-common/peripherals/network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L632`

DT configuration for the eMMC interface can be found here:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L619`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/imx-common/peripherals/gpios.rsti

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C bus configuration from SoM (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L117`

General I²C bus configuration from carrierboard (e.g. |dt-carrierboard|.dts)
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L166`

EEPROM
------

The system features three I2C EEPROM devices distributed across the SoM and
carrier board:

On the |som| SoM:

*  Board Detection EEPROM (write-protected)
   *  Bus: I2C-0
   *  Address: 0x51
   *  Purpose: Factory configuration for board identification

*  User EEPROM
   *  Bus: I2C-0
   *  Address: 0x50
   *  Purpose: Available for user applications

Device Tree Reference for SoM EEPROMs:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L125`

And on the |sbc| carrier board:

*  Board Detection EEPROM
   *  Bus: I2C-4
   *  Address: 0x51
   *  Purpose: Reserved for carrier board identification

Device Tree Reference for Carrier Board:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L231`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L139`

And the addions on the carrierboard:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L292`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed of up to 4 Gbit/s (SuperSpeed
'SS'). The USB subsystem has two independent USB controller cores. Both cores
are capable of acting as a USB peripheral device or a USB host. Each is
connected to a USB 3.0 PHY.

.. include:: /bsp/peripherals/usb-host.rsti

DT representation for USB Host:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L383`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

Device tree description of LVDS-0 can be found here:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc-lvds.dtsi#L35`

.. include:: /bsp/imx8/peripherals/pm.rsti

.. include:: peripherals/tm.rsti

.. include:: peripherals/gpu.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. +---------------------------------------------------------------------------+
.. | NXP Demos                                                                 |
.. +---------------------------------------------------------------------------+

.. include:: ../../imx-common/GoPoint/introduction.rsti

.. include:: ../../imx-common/GoPoint/ML_Benchmark.rsti
