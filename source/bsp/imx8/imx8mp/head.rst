.. Download links
.. |dlpage-bsp| replace:: our bsp
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MP-PD22.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-plus/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD22.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD22.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/phytec-qt5demo-image-phyboard-pollux-imx8mp-3.sdcard
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD22.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/imx-boot-tools/ 
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mp
.. _yocto-ref-manual: https://www.phytec.de/cdocuments/?doc=PoDEHw

.. IMX8(MP) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mp/phycore-imx8mp.c?h=v2021.04_2.2.0-phy#n163
.. _dtsomnetwork: https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n41
.. _dtsbcnetwork: https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n149


.. General Substitutions
.. |kit| replace:: **phyCORE-i.MX8M Plus Kit**
.. |soc| replace:: i.MX 8M Plus
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-i.MX8MP
.. |sbc| replace:: phyBOARD-Pollux
.. |mcore| replace:: M7 Core
.. |atfloadaddr| replace:: 0x970000
.. |doc-id| replace:: L-1017e.Ax


.. Linux Kernel
.. |kernel-tag| replace:: v5.10.72_2.2.0-phy9
.. |kernel-socname| replace:: imx8mp


.. Devicetree
.. |dt-carrierboard| replace:: imx8mp-phyboard-pollux-rdk
.. |dt-som| replace:: imx8mp-phycore-som


.. Yocto
.. |yocto-ref-manual| replace:: L-813e.A13 Yocto Reference Manual (kirkstone).
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MP
.. _yocto-bsp-name: `dl-server`_
.. |yocto-distro| replace:: ampliphy-vendor-xwayland
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MP-PD22.1.0
.. |yocto-codename| replace:: hardknott
.. |yocto-imagename| replace:: phytec-qt5demo-image
.. |yocto-machinename| replace:: phyboard-pollux-imx8mp-3


.. Ref Substitutions
.. |ref-bootswitch| replace:: *bootmode switch* :ref:`(S3) <imx8mp-head-bootswitch>`
.. |ref-debugusbconnector| replace:: :ref:`(X1) <imx8mp-head-components>`
.. |ref-usb-otg| replace:: :ref:`X2 <imx8mp-head-components>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mp-head-images>`
.. |ref-dt| replace:: :ref:`device tree <imx8mp-head-device-tree>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mp-head-development>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mp-head-network>`


