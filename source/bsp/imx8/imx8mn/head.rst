.. Download links
.. |dlpage-bsp| replace:: our bsp
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MM-PD22.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-mini/nano/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD22.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD22.1.0/images/ampliphy-vendor/phyboard-polis-imx8mn-1/phytec-headless-image-phyboard-polis-imx8mn-1.sdcard
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD22.1.0/images/ampliphy-vendor/phyboard-polis-imx8mn-1/imx-boot-tools/ 
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mm

.. IMX8(MN) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mn/phycore-imx8mn.c?h=v2021.04_2.2.0-phy


.. General Replacements
.. |atfloadaddr| replace:: 0x960000
.. |doc-id| replace:: L-1002e.Ax
.. |kit| replace:: **phyCORE-i.MX8M Nano Kit**
.. |mcore| replace:: M4 Core
.. |sbc| replace:: phyBOARD-Polis
.. |soc| replace:: i.MX 8M Nano
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-i.MX8MM


.. Linux Kernel
.. |kernel-socname| replace:: imx8mn
.. |kernel-tag| replace:: v5.10.72_2.2.0-phy9


.. Devicetree
.. |dt-carrierboard| replace:: imx8mn-phyboard-polis-rdk
.. |dt-som| replace:: imx8mn-phycore-som

.. IMX8(MN) specific
.. |dt-somnetwork| replace:: :imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy4#n44`

.. Yocto
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MM
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: hardknott
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-headless-image
.. |yocto-machinename| replace:: phyboard-polis-imx8mn-2
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MM-PD22.1.1
.. |yocto-ref-manual| replace:: L-813e.A13 Yocto Reference Manual (kirkstone)
.. _yocto-ref-manual: https://www.phytec.de/cdocuments/?doc=PoDEHw


.. Refs
.. |ref-bootswitch| replace:: *bootmode switch* :ref:`(S1) <imx8mn-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mn-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X30) <imx8mn-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mn-head-device-tree>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mn-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mn-head-development>`
.. |ref-usb-otg| replace:: :ref:`X2 <imx8mn-head-components>`


.. IMX8(MN) specific replacements
.. |pollux-sbc-network| replace:: \
.. |uboot-tag| replace:: v2021.04_2.2.0-phy5
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mn-head-ubootexternalenv>`


=======================
|doc-id| |soc| BSP Head
=======================

+----------------------+----------------------+
| |doc-id| |soc| BSP                          |
| Manual Head                                 |
+----------------------+----------------------+
| Document Title       | |doc-id| |soc| BSP   |
|                      | Manual Head          |
+----------------------+----------------------+
| Document Type        | BSP Manual           |
+----------------------+----------------------+
| Article Number       | |doc-id|             |
+----------------------+----------------------+
| Yocto Manual         |                      |
+----------------------+----------------------+
| Release Date         | XXXX/XX/XX           |
+----------------------+----------------------+
| Is Branch of         | |doc-id| |soc| BSP   |
|                      | Manual Head          |
+----------------------+----------------------+

.. include:: ../../intro.rsti

Supported Hardware
------------------

The |sbc| populated with the |soc| SoC is supported.

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname| `download <dlpage-bsp_>`_.
If you choose a specific **Machine Namein the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware

.. _imx8mn-head-components:
.. include:: ../imx8mm/components.rsti

.. +---------------------------------------------------------------------------+
..                          Getting Started
.. +---------------------------------------------------------------------------+

.. include:: /bsp/getting-started.rsti

First Start-up
--------------

* To boot from an SD card, |ref-bootswitch| needs to be set to the following
  position:

.. list-table:: Bootmode Selection
   :align: center

   *  -  .. figure:: images/Nano_SD_BOOT.jpg
            :width: 250px

            SD Card Boot

* Insert the SD card
* Connect the target and the host with **mirco USB** on |ref-debugusbconnector|
  debug USB
* Power up the board

.. +---------------------------------------------------------------------------+
..                          Building the BSP                                   |
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx8mn-head-images:

* **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
  Bootloader image!
* **oftree**: Default kernel device tree
* **u-boot-spl.bin**: Secondary program loader (SPL)
* **bl31-imx8mm.bin**: ARM Trusted Firmware binary
* **lpddr4_pmu_train_2d_dmem_202006.bin,
  lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
* **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
  Trusted Firmware and DDR firmware. This is the final bootloader image which is
  bootable.
* **Image**: Linux kernel image
* **Image.config**: Kernel configuration
* **imx8mn-phyboard-polis-rdk*.dtb**: Kernel device tree file
* **imx8mn-phy*.dtbo**: Kernel device tree overlay files
* **phytec-headless-image\*.tar.gz**: Root file system 
* **phytec-headless-image\*.sdcard**: SD card image

.. +---------------------------------------------------------------------------+
..                          INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

.. tip::

   Hardware revision baseboard: 1552.1

The |sbc| features a boot switch with six individually switchable ports to
select the phyCORE-|soc| default bootsource.

.. _imx8mn-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
..                                DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mn-head-development:
.. include:: /bsp/development.rsti

.. +---------------------------------------------------------------------------+
..                               DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mn-head-device-tree:
.. include:: /bsp/device-tree.rsti

::

   imx8mn-phyboard-polis-peb-eval-01.dtbo
   imx8mn-phyboard-polis-peb-av-010.dtbo
   imx8mn-phycore-rpmsg.dtbo
   imx8mn-phycore-no-eth.dtbo
   imx8mn-phycore-no-spiflash.dtbo
   imx8mn-vm016.dtbo
   imx8mn-vm016-fpdlink.dtbo
   imx8mn-vm017.dtbo
   imx8mn-vm017-fpdlink.dtbo
   imx8mn-dual-vm017-fpdlink.dtbo

.. _imx8mn-head-ubootexternalenv:
.. include:: ../dt-overlays.rsti

.. +---------------------------------------------------------------------------+
..                        ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: ../peripherals/pin-muxing.rsti

::

   pinctrl_uart1: uart1grp {
       fsl,pins = <
           MX8MM_IOMUXC_SAI2_RXFS_UART1_DCE_TX     0x00
           MX8MM_IOMUXC_SAI2_RXC_UART1_DCE_RX      0x00
           MX8MM_IOMUXC_SAI2_RXD0_UART1_DCE_RTS_B  0x00
           MX8MM_IOMUXC_SAI2_TXFS_UART1_DCE_CTS_B  0x00
       >;
   };

The first part of the string MX8MM_IOMUXC_SAI2_RXFS_UART1_DCE_TX names the pad (in this example
SAI2_RXFS). The second part of the string (UART1_DCE_RX) is the desired muxing option for this pad.
The pad setting value (hex value on the right) defines different modes of the pad, for example, if
internal pull resistors are activated or not. In this case, the internal resistors are disabled.

RS232/RS485
-----------

The |soc| SoC provides up to 4 UART units. PHYTEC boards support different
numbers of these UART units. UART1 can also be used as RS-485. For this,
|ref-bootswitch| needs to be set correctly:

.. list-table:: Switch between UART1 RS485/RS232

   *  - .. figure:: /bsp/imx8/imx8mm/images/UART1_RS485.png

            **UART1 RS485**

      - .. figure:: /bsp/imx8/imx8mm/images/UART1_RS232.jpg

           **UART1 RS232**

.. include:: /bsp/imx8/peripherals/rs232-485.rsti

The device tree representation for RS232 and RS485:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n171`

