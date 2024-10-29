.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MM-PD23.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-mini/nano/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-polis-imx8mm-5/phytec-qt6demo-image-phyboard-polis-imx8mm-5.wic
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-polis-imx8mm-5/phytec-qt6demo-image-phyboard-polis-imx8mm-5.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-polis-imx8mm-5/imx-boot-tools/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mm
.. _`static-pdf-dl`: ../../../_static/imx8mm-head.pdf

.. IMX8(MM) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mm/phycore-imx8mm.c?h=v2022.04_2.2.2-phy5#n120


.. General Replacements
.. |doc-id| replace:: L-1002e.Ax
.. |kit| replace:: **phyCORE-i.MX8M Mini Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: phyBOARD-Polis
.. |soc| replace:: i.MX 8M Mini
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-i.MX8MM
.. |debug-uart| replace:: ttymxc2
.. |serial-uart| replace:: ttymxc0
.. |bluetooth-uart| replace:: UART2
.. |expansion-connector| replace:: X8


.. Linux Kernel
.. |kernel-defconfig| replace:: imx_v8_defconfig imx8_phytec_distro.config imx8_phytec_platform.config
.. |kernel-recipe-path| replace:: meta-phytec/dynamic-layers/freescale-layer/recipes-kernel/linux/linux-imx_*.bb
.. |kernel-repo-name| replace:: linux-imx
.. |kernel-repo-url| replace:: git://git.phytec.de/linux-imx
.. |kernel-socname| replace:: imx8mm
.. |kernel-tag| replace:: v5.15.71_2.2.2-phy3
.. |emmcdev| replace:: mmcblk2

.. Bootloader
.. |u-boot-offset| replace:: 33
.. |u-boot-offset-boot-part| replace:: 33
.. |u-boot-mmc-flash-offset| replace:: 0x42
.. |u-boot-defconfig| replace:: phycore-imx8mm_defconfig
.. |u-boot-emmc-devno| replace:: 2
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://git.phytec.de/u-boot-imx


.. IMX8(MM) specific
.. |u-boot-socname-config| replace:: IMX8MM
.. |u-boot-tag| replace:: v2022.04_2.2.2-phy5


.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM


.. Devicetree
.. |dt-carrierboard| replace:: imx8mm-phyboard-polis-rdk
.. |dt-som| replace:: imx8mm-phycore-som
.. |dtbo-rpmsg| replace:: imx8mm-phycore-rpmsg.dtbo
.. |dtbo-peb-av-10| replace:: imx8mm-phyboard-polis-peb-av-010.dtbo

.. IMX8(MM) specific
.. |dt-somnetwork| replace:: :imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n59`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`kirkstone`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MM
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: kirkstone
.. |yocto-distro| replace:: ampliphy-vendor-xwayland
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: phyboard-polis-imx8mm-5
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MM-PD23.1.0
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX8MM-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX8MM-PD23.1.y
.. |yocto-ref-manual| replace:: Yocto Reference Manual (kirkstone)
.. _yocto-ref-manual: https://phytec.github.io/doc-bsp-yocto/yocto/manual-index.html#kirkstone
.. _yocto-ref-manual-kernel-and-bootloader-config: https://phytec.github.io/doc-bsp-yocto/yocto/kirkstone.html#kernel-and-bootloader-configuration
.. |yocto-sdk-rev| replace:: 4.0.13
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. Refs
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx8mm-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mm-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X30) <imx8mm-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mm-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mm-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mm-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mm-head-development>`
.. |ref-usb-otg| replace:: :ref:`X2 <imx8mm-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <imx8mm-head-development-build-uboot>`
.. |ref-disable-emmc-part| replace:: :ref:`Disable booting from eMMC boot partitions <emmc-disable-boot-part>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx8mm-head-format-sd>`


