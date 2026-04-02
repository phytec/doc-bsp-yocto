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

.. IMX93 specific

.. General Substitutions
.. |doc-id| replace:: Head
.. |kit| replace:: **phyFLEX-i.MX 93 Libra Rapid Development Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: Libra Rapid Development Kit
.. |soc| replace:: phyFLEX-i.MX 93 FPSC-Gamma
.. |socfamily| replace:: i.MX 93
.. |som| replace:: phyCORE-|soc| FPSC
.. |debug-uart| replace:: ttyLP3
.. |serial-uart| replace:: ttyLP2
.. TODO bluetooth works over USB
.. |bluetooth-uart| replace:: UART3
.. |expansion-connector| replace:: X6
.. TODO do we support netboot? Maybe remove for 1st shot.
.. |netboot-script| replace:: net_boot_fit.scr.uimg

.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-primary-ethernet| replace:: end1
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx93
.. |kernel-tag| replace:: v6.12.34-2.1.0-phyX
.. |emmcdev| replace:: mmcblk0
.. |led-names| replace:: red:user1, green:user2 and blue:user3
.. |led-example| replace:: red\\:user1

.. Bootloader
.. |u-boot-defconfig| replace:: imx93-phyflex_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0

.. |u-boot-multiple-defconfig-note| replace:: In command above replace ``<defconfig>`` with ``imx93-phyflex_defconfig``
.. |u-boot-multiple-dtb-note| replace:: In command above replace ``<dtb>`` with ``imx93-phyflex-libra-rdk.dtb``
.. |u-boot-soc-name| replace:: iMX9


.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-phytec-imx
.. |u-boot-repo-url| replace:: https://github.com/phytec/u-boot-phytec-imx
.. |emmcdev-uboot| replace:: mmc 0
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX93 specific
.. |u-boot-socname-config| replace:: PHYCORE_IMX93
.. |u-boot-tag| replace:: v2025.04-2.1.0-phyX

.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM

.. Devicetree
.. |dt-carrierboard| replace:: imx93-phyflex-libra-rdk
.. |dt-som| replace:: imx93-phyflex-fpsc-g-som

.. TODO
.. IMX93 specific
.. |dt-somnetwork| replace:: :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L110`
.. |dt-gpio-expander| replace:: :linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L192`

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
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (walnascar) <yocto-man-master>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-master-kernel-and-bootloader-conf>`
.. TODO
.. |yocto-sdk-rev| replace::  5.2.x
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. TODO
.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx8mp-fpsc-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mp-fpsc-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X14) <imx8mp-fpsc-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mp-fpsc-head-device-tree>`
.. |ref-supported-hardware| replace:: :ref:`Supported Hardware <imx8mp-fpsc-head-supported-hardware>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mp-fpsc-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mp-fpsc-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mp-fpsc-head-development>`
.. |ref-usb-otg| replace:: :ref:`X18 <imx8mp-fpsc-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx8mp-fpsc-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx8mp-fpsc-head-format-sd>`

.. TODO
.. IMX8(MP) specific
.. |gpu-model| replace:: Vivante GC7000UL
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found here:
   :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyflex-fpsc-g-som.dtsi#L102`.

.. TODO
.. |ref-serial| replace:: :ref:`X27 <imx8mp-fpsc-head-components>`
.. |ref-S5| replace:: :ref:`S5 <imx8mp-fpsc-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mp-fpsc-head-ubootexternalenv>`
.. |weston-hdmi-mode| replace:: preferred

.. TODO
.. M-Core specific
.. |mcore| replace:: M7 Core
.. |mcore-zephyr-docs| replace:: https://docs.zephyrproject.org/latest/boards/phytec/mimx8mp_phyboard_pollux/doc/index.html
.. |mcore-jtag-dev| replace:: MIMX8ML8_M7
.. |mcore-sdk-version| replace:: 2.13.0

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-----------------------+----------------------+
| |doc-id| |soc| FPSC   |                      |
| BSP Manual Head       |                      |
+-----------------------+----------------------+
| Document Title        | |doc-id| |soc| FPSC  |
|                       | BSP Manual Head      |
+-----------------------+----------------------+
| Document Type         | BSP Manual           |
+-----------------------+----------------------+
| Article Number        | |doc-id|             |
+-----------------------+----------------------+
| Yocto Manual          | walnascar            |
+-----------------------+----------------------+
| Release Date          | 2026/03/13           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| FPSC  |
|                       | BSP Manual Head      |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

