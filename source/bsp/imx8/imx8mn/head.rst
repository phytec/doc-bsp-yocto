.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MM-PD23.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-mini/nano/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor/phyboard-polis-imx8mn-2/phytec-headless-image-phyboard-polis-imx8mn-2.wic
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor/phyboard-polis-imx8mn-2/phytec-headless-image-phyboard-polis-imx8mn-2.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MM/BSP-Yocto-NXP-i.MX8MM-PD23.1.0/images/ampliphy-vendor/phyboard-polis-imx8mn-2/imx-boot-tools/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mm
.. _`static-pdf-dl`: ../../../_static/imx8mn-head.pdf

.. IMX8(MN) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mn/phycore-imx8mn.c?h=v2022.04_2.2.2-phy5#n66


.. General Replacements
.. |doc-id| replace:: L-1002e.Ax
.. |kit| replace:: **phyCORE-i.MX8M Nano Kit**
.. |kit-ram-size| replace:: 1GiB
.. |mcore| replace:: M4 Core
.. |sbc| replace:: phyBOARD-Polis
.. |soc| replace:: i.MX 8M Nano
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-i.MX8MN
.. |debug-uart| replace:: ttymxc2
.. |serial-uart| replace:: ttymxc0
.. |bluetooth-uart| replace:: UART2


.. Linux Kernel
.. |kernel-defconfig| replace:: imx_v8_defconfig imx8_phytec_distro.config imx8_phytec_platform.config
.. |kernel-recipe-path| replace:: meta-phytec/dynamic-layers/freescale-layer/recipes-kernel/linux/linux-imx_*.bb
.. |kernel-repo-name| replace:: linux-imx
.. |kernel-repo-url| replace:: git://git.phytec.de/linux-imx
.. |kernel-socname| replace:: imx8mn
.. |kernel-tag| replace:: v5.15.71_2.2.2-phy3
.. |emmcdev| replace:: mmcblk2

.. Bootloader
.. |u-boot-offset| replace:: 32
.. |u-boot-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-defconfig| replace:: phycore-imx8mn_defconfig
.. |u-boot-emmc-devno| replace:: 2
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://git.phytec.de/u-boot-imx

.. IMX8(MN) specific
.. |u-boot-socname-config| replace:: IMX8MN
.. |u-boot-tag| replace:: v2022.04_2.2.2-phy5


.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM


.. Devicetree
.. |dt-carrierboard| replace:: imx8mn-phyboard-polis
.. |dt-som| replace:: imx8mn-phycore-som
.. |dtbo-peb-av-10| replace:: imx8mn-phyboard-polis-peb-av-010.dtbo

.. IMX8(MN) specific
.. |dt-somnetwork| replace:: :imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n50`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`kirkstone`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MM
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: kirkstone
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-headless-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: phyboard-polis-imx8mn-2
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX8MM-PD23.1.0
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX8MM-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-NXP-i.MX8MM-PD23.1.y
.. |yocto-ref-manual| replace:: Yocto Reference Manual (kirkstone)
.. _yocto-ref-manual: https://phytec.github.io/doc-bsp-yocto/yocto/manual-index.html#kirkstone
.. _yocto-ref-manual-kernel-and-bootloader-config: https://phytec.github.io/doc-bsp-yocto/yocto/kirkstone.html#kernel-and-bootloader-configuration
.. |yocto-sdk-rev| replace:: 4.0.13
.. |yocto-sdk-a-core| replace:: cortexa53-crypto

.. Refs
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <imx8mn-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mn-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X30) <imx8mn-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mn-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mn-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mn-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mn-head-development>`
.. |ref-usb-otg| replace:: :ref:`X2 <imx8mn-head-components>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <imx8mn-head-format-sd>`