.. IMX8(MM) specific replacements
.. |sbc-network| replace:: \
.. |pollux-fan-note| replace:: Only GPIO fan supported.
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mm-head-ubootexternalenv>`


.. M-Core specific
.. |mcore| replace:: M4 Core
.. |mcore-zephyr-docs| replace:: https://docs.zephyrproject.org/latest/boards/phytec/mimx8mm_phyboard_polis/doc/index.html
.. |mcore-jtag-dev| replace:: MIMX8MM6_M4
.. |mcore-sdk-version| replace:: 2.13.0

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

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

The table below shows the Compatible BSPs for this manual:

================ ================ ================= ==========
Compatible BSP'S BSP Release Type BSP Release  Date BSP Status

================ ================ ================= ==========
..
================ ================ ================= ==========

.. include:: ../../intro.rsti

Supported Hardware
------------------

The |sbc| populated with either the i.MX 8M Mini SoC or i.MX 8M Nano SoC, is
supported.

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname| `download <dlpage-bsp_>`_.
If you choose a specific **Machine Name** in the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware

.. _imx8mm-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
..                          Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mm-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

* To boot from an SD card, |ref-bootswitch| needs to be set to the following
  position:

.. list-table:: Bootmode Selection

   *  -  .. figure:: images/SD_Card_Boot.jpg

            Mini

* Insert the SD card
* Connect the target and the host with **mirco USB** on |ref-debugusbconnector|
  debug USB
* Power up the board

.. +---------------------------------------------------------------------------+
..                          Building the BSP                                   |
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx8mm-head-images:

* **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
  Bootloader image!
* **oftree**: Default kernel device tree
* **u-boot-spl.bin**: Secondary program loader (SPL)
* **bl31-imx8mm.bin**: ARM Trusted Firmware binary
* **lpddr4_pmu_train_2d_dmem_202006.bin,
  lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
* **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
  Trusted Firmware and DDR firmware. This is the final bootloader image which is
  bootable.
* **Image**: Linux kernel image
* **Image.config**: Kernel configuration
* **imx8mm-phyboard-polis-rdk*.dtb**: Kernel device tree file
* **imx8mm-phy*.dtbo**: Kernel device tree overlay files
* **phytec-qt6demo-image\*.tar.gz**: Root file system
* **phytec-qt6demo-image\*.rootfs.wic.xz**: SD card image

.. +---------------------------------------------------------------------------+
..                          INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

The |sbc| features a boot switch with six individually switchable ports to
select the phyCORE-|soc| default bootsource.

.. _imx8mm-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
..                                DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mm-head-development:

Development
===========

.. include:: /bsp/imx-common/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot.rsti

.. include:: /bsp/imx-common/development/uuu.rsti

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti
.. _imx8mm-head-development-build-uboot:
.. include:: /bsp/imx-common/development/standalone_build_u-boot_binman.rsti

.. include:: /bsp/imx-common/development/standalone_build_kernel.rsti

.. include:: /bsp/imx8/development/development_manifests.rsti

.. include:: /bsp/imx8/development/upstream_manifest.rsti

.. _imx8mm-head-format-sd:

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
..                               DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mm-head-device-tree:
.. include:: /bsp/device-tree.rsti

::

   imx8mm-phyboard-polis-peb-eval-01.dtbo
   imx8mm-phyboard-polis-peb-av-010.dtbo
   imx8mm-phycore-rpmsg.dtbo
   imx8mm-phycore-no-eth.dtbo
   imx8mm-phycore-no-spiflash.dtbo
   imx8mm-vm016.dtbo
   imx8mm-vm016-fpdlink.dtbo
   imx8mm-vm017.dtbo
   imx8mm-vm017-fpdlink.dtbo
   imx8mm-dual-vm017-fpdlink.dtbo

.. _imx8mm-head-ubootexternalenv:
.. include:: ../dt-overlays.rsti

.. +---------------------------------------------------------------------------+
..                        ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART1 device in
|dt-carrierboard|.dts:

.. code-block::

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

.. include:: /bsp/peripherals/rs232.rsti
.. include:: /bsp/peripherals/rs485.rsti
.. include:: /bsp/peripherals/rs485-halfduplex.rsti

The device tree representation for RS232 and RS485:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n291`

.. _imx8mm-head-network:

Network
-------

|sbc|-|soc| provides one Gigabit Ethernet interface.