.. IMX8(MP) specific
.. |ref-jp3| replace:: :ref:`JP3 <imx8mp-head-components>`
.. |ref-jp4| replace:: :ref:`JP4 <imx8mp-head-components>`
.. |uboot-tag| replace:: v2021.04_2.2.0-phy7
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mp-head-ubootexternalenv>`
.. |pollux-som-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found `here <dtsbcnetwork_>`_.


==============================
|doc-id| |soc| BSP Manual Head
==============================

+-----------------------+----------------------+
| |doc-id| |soc| BSP    |                      |
| ManualHead            |                      |
+-----------------------+----------------------+
| Document Title        | |doc-id| |soc| BSP   |
|                       | Manual Head          |
+-----------------------+----------------------+
| Document Type         | BSP Manual           |
+-----------------------+----------------------+
| Article Number        | |doc-id|             |
+-----------------------+----------------------+
| Yocto Manual          |                      |
+-----------------------+----------------------+
| Release Date          | XXXX/XX/XX           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| BSP   |
|                       | Manual Head          |
+-----------------------+----------------------+

.. include:: ../../intro.rsti

Supported Hardware
------------------

The |sbc| with 2GB RAM  is supported. 

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname| `download <dlpage-bsp_>`_.

If you choose a specific Machine Name in the section Supported Machines, you can
see which Article Numbers are available under this machine and also a short
description of the hardware information. In case you only have the Article
Number of your hardware, you can leave the Machine Name drop-down menu empty and
only choose your Article Number. Now it should show you the necessary Machine
Name for your specific hardware

.. _imx8mp-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. include:: /bsp/getting-started.rsti

First Start-up
--------------

* To boot from an SD card, |ref-bootswitch| needs to be set to the following
  position:

.. image:: images/SD_Card_Boot.png

* Insert the SD card
* Connect the target and the host with **mirco USB** on |ref-debugusbconnector|
  debug USB
* Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx8mp-head-images:

* **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
  Bootloader image!
* **oftree**: Default kernel device tree
* **u-boot-spl.bin**: Secondary program loader (SPL)
* **bl31-imx8mp.bin**: ARM Trusted Firmware binary
* **lpddr4_pmu_train_2d_dmem_202006.bin,
  lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
* **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
  Trusted Firmware and DDR firmware. This is the final bootloader image which is
  bootable.
* **Image**: Linux kernel image
* **Image.config**: Kernel configuration
* **imx8mp-phyboard-pollux-rdk*.dtb**: Kernel device tree file
* **imx8mp-phy*.dtbo**: Kernel device tree overlay files
* **phytec-qt5demo-image\*.tar.gz**: Root file system 
* **phytec-qt5demo-image\*.sdcard**: SD card image

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
select the phyCORE-|soc| default bootsource.

.. _imx8mp-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mp-head-development:
.. include:: /bsp/development.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mp-head-device-tree:
.. include:: /bsp/device-tree.rsti

::

   imx8mp-isi-csi1.dtbo
   imx8mp-isi-csi2.dtbo
   imx8mp-isp-csi1.dtbo
   imx8mp-isp-csi2.dtbo
   imx8mp-phyboard-pollux-peb-av-010.dtbo
   imx8mp-phyboard-pollux-peb-av-012.dtbo
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

.. hint::
   There is one more overlay available for phyboard-pollux-imx8mp-2.conf:
   imx8mp-phyboard-pollux-1552.1.dtbo

.. _imx8mp-head-ubootexternalenv:
.. include:: ../dt-overlays.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: ../peripherals/pin-muxing.rsti

::

   pinctrl_uart1: uart1grp {
       fsl,pins = <
           MX8MP_IOMUXC_UART1_RXD_UART1_DCE_RX     0x49
           MX8MP_IOMUXC_UART1_TXD_UART1_DCE_TX     0x49
       >;
   };

The first part of the string MX8MP_IOMUXC_UART1_RXD_UART1_DCE_RX names the pad
(in this example UART1_RXD). The second part of the string (UART1_DCE_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal resistors are
disabled.

.. include:: rs232-485.rsti

.. _imx8mp-head-network:
.. include:: ../peripherals/network.rsti

WLAN and Bluetooth
..................

WLAN and Bluetooth on the |sbc| are provided by the PEB-WLBT-05 expansion card.
The PEB-WLBT-05 for |sbc| Quickstart Guide shows you how to install and use the
PEB-WLBT-05.

.. include:: ../peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n381

DT configuration for the eMMC interface can be found here:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n207

.. include:: /bsp/peripherals/emmc.rsti

.. include:: emmc.rsti

.. include:: ../peripherals/spi-master.rsti

The definition of the SPI master node in the device tree can be found here:

https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n67

.. include:: ../peripherals/gpios.rsti

.. include:: ../../peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n224

.. include:: i2c-bus.rsti

EEPROM
------

There are two different i2c EEPROM flashes populated on |som| SoM and on the
|sbc|. Both can be used with the sysfs interface in Linux. The ID page of the
I2C EEPROM populated on the SoM is also used for board detection.

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in phyCORE-|soc| file imx8mp-phycore-som.dtsi can be
found in our PHYTEC git:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n188

.. include:: ../../peripherals/rtc.rsti

DT representation for I²C RTCs:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n194

.. include:: ../peripherals/usb-host.rsti

DT representation for USB Host:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n354

CAN FD
------

The |sbc| two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation:  https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of imx8mp-phyboard-pollux.dtsi:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n173

.. include:: /bsp/peripherals/pcie.rsti

Device Tree PCIe configuration of imx8mm-phyboard-polis.dts:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n285

Audio
-----

Playback devices supported for |sbc| are HDMI and the TI TLV320AIC3007 audio
codec on the PEB-AV-10 connector. On the AV-Connector there is a 3.5mm headset
jack with OMTP-standard and an 8-pin header. The 8-pin header contains a mono
speaker, headphones, and line in signals.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/overlays/imx8mp-phyboard-pollux-peb-av-010.dtso?h=v5.10.72_2.2.0-phy9#n43

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: ../peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

The device tree description of PWM Fan can be found here:
https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux.dtsi?h=v5.10.72_2.2.0-phy9#n37

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/snvs-power-key.rsti

.. include:: ../peripherals/npu.rsti

.. include:: ../peripherals/isp.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

Reading the registers using /dev/mem will cause the system to hang unless the
ocotp_root_clk is enabled. To enable this clock permanent, add to the device
tree::

   &clk {
           init-on-array = <IMX8MP_CLK_OCOTP_ROOT>;
   };

.. +---------------------------------------------------------------------------+
.. M Core
.. +---------------------------------------------------------------------------+

.. include:: mcu.rsti

.. +---------------------------------------------------------------------------+
.. BSP EXTENSIONS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/bsp-extensions.rsti
