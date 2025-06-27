.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MP-PD24.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-plus/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD24.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD24.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/phytec-qt6demo-image-phyboard-pollux-imx8mp-3.rootfs.wic.xz
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD24.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/phytec-qt6demo-image-phyboard-pollux-imx8mp-3.rootfs.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD24.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/imx-boot-tools/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD24.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mp
.. _`static-pdf-dl`: ../../../_static/imx8mp-libra-fpsc-head.pdf

.. IMX8(MP) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mp/phycore-imx8mp.c?h=v2024.04-2.0.0-phy7#n177


.. General Substitutions
.. |doc-id| replace:: L-XXXXX.Xx
.. |kit| replace:: **Libra i.MX 8M Plus FPSC Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: Libra
.. |soc| replace:: i.MX 8M Plus
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-|soc| FPSC
.. |debug-uart| replace:: ttymxc0
.. |serial-uart| replace:: ttymxc1
.. |bluetooth-uart| replace:: UART3
.. |expansion-connector| replace:: X6


.. Linux Kernel
.. |kernel-defconfig| replace:: imx8_phytec_defconfig
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-imx
.. |kernel-socname| replace:: imx8mp-fpsc
.. |kernel-tag| replace:: v6.6.23-2.0.0-phy10
.. |emmcdev| replace:: mmcblk2
.. |led-names| replace:: red:user1, green:user2 and blue:user3
.. |led-example| replace:: red\\:user1

.. Bootloader
.. |u-boot-defconfig| replace:: imx8mp-libra_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 2
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://git.phytec.de/u-boot-imx
.. |emmcdev-uboot| replace:: mmc 2
.. |sdcarddev-uboot| replace:: mmc 1

.. IMX8(MP) specific
.. |u-boot-socname-config| replace:: IMX8MP_LIBRA
.. |u-boot-tag| replace:: v2024.04_2.0.0-phy7


.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM


.. Devicetree
.. |dt-carrierboard| replace:: imx8mp-libra-rdk-fpsc
.. |dt-som| replace:: imx8mp-phycore-fpsc
.. |dtbo-rpmsg| replace:: conf-imx8mp-phycore-fpsc-rpmsg.dtbo
.. |dtbo-peb-av-10| replace:: imx8mp-libra-peb-av-10.dtbo

.. IMX8(MP) specific
.. |dt-somnetwork| replace:: :linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L50`
.. |dt-gpio-expander| replace:: :linux-phytec-imx:`tree/v6.6.52-2.2.0-phy16/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L189`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`scarthgap`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MP-FPSC
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: scarthgap
.. |yocto-distro| replace:: ampliphy-vendor-xwayland
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: imx8mp-libra-fpsc-1
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MP-PD24.1.0
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX8MP-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX8MP-FPSC-PD25.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (scarthgap) <yocto-man-scarthgap>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-scarthgap-kernel-and-bootloader-conf>`
.. |yocto-sdk-rev| replace::  5.0.x
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S3) <imx8mp-libra-fpsc-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mp-libra-fpsc-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X1) <imx8mp-libra-fpsc-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mp-libra-fpsc-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mp-libra-fpsc-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mp-libra-fpsc-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mp-libra-fpsc-head-development>`
.. |ref-usb-otg| replace:: :ref:`X5 (upper connector) <imx8mp-libra-fpsc-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx8mp-libra-fpsc-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx8mp-libra-fpsc-head-format-sd>`


.. IMX8(MP) specific
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found here:
   :linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L179`.
.. |pollux-fan-note| replace::
   Starting with BSP-Yocto-i.MX8MP-PD22.1.1 we have to switch from PWM fan
   to GPIO fan due to availability. The PWM fan will not be supported
   anymore and will not function with the new release.

.. |ref-serial| replace:: :ref:`X2 <imx8mp-libra-fpsc-head-components>`
.. |ref-jp3| replace:: :ref:`JP3 <imx8mp-libra-fpsc-head-components>`
.. |ref-jp4| replace:: :ref:`JP4 <imx8mp-libra-fpsc-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mp-libra-fpsc-head-ubootexternalenv>`
.. |lvds-display-adapters| replace:: PEB-AV-10
.. |weston-hdmi-mode| replace:: preferred


.. M-Core specific
.. |mcore| replace:: M7 Core
.. |mcore-zephyr-docs| replace:: https://docs.zephyrproject.org/latest/boards/phytec/mimx8mp_phyboard_pollux/doc/index.html
.. |mcore-jtag-dev| replace:: MIMX8ML8_M7
.. |mcore-sdk-version| replace:: 2.13.0

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-----------------------+----------------------+
| |doc-id| |soc| FPSC   |                      |
| BSP ManualHead        |                      |
+-----------------------+----------------------+
| Document Title        | |doc-id| |soc| FPSC  |
|                       | BSP Manual Head      |
+-----------------------+----------------------+
| Document Type         | BSP Manual           |
+-----------------------+----------------------+
| Article Number        | |doc-id|             |
+-----------------------+----------------------+
| Yocto Manual          |                      |
+-----------------------+----------------------+
| Release Date          | XXXX/XX/XX           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| FPSC  |
|                       | BSP Manual Head      |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

================ ================ ================= ==========
Compatible BSPs  BSP Release Type BSP Release  Date BSP Status

================ ================ ================= ==========
..
================ ================ ================= ==========


.. include:: ../../intro.rsti

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

.. _imx8mp-libra-fpsc-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mp-libra-fpsc-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

.. image:: images/SD_Card_Boot.png

*  Insert the SD card
*  Connect the target and the host with **micro USB** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx8mp-libra-fpsc-head-images:

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
*  **imx8mp-libra-rdk-fpsc*.dtb**: Kernel device tree file
*  **imx8mp-phy*.dtbo**: Kernel device tree overlay files
*  **phytec-qt6demo-image\*.tar.gz**: Root file system
*  **phytec-qt6demo-image\*.rootfs.wic.xz**: compressed SD card image

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S3)
--------------------

.. tip::

   Hardware revision baseboard: 1552.2

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx8mp-libra-fpsc-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/imx-common/installing-os.rsti

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mp-libra-fpsc-head-development:

Development
===========

.. include:: ../../imx-common/development/standalone_build_preface.rsti

.. warning::
   Using the SDK on older host distributions (e.g., Ubuntu 20.04 LTS) with Scarthgap NXP-based BSPs
   can cause issues when building U-Boot or Linux kernel tools for host use. If you encounter an
   "undefined reference" error, a workaround is to prepend the host's binutils to the PATH.

   .. code-block:: console

      host$ export PATH=/usr/bin:$PATH

   Run this after sourcing the SDK *environment-setup* file.

   Note, SDK issue has not been observed on newer distributions, such as Ubuntu 22.04, which appear to work
   without requiring any modifications.

.. _imx8mp-libra-fpsc-head-development-build-uboot:
.. include:: ../../imx-common/development/standalone_build_u-boot_binman.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: ../../imx-common/development/uuu.rsti

.. include:: /bsp/imx-common/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. include:: /bsp/imx-common/development/master_manifest.rsti

.. _imx8mp-libra-fpsc-head-format-sd:

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mp-libra-fpsc-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   imx8mp-isi-csi1.dtbo
   imx8mp-isi-csi2.dtbo
   imx8mp-isp-csi1.dtbo
   imx8mp-isp-csi2.dtbo
   |dtbo-peb-av-10|
   imx8mp-phyboard-pollux-peb-wlbt-05.dtbo
   imx8mp-phycore-no-eth.dtbo
   imx8mp-phycore-no-rtc.dtbo
   imx8mp-phycore-no-spiflash.dtbo
   imx8mp-phycore-rpmsg.dtbo
   imx8mp-vm016-csi1.dtbo
   imx8mp-vm016-csi1-fpdlink.dtbo
   imx8mp-vm016-csi2.dtbo
   imx8mp-vm016-csi2-fpdlink.dtbo
   imx8mp-vm017-csi1.dtbo
   imx8mp-vm017-csi1-fpdlink.dtbo
   imx8mp-vm017-csi2.dtbo
   imx8mp-vm017-csi2-fpdlink.dtbo

.. _imx8mp-libra-fpsc-head-ubootexternalenv:
.. include:: ../../dt-overlays.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART1 device in
|dt-carrierboard|.dts:

.. code-block::

   pinctrl_uart1: uart1grp {
           fsl,pins = <
                   MX8MP_IOMUXC_UART1_RXD_UART1_DCE_RX     0x140
                   MX8MP_IOMUXC_UART1_TXD_UART1_DCE_TX     0x140
           >;
   };

