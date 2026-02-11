.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX95-ALPHA1
.. |dlpage-bsp-link| replace:: |dlpage-bsp|_
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phyflex-imx-95-fpsc/
.. |dl-server| replace:: BSP downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/
.. |dl-server-link| replace:: |dl-server|_
.. |dl-sdk| replace:: SDK downloads
.. _dl-sdk: none
.. |dl-sdk-link| replace:: |dl-sdk|_
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/phytec-qt6demo-image-imx95-libra-fpsc-1.rootfs.wic.xz
.. |link-partup-package| replace:: none
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/imx-boot-tools/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX95/BSP-Yocto-NXP-i.MX95-ALPHA1/images/ampliphy-vendor/imx95-libra-fpsc-1/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx95
.. _`static-pdf-dl`: ../../../_static/imx95-fpsc-head.pdf

.. General Substitutions
.. |doc-id| replace:: Head
.. |kit| replace:: **phyFLEX-i.MX 95 Libra Rapid Development Kit**
.. |kit-ram-size| replace:: 8GiB
.. |sbc| replace:: phyFLEX Libra RDK
.. |soc| replace:: i.MX 95
.. |socfamily| replace:: i.MX 9
.. |som| replace:: phyFLEX-|soc| FPSC
.. |debug-uart| replace:: ttyLP6
.. |serial-uart| replace:: ttyLP7
.. |bluetooth-uart| replace:: UART3
.. |expansion-connector| replace:: X56
.. |netboot-script| replace:: net_boot_fit.scr.uimg
.. |can0-interface| replace:: fcan1
.. |can-network-file| replace:: 11-fcan.network

.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-primary-ethernet| replace:: end1
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx95
.. |kernel-tag| replace:: v6.6.52-2.2.0-phy13
.. |emmcdev| replace:: mmcblk0

.. Bootloader
.. |u-boot-defconfig| replace:: imx95-phyflex-libra-rdk_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-phytec-imx
.. |u-boot-repo-url| replace:: https://github.com/phytec/u-boot-phytec-imx
.. |emmcdev-uboot| replace:: mmc 0
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX95 specific
.. |u-boot-socname-config| replace:: IMX95_PHYFLEX_LIBRA_RDK
.. |u-boot-tag| replace:: v2024.04_2.0.0-phy14

.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM

.. Devicetree
.. |dt-carrierboard| replace:: imx95-phyflex-libra-rdk
.. |dt-som| replace:: imx95-phyflex-fpsc-g-som
.. |dtbo-peb-av-10| replace:: imx95-phyflex-libra-rdk-peb-av-10-ph128800t006-zhc01.dtbo

.. IMX95 specific
.. |dt-somnetwork| replace:: :linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L229`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`walnascar`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX95
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: walnascar
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: imx95-phyflex-libra-2
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX95-ALPHA1
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX95-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX95-PD26.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (walnascar) <yocto-man-walnascar>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-walnascar-kernel-and-bootloader-conf>`
.. |yocto-sdk-rev| replace::  5.0.x
.. |yocto-sdk-a-core| replace:: cortexa55-crypto

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx95-fpsc-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx95-fpsc-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X14) <imx95-fpsc-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx95-fpsc-head-device-tree>`
.. |ref-supported-hardware| replace:: :ref:`Supported Hardware <imx95-fpsc-head-supported-hardware>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx95-fpsc-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx95-fpsc-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx95-fpsc-head-development>`
.. |ref-usb-otg| replace:: :ref:`X18 (upper connector) <imx95-fpsc-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx95-fpsc-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx95-fpsc-head-format-sd>`

.. IMX95 specific
.. |gpu-model| replace:: MALI G310
.. |sbc-network| replace::
   The device tree set up for the ethernet where the PHY is populated on the |sbc|
   can be found here:
   :linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts#L109`.

.. |ref-serial| replace:: :ref:`X27 <imx95-fpsc-head-components>`
.. |ref-S5| replace:: :ref:`S5 <imx95-fpsc-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx95-fpsc-head-ubootexternalenv>`

.. |jtag-target-interface| replace:: S
.. |jtag-soc-doc-link| replace:: https://kb.segger.com/NXP_i.MX_95

.. _imx95-fpsc-head-bsp-manual:

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-----------------------+----------------------+
| |doc-id| |soc| BSP    |                      |
| Manual Head           |                      |
+-----------------------+----------------------+
| Document Title        | |doc-id| |soc| BSP   |
|                       | Manual Head          |
+-----------------------+----------------------+
| Document Type         | BSP Manual           |
+-----------------------+----------------------+
| Article Number        | |doc-id|             |
+-----------------------+----------------------+
| Yocto Manual          | Walnascar            |
+-----------------------+----------------------+
| Release Date          | XXXX/XX/XX           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| BSP   |
|                       | Manual Head          |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

============================== ================ ================= ==============
Compatible BSPs                BSP Release Type BSP Release  Date BSP Status

============================== ================ ================= ==============
BSP-Yocto-NXP-i.MX95-ALPHA2    ALPHA            q1 2026           in development
============================== ================ ================= ==============

.. include:: /bsp/intro.rsti

.. _imx95-fpsc-head-supported-hardware:

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

.. _imx95-fpsc-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the
   following position:

   .. image:: /bsp/images/dipswitch-tristate-4-mmpm.svg
      :scale: 400%

*  Insert the SD card
*  Connect the target and the host with **USB-C** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx95-fpsc-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx95.bin**: ARM Trusted Firmware binary
*  **lpddr5_dmem_qb_v202409.bin,
   lpddr5_dmem_v202409.bin,
   lpddr5_imem_qb_v202409.bin,
   lpddr5_imem_v202409.bin**: DDR PHY firmware images
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
*  **imx95-phyflex-libra-rdk*.dtb**: Kernel device tree file
*  **imx95-phyflex-fpsc\*.dtbo,
   imx95-phyflex-libra-rdk\*.dtbo**: Kernel device tree overlay files
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

.. _imx95-fpsc-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/imx-common/installing-os.rsti
   :end-before: .. flash-emmc-from-usb-stick-in-uboot-marker

.. include:: /bsp/imx-common/installing-os.rsti
   :start-after: .. flash-emmc-from-sdcard-marker
   :end-before: .. flash-spi-nor-flash-marker

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-head-development:

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

.. _imx95-fpsc-head-development-build-uboot:
.. include:: development/standalone_build_u-boot_imxmkimage.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: /bsp/imx-common/development/uuu.rsti
   :end-before: .. uuu-flash-emmc-marker

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti
.. include:: /bsp/development/pxe_boot.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. _imx95-fpsc-head-format-sd:

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. include:: /bsp/development/ampliphy-boot.rsti
   :end-before: .. ampliphy-boot-supported-bootscripts-marker

.. code-block::

   mmc_boot_fit
   net_boot_fit

.. include:: /bsp/development/ampliphy-boot.rsti
   :start-after: .. ampliphy-boot-supported-bootscripts-marker

For the |kit|, the default values are defined in the U-Boot devicetree
(e.g. arch/arm/dts/|dt-carrierboard|-u-boot.dtsi):

.. code-block::

   bootstd {
           bootph-verify;
           compatible = "u-boot,boot-std";

           filename-prefixes = "/", "/boot/";
           bootdev-order = "mmc0", "mmc1", "ethernet";

           script {
                   compatible = "u-boot,script";
           };
   };

The filename-prefixes property describes the paths that will be searched for
the bootscripts. In this case this is the root of the partition as well as the
boot folder. The bootdev-order property sets the default value for the
boot_targets variable. The supported bootmeths will also be named. In this case
only the script method is supported.

.. include:: /bsp/development/fitImages.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx95-fpsc-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   imx95-phyflex-libra-rdk-bluetooth-88w8987.dtbo
   imx95-phyflex-libra-rdk-lvds-ph128800t006-zhc01.dtbo
   imx95-phyflex-libra-rdk-neoisp.dtbo
   imx95-phyflex-libra-rdk-vm016-csi1.dtbo
   imx95-phyflex-libra-rdk-vm016-fpdlink-port0-csi1.dtbo
   imx95-phyflex-libra-rdk-vm016-fpdlink-port1-csi1.dtbo
   imx95-phyflex-libra-rdk-vm016-csi2.dtbo
   imx95-phyflex-libra-rdk-vm016-fpdlink-port0-csi2.dtbo
   imx95-phyflex-libra-rdk-vm016-fpdlink-port1-csi2.dtbo
   imx95-phyflex-libra-rdk-vm017-csi1.dtbo
   imx95-phyflex-libra-rdk-vm017-fpdlink-port0-csi1.dtbo
   imx95-phyflex-libra-rdk-vm017-fpdlink-port1-csi1.dtbo
   imx95-phyflex-libra-rdk-vm017-csi2.dtbo
   imx95-phyflex-libra-rdk-vm017-fpdlink-port0-csi2.dtbo
   imx95-phyflex-libra-rdk-vm017-fpdlink-port1-csi2.dtbo
   imx95-phyflex-libra-rdk-vm020-csi1.dtbo
   imx95-phyflex-libra-rdk-vm020-fpdlink-port0-csi1.dtbo
   imx95-phyflex-libra-rdk-vm020-fpdlink-port1-csi1.dtbo
   imx95-phyflex-libra-rdk-vm020-csi2.dtbo
   imx95-phyflex-libra-rdk-vm020-fpdlink-port0-csi2.dtbo
   imx95-phyflex-libra-rdk-vm020-fpdlink-port1-csi2.dtbo
   imx95-phyflex-fpsc-g-som-temperature.dtbo

.. _imx95-fpsc-head-ubootexternalenv:
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti

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

.. _imx95-fpsc-head-network:

Ethernet
--------

|sbc|-|soc| provides three ethernet interfaces. A gigabit Ethernet is provided
by our module and board. Additionally there is a 10Gbit Ethernet. Currently
only the one Gigabit Ethernet ports are supported (Ethernet1 and Ethernet2).

.. include:: /bsp/peripherals/network.rsti

.. include:: wireless-network.rsti

.. include:: ../../peripherals/wireless-network.rsti

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

CAN FD
------

The |sbc| has two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon the Linux network layer. Using
this framework, the CAN interfaces behave like an ordinary Linux network device,
with some additional features special to CAN. More information can be found in
the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy6/arch/arm64/boot/dts/freescale/imx95-phyflex-libra-rdk.dts#L200`

EEPROM
------

The system features three I2C EEPROM devices distributed across the SoM and
carrier board:

On the |som| SoM:

*  SoM Detection EEPROM (write-protected)

   *  Bus: I2C-5
   *  Address: 0x51
   *  Purpose: Factory configuration for SoM identification

*  User EEPROM

   *  Bus: I2C-5
   *  Address: 0x50
   *  Purpose: Available for user applications

Device Tree Reference for SoM EEPROMs:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy13/arch/arm64/boot/dts/freescale/imx95-phycore-fpsc.dtsi#L125`

And on the |sbc| carrier board:

*  Board Detection EEPROM

   *  Bus: I2C-2
   *  Address: 0x51
   *  Purpose: Reserved for carrier board identification

*  User EEPROM

   *  Bus: I2C-2
   *  Address: 0x52
   *  Purpose: Available for user applications

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

.. include:: /bsp/peripherals/pwm-fan.rsti

.. include:: /bsp/peripherals/tpm.rsti

.. include:: /bsp/peripherals/gpu.rsti
   :end-before: .. gpu-platform-specific-marker

.. include:: peripherals/gpu.rsti

.. include:: /bsp/peripherals/gpu.rsti
   :start-after: .. gpu-platform-specific-marker

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: /bsp/peripherals/jtag.rsti
   :end-before: .. jtag-basic-functions-marker

.. warning::

   There are some limitations:

   -  Connecting to A55 core only works in U-Boot not in Linux
   -  Booting Linux will fail when J-Link is connected
   -  J-Link needs to be reconnected after board reset
   -  Connecting to M7 core does not work, as there is currently not running any
      application on it
   -  Need to use SWD target protocol for connecting (at least for M33 core).
      This is also used in |soc| example from Segger website.

.. include:: /bsp/peripherals/jtag.rsti
   :start-after: .. jtag-basic-functions-marker

.. warning::

   There are some limitations:

   -  According to Segger |soc| documentation, reset command does not actually
      trigger a core reset.
   -  Writing to memory does not work from M33 core.

.. +---------------------------------------------------------------------------+
.. | NXP Demos                                                                 |
.. +---------------------------------------------------------------------------+

.. include:: ../../imx-common/GoPoint/introduction.rsti

.. include:: ../../imx-common/GoPoint/ML_Benchmark.rsti