.. IMX8(MN) specific replacements
.. |sbc-network| replace:: \
.. |pollux-fan-note| replace:: Only GPIO fan supported.
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mn-head-ubootexternalenv>`

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
Compatible BSPs  BSP Release Type BSP Release  Date BSP Status

================ ================ ================= ==========
..
================ ================ ================= ==========

.. include:: ../../intro.rsti

Supported Hardware
------------------

The |sbc| populated with the |soc| SoC is supported.

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname| `download <dlpage-bsp_>`_.
If you choose a specific **Machine Name** in the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware

.. _imx8mn-head-components:
.. include:: ../imx8mm/components.rsti

.. +---------------------------------------------------------------------------+
..                          Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mn-head-getting-started:
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
* **bl31-imx8mn.bin**: ARM Trusted Firmware binary
* **lpddr4_pmu_train_2d_dmem_202006.bin,
  lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
* **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
  Trusted Firmware and DDR firmware. This is the final bootloader image which is
  bootable.
* **Image**: Linux kernel image
* **Image.config**: Kernel configuration
* **imx8mn-phyboard-polis*.dtb**: Kernel device tree file
* **imx8mn-phy*.dtbo**: Kernel device tree overlay files
* **phytec-headless-image\*.tar.gz**: Root file system
* **phytec-headless-image\*.rootfs.wic.xz**: compressed SD card image

.. +---------------------------------------------------------------------------+
..                          INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S1)
--------------------

The |sbc| features a boot switch with six individually switchable ports to
select the phyCORE-|soc| default bootsource.

.. _imx8mn-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
..                                DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mn-head-development:

Development
===========

.. include:: /bsp/imx-common/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot.rsti

.. include:: /bsp/imx-common/development/uuu.rsti

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti
.. include:: /bsp/imx-common/development/standalone_build_u-boot_binman.rsti
   :end-before: .. build-uboot-fixed-ram-size-marker

.. include:: /bsp/imx-common/development/standalone_build_kernel.rsti

.. include:: /bsp/imx8/development/development_manifests.rsti

.. include:: /bsp/imx8/development/upstream_manifest.rsti

.. _imx8mn-head-format-sd:

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
..                               DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mn-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::

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

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART1 device in
|dt-carrierboard|.dts:

.. code-block::

   pinctrl_uart1: uart1grp {
           fsl,pins = <
                   MX8MN_IOMUXC_SAI2_RXFS_UART1_DCE_TX     0x00
                   MX8MN_IOMUXC_SAI2_RXC_UART1_DCE_RX      0x00
                   MX8MN_IOMUXC_SAI2_RXD0_UART1_DCE_RTS_B  0x00
                   MX8MN_IOMUXC_SAI2_TXFS_UART1_DCE_CTS_B  0x00
           >;
   };

The first part of the string MX8MN_IOMUXC_SAI2_RXFS_UART1_DCE_TX names the pad
(in this example SAI2_RXFS). The second part of the string (UART1_DCE_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the right)
defines different modes of the pad, for example, if internal pull resistors are
activated or not. In this case, the internal resistors are disabled.

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
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n220`

.. _imx8mn-head-network:

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
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n301`

DT configuration for the eMMC interface can be found here:
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n309`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/imx-common/emmc.rsti

.. include:: ../peripherals/spi-master.rsti

The definition of the SPI master node in the device tree can be found here:

:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n78`

.. include:: ../peripherals/gpios.rsti

Pinmuxing of some GPIO pins in the device tree |dt-carrierboard|.dts:

.. code-block::

   pinctrl_leds: leds1grp {
           fsl,pins = <
                   MX8MN_IOMUXC_GPIO1_IO01_GPIO1_IO1       0x16
                   MX8MN_IOMUXC_GPIO1_IO14_GPIO1_IO14      0x16
                   MX8MN_IOMUXC_GPIO1_IO15_GPIO1_IO15      0x16
           >;
   };

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n45`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C1 bus configuration (e.g. |dt-som|.dtsi):
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n106`

General I²C3 bus configuration (e.g. |dt-carrierboard|.dts):
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n196`


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
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n259`

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:imx-dt:`imx8mn-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n267`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed up to 480 Mbps (HighSpeed
'HS').

The |soc| SoC has a single USB controller core that is set to OTG mode.
To use the micro USB / OTG port dip switch S1 Pos5 has to be set to on.

.. include:: /bsp/peripherals/usb-host.rsti

.. include:: /bsp/peripherals/usb-otg.rsti

The USB interface is configured as host in the kernel device tree
|dt-carrierboard|.dts. See:
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n264`

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

   On phyBOARD-Polis-i.MX8MN a terminating resistor can be enabled by setting
   S5 to ON if required.

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
:imx-dt:`imx8mn-phyboard-polis.dts?h=v5.15.71_2.2.2-phy3#n125`

.. include:: ../peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti
