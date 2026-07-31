.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX93-PD26.1.0
.. |dlpage-bsp-link| replace:: |dlpage-bsp|_
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phyflex-imx-91/93-fpsc/#downloads/
.. |dl-server| replace:: BSP downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/
.. |dl-server-link| replace:: |dl-server|_
.. |dl-sdk| replace:: SDK downloads
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/sdk/ampliphy-vendor/
.. |dl-sdk-link| replace:: |dl-sdk|_
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/imx93-phyflex-libra-rdk-1/phytec-qt6demo-image-imx93-phyflex-libra-rdk-1.rootfs.wic.xz
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/imx93-phyflex-libra-rdk-1/phytec-qt6demo-image-imx93-phyflex-libra-rdk-1.rootfs.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/imx93-phyflex-libra-rdk-1/imx-boot-tools/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/imx93-phyflex-libra-rdk-1/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx93
.. _`static-pdf-dl`: ../../../_static/imx91-93-fpsc-head.pdf

.. General Substitutions
.. |kit| replace:: **phyFLEX-i.MX 93 Libra Rapid Development Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: phyFLEX Libra RDK
.. |soc| replace:: i.MX 93
.. |socfamily| replace:: i.MX 9
.. |som| replace:: phyFLEX-|soc| FPSC-Gamma
.. |debug-uart| replace:: ttyLP3
.. |serial-uart| replace:: ttyLP1
.. |bluetooth-uart| replace:: USB
.. |expansion-connector| replace:: X6
.. |netboot-script| replace:: net_boot_fit.scr.uimg
.. |can0-interface| replace:: can0
.. |can-network-file| replace:: 11-can.network

.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-primary-ethernet| replace:: end1
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx93
.. |kernel-tag| replace:: v6.12.34-2.1.0-phy9
.. |emmcdev| replace:: mmcblk0
.. |led-names| replace:: blue:status, green:heartbeat, green:status and red:status
.. |led-example| replace:: red\\:status

.. Bootloader
.. |u-boot-defconfig| replace:: imx93-phyflex_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-multiple-defconfig-note| replace:: In command above replace ``<defconfig>`` with ``imx93-phyflex_defconfig``
.. |u-boot-multiple-dtb-note| replace:: In command above replace ``<dtb>`` with ``imx93-phyflex-libra-rdk.dtb``
.. |u-boot-imx-mkimage-tag| replace:: lf-6.12.34_2.1.0
.. |u-boot-soc-name| replace:: iMX9
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-phytec-imx
.. |u-boot-repo-url| replace:: https://github.com/phytec/u-boot-phytec-imx
.. |emmcdev-uboot| replace:: mmc 0
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX93 specific
.. |u-boot-socname-config| replace:: PHYFLEX_IMX93
.. |u-boot-tag| replace:: v2025.04-2.1.0-phy9

.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM

.. Devicetree
.. |dt-carrierboard| replace:: imx93-phyflex-libra-rdk
.. |dt-som| replace:: imx93-phyflex-fpsc-g-som

.. IMX93 specific
.. |dt-gpio-expander1| replace:: :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L258`
.. |dt-gpio-expander2| replace:: :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L297`
.. |dt-somnetwork| replace:: :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L110`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`walnascar`
.. |yocto-bsp-name| replace:: BSP-Yocto-NXP-i.MX93
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: walnascar
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: imx93-phyflex-libra-rdk-1
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX93-PD26.1.0
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX93-PD26.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (walnascar) <yocto-man-walnascar>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-master-kernel-and-bootloader-conf>`
.. |yocto-sdk-rev| replace::  5.2.2
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx91-93-fpsc-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx91-93-fpsc-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X14) <imx91-93-fpsc-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx91-93-fpsc-head-device-tree>`
.. |ref-supported-hardware| replace:: :ref:`Supported Hardware <imx91-93-fpsc-head-supported-hardware>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx91-93-fpsc-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx91-93-fpsc-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx91-93-fpsc-head-development>`
.. |ref-usb-otg| replace:: :ref:`X18 <imx91-93-fpsc-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx91-93-fpsc-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx91-93-fpsc-head-format-sd>`

.. IMX93 specific
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found here:
   :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L102`.

.. |ref-serial| replace:: :ref:`X27 <imx91-93-fpsc-head-components>`
.. |ref-S5| replace:: :ref:`S5 <imx91-93-fpsc-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx91-93-fpsc-head-ubootexternalenv>`
.. |weston-hdmi-mode| replace:: preferred

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

The table below shows the Compatible BSPs for this manual:

==================== ================ ============= ================ ===========
Compatible BSPs      BSP Release Type Yocto Version BSP Release Date BSP Status

==================== ================ ============= ================ ===========
|yocto-manifestname| Head                           ----/--/--       Development
==================== ================ ============= ================ ===========

.. include:: /bsp/intro.rsti

.. _imx91-93-fpsc-head-supported-hardware:

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

.. _imx91-93-fpsc-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx91-93-fpsc-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

   .. image:: /bsp/images/dipswitch-tristate-4-mmpp.svg
      :scale: 400%

*  Insert the SD card
*  Connect the target and the host with **USB-C** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx91-93-fpsc-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **imx-boot-tools/bl31-imx93.bin**: ARM Trusted Firmware binary
*  **imx-boot-tools/lpddr4_dmem_1d_v202201.bin,
   imx-boot-tools/lpddr4_dmem_2d_v202201.bin,
   imx-boot-tools/lpddr4_imem_1d_v202201.bin,
   imx-boot-tools/lpddr4_imem_2d_v202201.bin**: DDR PHY firmware images
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which is
   bootable.
*  **fitImage**: Linux kernel FIT image
*  **fitImage-its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx93-phyflex-libra-rdk.dtb**: Kernel device tree file
*  **imx93-phyflex-libra-rdk-\*.dtbo**: Kernel device tree overlay files
*  **phytec-\*.tar.gz**: Root file system,
   of bitbake-image that was built.

   * **phytec-qt6demo-image-imx93-phyflex-libra-rdk-1.rootfs.tar.gz**: when bitbake-build
     was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-imx93-phyflex-libra-rdk-1.rootfs.tar.gz**: when bitbake-build
     was processed for ``phytec-headless-image``
*  **phytec-\*.rootfs.wic.xz**: Compressed bootable SD
   card image of bitbake-image that was built. Includes bootloader, DTBs, Kernel
   and Root file system.

   * **phytec-qt6demo-image-imx93-phyflex-libra-rdk-1.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-imx93-phyflex-libra-rdk-1.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-headless-image``

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

.. tip::

   Hardware revision baseboard: 1618.1

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx91-93-fpsc-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/imx-common/installing-os.rsti
   :end-before: .. flash-spi-nor-flash-marker

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx91-93-fpsc-head-development:

Development
===========

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti

.. warning::
   Using the SDK on older host distributions (e.g., Ubuntu 20.04 LTS) with Scarthgap NXP-based BSPs
   can cause issues when building U-Boot or Linux kernel tools for host use. If you encounter an
   "undefined reference" error, a workaround is to prepend the host's binutils to the PATH.

   .. code-block:: console

      host$ export PATH=/usr/bin:$PATH

   Run this after sourcing the SDK *environment-setup* file.

   Note, SDK issue has not been observed on newer distributions, such as Ubuntu 22.04, which appear to work
   without requiring any modifications.

.. _imx91-93-fpsc-head-development-build-uboot:
.. include:: /bsp/imx-common/development/standalone_build_u-boot_imxmkimage.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: /bsp/imx-common/development/uuu.rsti
   :end-before: .. uuu-flash-spinor-marker

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. _imx91-93-fpsc-head-format-sd:

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

           rauc {
                   compatible = "u-boot,distro-rauc";
           };

           script {
                   compatible = "u-boot,script";
           };
   };

The filename-prefixes property describes the paths that will be searched for
the bootscripts. In this case this is the root of the partition as well as the
boot folder. The bootdev-order property sets the default value for the
boot_targets variable. The supported bootmeths will also be named. In this case
the rauc and script bootmethods are supported.

.. include:: /bsp/development/fitImages.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx91-93-fpsc-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   imx93-phyflex-libra-rdk-lvds-ph128800t006-zhc01.dtbo
   imx93-phyflex-libra-rdk-peb-av-10.dtbo
   imx93-phyflex-libra-rdk-peb-av-12-ph128800t006-zhc01.dtbo
   imx93-phyflex-libra-rdk-vm016.dtbo
   imx93-phyflex-libra-rdk-vm020.dtbo

.. _imx91-93-fpsc-head-ubootexternalenv:
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti
   :end-before: .. extension-support-marker
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti
   :start-after: .. change-u-boot-env-in-linux-marker

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the lpuart1 device in
|dt-som|.dtsi:

.. code-block::

   pinctrl_uart1: uart1grp {
           fsl,pins = <
                   MX93_PAD_UART1_RXD__LPUART1_RX		0x31e
                   MX93_PAD_UART1_TXD__LPUART1_TX		0x37e
           >;
   };

The first part of the string MX93_PAD_UART1_RXD__LPUART1_RX names the pad
(in this example UART1_RX). The second part of the string (LPUART1_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal pull resistors are
enabled.

The device tree representation for UART1 pinmuxing:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L577`

.. _imx91-93-fpsc-head-network:

Ethernet
--------

|sbc|-|soc| provides two ethernet interfaces. A gigabit Ethernet is provided by our
module and board.

.. include:: /bsp/peripherals/network.rsti

WLAN/Bluetooth
--------------

WLAN and Bluetooth connectivity on the |sbc| is provided through a USB-based wireless modules.

.. include:: /bsp/peripherals/wireless-network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L399`
and
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L497`

DT configuration for the e.MMC interface can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L386`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: gpios.rsti

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L320`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C bus configuration from SoM (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L163`

General I²C bus configuration from carrierboard (e.g. |dt-carrierboard|.dts)
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L255`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L291`

And the addions on the carrierboard:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L384`

CAN FD
------

The |sbc| has two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon the Linux network layer. Using
this framework, the CAN interfaces behave like an ordinary Linux network device,
with some additional features special to CAN. More information can be found in
the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: /bsp/peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L431`

RS232/RS485
-----------

.. include:: /bsp/peripherals/rs232.rsti

.. include:: /bsp/peripherals/rs485.rsti
.. include:: /bsp/peripherals/rs485-halfduplex.rsti

EEPROM
------

The system features three I2C EEPROM devices distributed across the SoM and
carrier board:

On the |som| SoM:

*  SoM Detection EEPROM (write-protected)

   *  Bus: I2C-1
   *  Address: 0x50
   *  Purpose: Factory configuration for SoM identification

*  User EEPROM

   *  Bus: I2C-1
   *  Address: 0x51
   *  Purpose: Available for user applications

Device Tree Reference for SoM EEPROMs:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L275`

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
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#L276`

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
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-libra-rdk.dts#490`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

.. include:: /bsp/peripherals/tm.rsti

.. include:: /bsp/peripherals/tpm.rsti

.. include:: /bsp/peripherals/watchdog.rsti