The first part of the string MX8MP_IOMUXC_UART1_RXD_UART1_DCE_RX names the pad
(in this example UART1_RXD). The second part of the string (UART1_DCE_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal resistors are
disabled.

The device tree representation for UART1 pinmuxing:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L373`

RS232/RS485
-----------

The |som| supports up to 4 UART units. On the |sbc|, TTL level signals
of UART1 (the standard console) and UART4 are routed to Silicon Labs CP2105 UART
to USB converter expansion. This USB is brought out at Micro-USB connector X1.
UART3 is at X6 (Expansion Connector) at TTL level. UART2 is connected to a
multi-protocol transceiver for RS-232 and RS-485, available at pin header
connector |ref-serial| at the RS-232 level, or at the RS-485 level. The
configuration of the multi-protocol transceiver is done by jumpers |ref-jp3| and
|ref-jp4| on the baseboard. For more information about the correct setup please
refer to the |som|/|sbc| Hardware Manual section UARTs.

We use the same device tree node for RS-232 and RS-485. RS-485 mode can be
enabled with ioctl TIOCSRS485. Also, full-duplex support is also configured
using ioctls. Have a look at our small example application rs485test, which is
also included in the BSP. The jumpers |ref-jp3| and |ref-jp4| need to be set
correctly.

.. include:: /bsp/peripherals/rs232.rsti
.. include:: /bsp/peripherals/rs485.rsti
.. include:: /bsp/peripherals/rs485-halfduplex.rsti
.. include:: /bsp/peripherals/rs485-fullduplex.rsti

The device tree representation for RS232 and RS485:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L412`

.. _imx8mp-libra-fpsc-head-network:

Network
-------

|sbc|-|soc| provides two ethernet interfaces. A gigabit Ethernet is provided by our
module and board.

.. warning::

   The naming convention of the Ethernet interfaces in the hardware (ETH0
   and ETH1) do not align with the network interfaces (eth0 and eth1) in
   Linux. So, be aware of these differences:

   | ETH1 = eth0
   | ETH0 = eth1

.. include:: /bsp/imx-common/peripherals/network.rsti
   :end-before: .. kernel-network-environment-marker

Secondary Ethernet Interface Configuration in U-Boot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, U-Boot utilizes the Ethernet PHY located on the module. To use the network connection
provided by the PHY on the carrier board, configuration changes are required.

To enable the secondary Ethernet interface in U-Boot, the active Ethernet connection must be
adjusted. The IP address configuration in U-Boot may also need modification.

Configure the development host with IP address 192.168.4.10 and netmask 255.255.255.0. The target
device must then be configured as follows:

.. code-block::

    u-boot=> setenv ethact eth1
    u-boot=> setenv ipaddr 192.168.4.11

.. include:: /bsp/imx-common/peripherals/network.rsti
   :start-after: .. kernel-network-environment-marker

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L422`

DT configuration for the e.MMC interface can be found here:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L214`

.. include:: ../imx8mp/emmc.rsti

.. include:: ../peripherals/spi-master.rsti

The definition of the SPI master node in the device tree can be found here:

:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L76`

.. include:: gpios.rsti

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-imx:`tree/v6.6.52-2.2.0-phy16/arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc.dts#L165`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C1 bus configuration (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L113`

General I²C2 bus configuration (e.g. |dt-carrierboard|.dts)
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L239`


EEPROM
------

On the |som| there is an i2c EEPROM flash populated. It has two addresses. The
main EEPROM space (bus: I2C-0 address: 0x51) can be accessed via the sysfs
interface in Linux. The first 256 bytes of the main EEPROM and the ID-page
(bus: I2C-0 address: 0x59) are used for board detection and must not be
overwritten. Therefore the ID-page can not be accessed via the sysfs interface.
Overwriting reserved spaces will result in boot issues.

.. note::

   If you deleted reserved EEPROM spaces, please contact our support!

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in |som| file imx8mp-phycore-som.dtsi can be
found in our PHYTEC git:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L201`

.. include:: ../../peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi#L208`

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
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L380`

CAN FD
------

The |sbc| has two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L203`

.. include:: /bsp/peripherals/pcie.rsti

Device Tree PCIe configuration of |dt-carrierboard|.dts:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L345`

Audio
-----

Playback devices supported for |sbc| are HDMI and the TI TLV320AIC3007 audio
codec on the PEB-AV-10 connector. On the AV-Connector there is a 3.5mm headset
jack with OMTP-standard and an 8-pin header. The 8-pin header contains a mono
speaker, headphones, and line in signals.

.. note::

   Using the PEB-AV-10 connector for display output along HDMI as audio output
   is not supported. The audio output device must match the video output device.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-peb-av-10.dtso#L58`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti
   :end-before: .. supported-display-interfaces-marker-start

The |sbc| supports up to 3 different display outputs. Two can be used
simultaneously. The following table shows the required extensions and devicetree
overlays for the different interfaces.

========= ======================== ======================================
Interface Expansion                devicetree overlay
========= ======================== ======================================
HDMI      |sbc|                    no overlay needed (enabled by default)
LVDS0     PEB-AV-10                |dtbo-peb-av-10|
                                   (loaded by default)
LVDS1     |sbc|                    disabled if PEB-AV-10 overlay is used
========= ======================== ======================================

.. include:: display.rsti
   :start-after: .. supported-display-interfaces-marker-end
   :end-before: .. no-peb-av-12-marker

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

Device tree description of LVDS-1 and HDMI can be found here:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L294`
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L218`

The device tree of LVDS-0 on PEB-AV-10 can be found here:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-peb-av-10.dtso#L133`

.. include:: ../peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

The device tree description of GPIO Fan can be found here:
:linux-phytec-imx:`tree/v6.6.23-2.0.0-phy10/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-rdk.dts#L35`

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/snvs-power-key.rsti

.. include:: ../peripherals/npu.rsti

.. include:: ../peripherals/isp.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

.. +---------------------------------------------------------------------------+
.. i.MX 8M Plus M7 Core
.. +---------------------------------------------------------------------------+

.. include:: ../mcu.rsti