.. include:: /bsp/imx-common/peripherals/network.rsti

WLAN
....

For WLAN and Bluetooth support, we use the Sterling-LWB module from LSR. This
module supports 2,4 GHz bandwidth and can be run in several modes, like client
mode, Access Point (AP) mode using WEP, WPA, WPA2 encryption, and more. More
information about the module can be found at
https://connectivity-staging.s3.us-east-2.amazonaws.com/2019-09/CS-DS-SterlingLWB%20v7_2.pdf

.. include:: ../../peripherals/wireless-network.rsti

.. note::

   If the connection fails with the error message: "Failed to connect:
   org.bluez.Error.Failed" try restarting PulseAudio with:

   .. code-block:: console

      target:~$ pulseaudio --start

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n383`

DT configuration for the eMMC interface can be found here:
:imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n335`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/imx-common/emmc.rsti

.. include:: ../peripherals/spi-master.rsti

The definition of the SPI master node in the device tree can be found here:

:imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n87`

.. include:: ../peripherals/gpios.rsti

Pinmuxing of some GPIO pins in the device tree |dt-carrierboard|.dts:

.. code-block::

   pinctrl_leds: leds1grp {
           fsl,pins = <
                   MX8MM_IOMUXC_GPIO1_IO01_GPIO1_IO1       0x16
                   MX8MM_IOMUXC_GPIO1_IO14_GPIO1_IO14      0x16
                   MX8MM_IOMUXC_GPIO1_IO15_GPIO1_IO15      0x16
           >;
   };

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n36`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C1 bus configuration (e.g. |dt-som|.dtsi):
:imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n119`

General I²C4 bus configuration (e.g. |dt-carrierboard|.dts):
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n244`


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

DT representation, e.g. in phyCORE-|soc| file |dt-som|.dtsi can be
found in our PHYTEC git:
:imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n311`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:imx-dt:`imx8mm-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n319`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed up to 480 Mbps (HighSpeed
'HS'). The USB subsystem has two independent USB controller cores. Both cores
are On-The-Go (OTG) controller cores and are capable of acting as a USB
peripheral device or a USB host. Each is connected to a USB 2.0 PHY.

.. include:: /bsp/peripherals/usb-host.rsti

User USB2 (host) configuration is in the kernel device tree
|dt-carrierboard|.dts:

.. code-block::

   &usbotg2 {
           dr_mode = "host";
           picophy,pre-emp-curr-control = <3>;
           picophy,dc-vol-level-adjust = <7>;
           status = "okay";
   };

DT representation for USB Host:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n347`

.. include:: /bsp/peripherals/usb-otg.rsti

Both USB interfaces are configured as host in the kernel device tree
|dt-carrierboard|.dts. See:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n335`

CAN FD
------

The |sbc| two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. Hint::

   phyBOARD-Polis has an external CANFD chip MCP2518FD connected over SPI.
   There are different interfaces involved, which limits the datarate
   capabilities of CANFD.

.. Hint::

   On phyBOARD-Polis-i.MX8MM a terminating resistor can be enabled by setting
   S5 to ON if required.

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
:imx-dt:`imx8mm-phyboard-polis-rdk.dts?h=v5.15.71_2.2.2-phy3#n175`

.. include:: /bsp/peripherals/pcie.rsti

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
:imx-dt:`overlays/imx8mm-phyboard-polis-peb-av-010.dtsi?h=v5.15.71_2.2.2-phy3#n54`

.. include:: /bsp/peripherals/video.rsti

Display
-------

The 10" Display is always active. If the PEB-AV-Connector is not connected, an
error message may occur at boot.

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

The device tree of PEB-AV-10 can be found here:
:imx-dt:`overlays/imx8mm-phyboard-polis-peb-av-010.dtsi?h=v5.15.71_2.2.2-phy3`

.. include:: ../peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

.. +---------------------------------------------------------------------------+
..                                i.MX 8M Mini M4 Core
.. +---------------------------------------------------------------------------+

.. include:: ../mcu.rsti

.. +---------------------------------------------------------------------------+
..                          BSP EXTENSIONS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/bsp-extensions.rsti
