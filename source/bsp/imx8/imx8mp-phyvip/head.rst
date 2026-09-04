.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MP-PD26.1.1
.. |dlpage-bsp-link| replace:: |dlpage-bsp|_
.. |dlpage-product| replace:: https://www.phytec.eu/en/produkte/embedded-vision/phyvip-vision-integration-platform-imx-8m-plus/#downloads
.. |dl-server| replace:: BSP downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/
.. |dl-server-link| replace:: |dl-server|_
.. |dl-sdk| replace:: SDK downloads
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD26.1.1/sdk/ampliphy-vendor/
.. |dl-sdk-link| replace:: |dl-sdk|_
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD26.1.1/images/ampliphy-vendor/imx8mp-phyflex-phyvip-1/phytec-vision-image-imx8mp-phyflex-phyvip-1.rootfs.wic.xz
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD26.1.1/images/ampliphy-vendor/imx8mp-phyflex-phyvip-1/phytec-vision-image-imx8mp-phyflex-phyvip-1.rootfs.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD26.1.1/images/ampliphy-vendor/imx8mp-phyflex-phyvip-1/imx-boot-tools/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD26.1.1/images/ampliphy-vendor/imx8mp-phyflex-phyvip-1/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mp
.. _`static-pdf-dl`: ../../../_static/imx8mp-phyvip-head.pdf

.. IMX8(MP) specific

.. General Substitutions
.. |kit| replace:: **phyVIP-i.MX 8M Plus Vision Integration Platform**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: phyVIP
.. |soc| replace:: i.MX 8M Plus
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyFLEX-|soc| FPSC Gamma
.. |debug-uart| replace:: ttymxc3
.. |serial-uart| replace:: ttymxc1
.. |bluetooth-uart| replace:: UART2
.. |netboot-script| replace:: net_boot_fit.scr.uimg
.. |can0-interface| replace:: fcan1
.. |can-network-file| replace:: 11-can.network

.. Linux Kernel
.. |kernel-defconfig| replace:: imx8_phytec_defconfig
.. |kernel-primary-ethernet| replace:: end1
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx8mp
.. TODO: check kernel tag
.. |kernel-tag| replace:: v6.12.49-2.2.0-phy14
.. |emmcdev| replace:: mmcblk2

.. Bootloader
.. |u-boot-defconfig| replace:: imx8mp-phyflex-phyvip_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 2
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-phytec-imx
.. |u-boot-repo-url| replace:: https://github.com/phytec/u-boot-phytec-imx
.. |emmcdev-uboot| replace:: mmc 2
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX8(MP) specific
.. |u-boot-socname-config| replace:: IMX8MP_PHYFLEX_LIBRA_RDK
.. TODO: check u-boot tag?
.. |u-boot-tag| replace:: v2025.04-2.2.0-phy10

.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM

.. Devicetree
.. |dt-carrierboard| replace:: imx8mp-phyflex-phyvip
.. |dt-expansionboard| replace:: imx8mp-phyflex-phyvip-peb-b-006
.. |dt-som| replace:: imx8mp-phyflex-fpsc-g-som