.. _imx8mn-head-network:
.. include:: ../peripherals/network.rsti

.. include:: ../imx8mm/wireless-network.rsti

.. include:: ../peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n249`

DT configuration for the eMMC interface can be found here:
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy4#n296`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: ../peripherals/spi-master.rsti

The definition of the SPI master node in the device tree can be found here:

:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n76`

.. include:: ../peripherals/gpios.rsti

Pinmuxing of some GPIO pins in the device tree |dt-carrierboard|.dtsi::

   pinctrl_leds: leds1grp {
           fsl,pins = <
                   MX8MM_IOMUXC_GPIO1_IO01_GPIO1_IO1       0x16
                   MX8MM_IOMUXC_GPIO1_IO14_GPIO1_IO14      0x16
                   MX8MM_IOMUXC_GPIO1_IO15_GPIO1_IO15      0x16
           >;
   };

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n37`

.. include:: /bsp/imx8/peripherals/i2c-bus.rsti

General I²C1 bus configuration (e.g. |dt-som|.dtsi):
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy#n97`

General I²C2 bus configuration (e.g. |dt-carrierboard|.dtsi):
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n137`


EEPROM
------

There are two different i2c EEPROM flashes populated on |som|. Both can be used
with the sysfs interface in Linux. The ID page of the I2C EEPROM populated on
the SoM is also used for board detection.

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in phyCORE-|soc| file |dt-som|.dtsi can be
found in our PHYTEC git:
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy4#n247`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.10.72_2.2.0-phy9#n194`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed up to 480 Mbps (HighSpeed
'HS'). The |soc| SoC has a single USB controller core that is set to OTG mode.
To use the micro USB / OTG port dip switch S1 Pos5 has to be set to on.

.. include:: /bsp/peripherals/usb-host.rsti

User USB2 (host) configuration is in the kernel device tree
|kernel-socname|.dtsi::

   &usbotg2 {
           dr_mode = "host";
           picophy,pre-emp-curr-control = <3>;
           picophy,dc-vol-level-adjust = <7>;
           status = "okay";
   };

DT representation for USB Host:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy9#n240`

.. include:: /bsp/peripherals/usb-otg.rsti

Both USB interfaces are configured as host in the kernel device tree
imx8mm-phyboard-polis.dtsi. See:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n211`

CAN FD
------

The |sbc| two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation:  https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of imx8mm-phyboard-polis.dtsi:
:imx-dt:`imx8mn-phyboard-polis.dtsi?h=v5.10.72_2.2.0-phy4#n94`

Audio
-----

The PEB-AV-10-Connector exists in two versions and the 1531.1 version is
populated with a TI TLV320AIC3007 audio codec. Audio support is done via the I2S
interface and controlled via I2C.

There is a 3.5mm headset jack with OMTP standard and an 8-pin header to connect
audio devices with the AV-Connector.  The 8-pin header contains a mono speaker,
headphones, and line-in signals.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
:imx-dt:`overlays/imx8mn-phyboard-polis-peb-av-010.dtso?h=v5.10.72_2.2.0-phy4#n56`

.. include:: /bsp/peripherals/video.rsti

Display
-------

The 10" Display is always active. If the PEB-AV-Connector is not connected, an
error message may occur at boot.

.. include:: /bsp/imx8/peripherals/display.rsti

The device tree of PEB-AV-10 can be found here:
:imx-dt:`overlays/imx8mn-phyboard-polis-peb-av-010.dtso?h=v5.10.72_2.2.0-phy4`

.. include:: ../peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

.. +---------------------------------------------------------------------------+
..                                M Core
.. +---------------------------------------------------------------------------+

.. include:: ../imx8mm/mcu.rsti

.. +---------------------------------------------------------------------------+
..                          BSP EXTENSIONS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/bsp-extensions.rsti