============================== ================ ================= ==============
Compatible BSPs                BSP Release Type BSP Release  Date BSP Status

============================== ================ ================= ==============
BSP-Yocto-NXP-i.MX93-PD26.1.0  Major            2026/03/13        Released
============================== ================ ================= ==============

.. include:: /bsp/intro.rsti

.. _imx8mp-fpsc-head-supported-hardware:

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

.. _imx8mp-fpsc-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mp-fpsc-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

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

.. _imx8mp-fpsc-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx93i.bin**: ARM Trusted Firmware binary
* **lpddr4_dmem_1d_v202201.bin, lpddr4_dmem_2d_v202201.bin,
   lpddr4_imem_1d_v202201.bin,
   lpddr4_imem_2d_v202201.bin**: DDR PHY firmware images
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which is
   bootable.
*  **fitImage**: Linux kernel FIT image
*  **fitImage-its\*.its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx93-phyboard-*.dtb** or **imx91-phyboard-*.dtb**: Kernel device tree file
*  **imx93-phy\*.dtbo** or **imx91-phy\*.dtbo**: Kernel device tree overlay files
*  **phytec-\*.tar.gz**: Root file system,
   of bitbake-image that was built.

   * **phytec-qt6demo-image-phyboard-*-imx9*-*.tar.gz**: when bitbake-build
     was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-phyboard-*-imx9*-*.tar.gz**: when bitbake-build
     was processed for ``phytec-headless-image``
*  **phytec-\*.rootfs.wic.xz**: Compressed bootable SD
   card image of bitbake-image that was built. Includes bootloader, DTBs, Kernel
   and Root file system.

   * **phytec-qt6demo-image-phyboard-*-imx9*-*.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-phyboard-*-imx9*-*.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-headless-image``

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

.. tip::

   Hardware revision baseboard: 1618.2

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx8mp-fpsc-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mp-fpsc-head-development:

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

.. _imx8mp-fpsc-head-development-build-uboot:
.. include:: /bsp//imx-common/development/standalone_build_u-boot_imxmkimage.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: /bsp/imx-common/development/uuu.rsti
   :end-before: .. uuu-flash-spinor-marker

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. _imx8mp-fpsc-head-format-sd:

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
the efi, rauc and script bootmethods are supported.

.. include:: /bsp/development/fitImages.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mp-fpsc-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   imx93-phyflex-libra-rdk-lvds-ph128800t006-zhc01.dtbo
   imx93-phyflex-libra-rdk-peb-av-10.dtbo
   imx93-phyflex-libra-rdk-peb-av-12-ph128800t006-zhc01.dtbo
   imx93-phyflex-libra-rdk-vm016.dtbo
   imx93-phyflex-libra-rdk-vm020.dtbo

.. _imx8mp-fpsc-head-ubootexternalenv:
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART1 device in
|dt-som|.dtsi:

.. code-block::

   pinctrl_uart1: uart1grp {
           fsl,pins = <
                   MX93_PAD_UART1_RXD__LPUART1_RX     0x31e
                   MX93_PAD_UART1_TXD__LPUART1_TX     0x30e
           >;
   };

The first part of the string MX93_PAD_UART1_RXD__LPUART1_RX names the pad
(in this example UART1_RXD). The second part of the string (LPUART1_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal pull up is
activated.

The device tree representation for UART1 pinmuxing:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-phycore-fpsc.dtsi#L714`

Ethernet
--------

|sbc|-|soc| provides two ethernet interfaces. A gigabit Ethernet is provided by our
module and board.

.. include:: /bsp/peripherals/network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-phycore-fpsc.dtsi#L401`
and
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L318`

DT configuration for the e.MMC interface can be found here:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-phycore-fpsc.dtsi#L412`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L165`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C bus configuration from SoM (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-phycore-fpsc.dtsi#L188`

General I²C bus configuration from carrierboard (e.g. |dt-carrierboard|.dts)
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L149`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-phycore-fpsc.dtsi#L293`

And the addions on the carrierboard:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L252`

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
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L295`

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

Device tree description of LVDS-0 can be found here:
:linux-phytec-imx:`tree/v6.12.20-2.0.0-phy1/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L223`

.. include:: /bsp/peripherals/watchdog.rsti