.. IMX8(MP) specific
.. |dt-somnetwork| replace:: :linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L94`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`walnascar`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MP
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: Walnascar
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-vision-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: imx8mp-phyflex-phyvip-1
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MP-PD26.1.1
.. TODO: phyVIP not available on master?
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX8MP-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX8MP-PD26.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (walnascar) <yocto-man-master>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-master-kernel-and-bootloader-conf>`
.. TODO: not sure about the SDK version?
.. |yocto-sdk-rev| replace::  5.2.4
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx8mp-phyvip-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mp-phyvip-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X8) <imx8mp-phyvip-head-components>`
.. |ref-boardconnector1| replace:: :ref:`(CON1) <imx8mp-phyvip-head-components>`
.. |ref-boardconnector2| replace:: :ref:`(CON2) <imx8mp-phyvip-head-components>`
.. |ref-bootmodeconnector| replace:: :ref:`(X12) <imx8mp-phyvip-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mp-phyvip-head-device-tree>`
.. |ref-supported-hardware| replace:: :ref:`Supported Hardware <imx8mp-phyvip-head-supported-hardware>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mp-phyvip-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mp-phyvip-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mp-phyvip-head-development>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx8mp-phyvip-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx8mp-phyvip-head-format-sd>`

.. IMX8(MP) specific
.. |gpu-model| replace:: Vivante GC7000UL
.. |sbc-network| replace:: \

.. |ref-serial| replace:: :ref:`X12 <imx8mp-phyvip-head-components>`
.. TODO: ref-S5 not available on phyVIP. Check if could be removed
.. |ref-S5| replace:: :ref:`S5 <imx8mp-phyvip-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mp-phyvip-head-ubootexternalenv>`
.. |weston-hdmi-mode| replace:: preferred

.. M-Core specific
.. |mcore| replace:: M7 Core
.. |mcore-zephyr-docs| replace:: https://docs.zephyrproject.org/latest/boards/phytec/mimx8mp_phyboard_pollux/doc/index.html
.. |mcore-jtag-dev| replace:: MIMX8ML8_M7
.. |mcore-sdk-version| replace:: v2.15.0-phy

.. Powerkey specific
.. |powerkey-driver| replace:: snvs_pwrkey
.. |systemd-logind-conf-path-powerkey| replace:: ``/usr/lib/systemd/logind.conf.d/00-systemd-conf-imx.conf``
.. |powerkey-input-dev| replace:: 30370000.snvs\:snvs-powerkey
.. |powerkey-keycode-property| replace:: linux,keycode

.. _bsp-man-imx8mp-phyvip-head:

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

.. TODO: Check release date?

The table below shows the Compatible BSPs for this manual:

==================== ================ ================ ================ ==============
Compatible BSPs      BSP Release Type Yocto Version    BSP Release Date BSP Status

==================== ================ ================ ================ ==============
|yocto-manifestname| Major            |yocto-codename| 2026/09/XX       Released
==================== ================ ================ ================ ==============

.. include:: /bsp/intro.rsti

.. _imx8mp-phyvip-head-supported-hardware:

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

.. _imx8mp-phyvip-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mp-phyvip-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

   .. image:: /bsp/images/dipswitch-1-1.svg
      :scale: 400%

*  Insert the SD card
*  Connect the target and the host with **USB to TTL serial adapter (1.8V)** on
   |ref-debugusbconnector| debug connector port
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti
   :end-before: .. nxp-eula-marker
*  Open the main configuration file and accept the GPU and VPU binary license
   agreements. Do this by uncommenting the corresponding line, as below.

   .. code-block:: console

      host:~/yocto/build$ vim conf/local.conf
      # Uncomment to accept NXP EULA
      # EULA can be found under ../sources/meta-freescale/EULA
      ACCEPT_FSL_EULA = "1"

.. include:: /bsp/building-bsp.rsti
   :start-after: .. nxp-eula-marker

.. _imx8mp-phyvip-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx8mp.bin**: ARM Trusted Firmware binary
*  **lpddr4_pmu_train_2d_dmem_202006.bin,
   lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which is
   bootable.
*  **fitImage**: Linux kernel FIT image
*  **fitImage-its\*.its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx8mp-phyflex-phyvip*.dtb**: Kernel device tree file
*  **imx8mp-phyflex-phyvip*.dtbo**: Kernel device tree overlay files
*  **phytec-vision-image\*.tar.gz**: Root file system
*  **phytec-vision-image\*.rootfs.wic.xz**: compressed SD card image
*  **\*.scr.uimg**: compiled bootscripts

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

.. tip::

   Hardware revision baseboard: 1645.0

The |sbc| features a boot switch with a single port to select the |som| default
bootsource.

.. _imx8mp-phyvip-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/imx-common/installing-os.rsti
   :end-before: .. flash-spi-nor-flash-marker

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mp-phyvip-head-development:

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

.. _imx8mp-phyvip-head-development-build-uboot:
.. include:: /bsp//imx-common/development/standalone_build_u-boot_binman.rsti
   :end-before: .. build-uboot-fixed-ram-size-marker
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. include:: /bsp/imx-common/development/master_manifest.rsti

.. _imx8mp-phyvip-head-format-sd:

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
           bootdev-order = "mmc2", "mmc1", "ethernet";

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

.. _imx8mp-phyvip-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

	imx8mp-phyflex-phyvip.dtb
	imx8mp-phyflex-phyvip-peb-b-006.dtbo
	imx8mp-phyflex-phyvip-temperature.dtbo
	imx8mp-phyflex-vm016-csi1.dtbo
	imx8mp-phyflex-vm016-csi1-fpdlink-port0.dtbo
	imx8mp-phyflex-vm016-csi1-fpdlink-port1.dtbo
	imx8mp-phyflex-vm016-csi2.dtbo
	imx8mp-phyflex-vm016-csi2-fpdlink-port0.dtbo
	imx8mp-phyflex-vm016-csi2-fpdlink-port1.dtbo
	imx8mp-phyflex-vm017-csi1.dtbo
	imx8mp-phyflex-vm017-csi1-fpdlink-port0.dtbo
	imx8mp-phyflex-vm017-csi1-fpdlink-port1.dtbo
	imx8mp-phyflex-vm017-csi2.dtbo
	imx8mp-phyflex-vm017-csi2-fpdlink-port0.dtbo
	imx8mp-phyflex-vm017-csi2-fpdlink-port1.dtbo
	imx8mp-phyflex-vm020-csi1.dtbo
	imx8mp-phyflex-vm020-csi1-fpdlink-port0.dtbo
	imx8mp-phyflex-vm020-csi1-fpdlink-port1.dtbo
	imx8mp-phyflex-vm020-csi2.dtbo
	imx8mp-phyflex-vm020-csi2-fpdlink-port0.dtbo
	imx8mp-phyflex-vm020-csi2-fpdlink-port1.dtbo
	imx8mp-phyflex-vm024-csi1.dtbo
	imx8mp-phyflex-vm024-csi2.dtbo

.. _imx8mp-phyvip-head-ubootexternalenv:
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti
   :end-before: .. extension-support-marker

.. include:: /bsp/dt-overlays-ampliphy-boot.rsti
   :start-after: .. change-u-boot-env-in-linux-marker

.. include:: /bsp/fpsc-device-tree.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART3 device in
|dt-som|.dtsi:

.. code-block::

   pinctrl_uart4: uart4grp {
           fsl,pins = <
                   MX8MP_IOMUXC_UART4_RXD__UART4_DCE_RX	0x140	/* UART3_RXD */
                   MX8MP_IOMUXC_UART4_TXD__UART4_DCE_TX	0x140	/* UART3_TXD */
           >;
   };

The first part of the string MX8MP_IOMUXC_UART4_RXD__UART4_DCE_RX names the pad
(in this example UART4_RX). The second part of the string (UART3_DCE_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal resistors are
disabled.

The device tree representation for UART3 pinmuxing:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L612`

RS232/RS485
-----------

The FPSC Standard supports 3 UART units. On the |sbc|-|soc|, TTL level signals
of UART3 (the standard console) are routed to a connector |ref-debugusbconnector|.

.. warning::
   The TTL level signals of |ref-debugusbconnector| are 1.8V compatible and not
   3.3V tolerant. Please use a USB to TTL serial adapter with 1.8V logic level
   only!

UART2 interface is used for the onboard Bluetooth module and thus not available
for external use.

UART1 interface is thus the only one brought out to |sbc| board connector
|ref-boardconnector1| and can be used for general purpose RS232 or RS485 communication.

.. note::
   With the |sbc| default expansion board PEB-B-006, UART1 is connected to a
   RS-485 transceiver chip capable of translating the UART1 signals to RS-485 differential signals available at the connector |ref-serial|.

.. include:: /bsp/peripherals/rs232.rsti
.. include:: /bsp/peripherals/rs485.rsti
.. include:: /bsp/peripherals/rs485-halfduplex.rsti
.. include:: /bsp/peripherals/rs485-fullduplex.rsti

The device tree representation for RS485 with default expansion board PEB-B-006:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip-peb-b-006.dtso#L170`

.. _imx8mp-phyvip-head-network:

Ethernet
--------

|sbc|-|soc| provides two Ethernet interfaces. However, with the default expansion
board PEB-B-006, only one gigabit Ethernet interface is available.

.. include:: /bsp/peripherals/network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L821`
and
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip.dts#L187`

DT configuration for the e.MMC interface can be found here:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L831`

.. include:: ../imx8mp/emmc.rsti

.. include:: ../peripherals/spi-master.rsti
  :end-before: .. peripherals-spi-nor-flash-marker

.. include:: /bsp/imx-common/peripherals/gpios.rsti

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C bus configuration from SoM (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L205`

General I²C bus configuration from carrierboard (e.g. |dt-carrierboard|.dts)
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip.dts#L63`

EEPROM
------

The system features three I2C EEPROM devices distributed across the SoM and
carrier board:

On the |som| SoM:

*  SoM Detection EEPROM (write-protected)

   *  Bus: I2C-1
   *  Address: 0x51
   *  Purpose: Factory configuration for SoM identification

*  User EEPROM

   *  Bus: I2C-1
   *  Address: 0x50
   *  Purpose: Available for user applications

Device Tree Reference for SoM EEPROMs:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L293`

And on the |sbc| carrier board:

*  Board Detection EEPROM

   *  Bus: I2C-2
   *  Address: 0x51
   *  Purpose: Reserved for carrier board identification

Device Tree Reference for Carrier Board:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip.dts#L67`

.. include:: /bsp/imx-common/peripherals/eeprom.rsti

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L318`

And the addions on the expansion board:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip-peb-b-006.dtso#L150`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed of up to 4 Gbit/s (SuperSpeed
'SS'). The USB subsystem has two independent USB controller cores.

.. include:: /bsp/peripherals/usb-host.rsti

DT representation for USB Host:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip-peb-b-006.dtso#L193`

CAN FD
------

The |sbc| has two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: /bsp/peripherals/canfd.rsti

Device Tree CAN configuration of |dt-som|.dtsi:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-fpsc-g-som.dtsi#L121`

and of |dt-expansionboard|.dtso:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip-peb-b-006.dtso#L85`

Audio
-----

Playback devices supported for |sbc|-|soc| are HDMI and the TI TLV320AIC3007
audio codec on the default PEB-B-006 expansion board. The connector X16 on the
PEB-B-006 provides mono-speaker output, while the X17 connector provides input
for the microphone. The PEB-B-006 also features a Class-D amplifier output on
the X18 connector.

.. note::
   For more details refer to the |sbc|-|soc| Hardware Manual and the Schematics.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
:linux-phytec-imx:`tree/v6.12.49-2.2.0-phy14/arch/arm64/boot/dts/freescale/imx8mp-phyflex-phyvip-peb-b-006.dtso#L51`

.. include:: display.rsti

.. include:: /bsp/peripherals/gpu.rsti

.. include:: /bsp/imx8/peripherals/pm.rsti
   :end-before: .. suspend_to_ram_start_label

.. include:: /bsp/imx8/peripherals/tm.rsti
   :end-before: .. tm-gpio-fan-marker

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: /bsp/imx-common/peripherals/power-key.rsti

.. include:: /bsp/imx8/peripherals/isp.rsti

.. include:: /bsp/imx8/peripherals/ocotp-ctrl.rsti

.. +---------------------------------------------------------------------------+
.. i.MX 8M Plus M7 Core
.. +---------------------------------------------------------------------------+
