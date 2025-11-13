.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-Ampliphy-AM62Lx-ALPHA2
.. |dlpage-bsp-link| replace:: |dlpage-bsp|_
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phyflex-am62lx-fpsc/#downloads/
.. |dl-server| replace:: BSP downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/
.. |dl-server-link| replace:: |dl-server|_
.. |dl-sdk| replace:: SDK downloads
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/BSP-Yocto-Ampliphy-AM62Lx-ALPHA2/sdk/ampliphy-vendor/
.. |dl-sdk-link| replace:: |dl-sdk|_
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/BSP-Yocto-Ampliphy-AM62Lx-ALPHA2/images/ampliphy-vendor/am62lxx-libra-fpsc-1/phytec-qt6demo-image-am62lxx-libra-fpsc-1.rootfs.wic.xz
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/BSP-Yocto-Ampliphy-AM62Lx-ALPHA2/images/ampliphy-vendor/am62lxx-libra-fpsc-1/phytec-qt6demo-image-am62lxx-libra-fpsc-1.rootfs.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/BSP-Yocto-Ampliphy-AM62Lx-ALPHA2/images/ampliphy-vendor/am62lxx-libra-fpsc-1/
.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-AM62Lx/BSP-Yocto-Ampliphy-AM62Lx-ALPHA2/images/ampliphy-vendor/am62lxx-libra-fpsc-1/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=am62lx
.. _`static-pdf-dl`: ../../../_static/am62l-fpsc-head.pdf

.. AM62Lx specific

.. General Substitutions
.. |doc-id| replace:: Head
.. |kit| replace:: **phyFLEX-AM62L FPSC Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: Libra FPSC
.. |soc| replace:: AM62L
.. |socfamily| replace:: AM62
.. |som| replace:: phyFLEX-|soc| FPSC
.. |debug-uart| replace:: ttyS3
.. |serial-uart| replace:: ttyS1
.. |bluetooth-uart| replace:: UART3
.. |expansion-connector| replace:: X6
.. |vendor| replace:: TI


.. Linux Kernel
.. |kernel-defconfig| replace:: phytec_ti_defconfig
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-ti_*.bb
.. |kernel-repo-name| replace:: linux-phytec-ti
.. |kernel-repo-url| replace:: https://github.com/phytec/linux-phytec-ti
.. |kernel-socname| replace:: am62l-fpsc
.. |kernel-tag| replace:: v6.12.35-11.01.05-phy
.. |emmcdev| replace:: mmcblk0
.. |led-names| replace:: led-1, led-2 and led-3
.. |led-example| replace:: led-1

.. Bootloader
.. |u-boot-defconfig| replace:: phycore_am62lx_defconfig
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-phytec-ti_*.bb
.. |u-boot-repo-name| replace:: u-boot-phytec-ti
.. |u-boot-repo-url| replace:: https://github.com/phytec/u-boot-phytec-ti
.. |emmcdev-uboot| replace:: mmc 0
.. |sdcarddev-uboot| replace:: mmc 1

.. AM62L specific
.. |u-boot-socname-config| replace:: AM62L_LIBRA
.. |u-boot-tag| replace:: 11.01.02


.. RAUC
.. |rauc-manual| replace:: L-1006e.A6 RAUC Update & Device Management Manual
.. _rauc-manual: https://www.phytec.de/cdocuments/?doc=F4DiM


.. Devicetree
.. |dt-carrierboard| replace:: k3-am62l3-libra-rdk-fpsc
.. |dt-som| replace:: k3-am62l-phyflex-fpsc

.. AM62L specific
.. |dt-somnetwork| replace:: :linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L148`
   `
.. |dt-gpio-expander| replace:: :linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L274`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`scarthgap`
.. |yocto-bsp-name| replace:: BSP-Yocto-AM62Lx-FPSC
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: scarthgap
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: rootfs.wic.xz
.. |yocto-machinename| replace:: am62lxx-libra-fpsc-1
.. |yocto-manifestname| replace:: BSP-Yocto-Ampliphy-AM62Lx-ALPHA2
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-AM62Lx-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-Ampliphy-AM62Lx-FPSC-PD25.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (scarthgap) <yocto-man-scarthgap>`
.. |yocto-ref-manual-kernel-and-bootloader-conf| replace:: :ref:`Yocto Reference Manual <yocto-man-scarthgap-kernel-and-bootloader-conf>`
.. |yocto-sdk-rev| replace::  BSP-Yocto-Ampliphy-AM62Lx-ALPHA2
.. |yocto-sdk-a-core| replace:: aarch64

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S1) <am62l-fpsc-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <am62l-fpsc-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X14) <am62l-fpsc-head-components>`
.. |ref-dt| replace:: :ref:`device tree <am62l-fpsc-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <am62l-fpsc-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <am62l-fpsc-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <am62l-fpsc-head-development>`
.. |ref-usb-otg| replace:: :ref:`X18 <am62l-fpsc-head-components>`
.. |ref-build-uboot| replace:: :ref:`Build U-Boot <am62l-fpsc-head-development-build-uboot>`
.. |ref-format-sd| replace:: :ref:`Resizing ext4 Root Filesystem  <am62l-fpsc-head-format-sd>`


.. AM62L specific
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found here:
   :linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L213`.

.. |ref-serial| replace:: :ref:`X27 <am62l-fpsc-head-components>`
.. |ref-S5| replace:: :ref:`S5 <am62l-fpsc-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <am62l-fpsc-head-ubootexternalenv>`
.. |weston-hdmi-mode| replace:: preferred
.. |eeprom-detect-bus| replace:: 1
.. |eeprom-detect-addr| replace:: 0x50
.. |eeprom-som-detect-area| replace:: 1024
.. |eeprom-som-detect-area-hex| replace:: 0x400


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
| Yocto Manual          | Scarthgap            |
+-----------------------+----------------------+
| Release Date          | XXXX/XX/XX           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| FPSC  |
|                       | BSP Manual Head      |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

================================= ================ ================= ==============
Compatible BSPs                   BSP Release Type BSP Release  Date BSP Status

================================= ================ ================= ==============
BSP-Yocto-Ampliphy-AM62Lx-ALPHA2  Alpha            2025/07/10        Released
================================= ================ ================= ==============


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

.. _am62l-fpsc-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _am62l-fpsc-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

.. image:: images/SD_Card_Boot.png

*  Insert the SD card
*  Connect the target and the host with **USB-C** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti
   :end-before: .. nxp-eula-marker
.. include:: /bsp/building-bsp.rsti
   :start-after: .. nxp-eula-marker

.. _am62l-fpsc-head-images:

*  **u-boot.img**: U-Boot bootloader image
*  **oftree**: Default kernel device tree
*  **ti-boot3.bin**: First stage bootloader (R5 SPL)
*  **tispl.bin**: Secondary program loader (SPL)
*  **bl1.bin**: ARM Trusted Firmware binary
*  **bl31.bin**: ARM Trusted Firmware binary
*  **fitImage**: Linux kernel FIT image
*  **fitImage-its\*.its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **k3-am62l32-libra-fpsc*.dtb**: Kernel device tree file
*  **phytec-qt6demo-image\*.tar.gz**: Root file system
*  **phytec-qt6demo-image\*.rootfs.wic.xz**: compressed SD card image

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

.. _am62l-fpsc-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: /bsp/ti-common/installing-os.rsti
   :end-before: .. rauc-marker

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _am62l-fpsc-head-development:

Development
===========

.. include:: /bsp/ti-common/development/standalone_build_preface.rsti

.. warning::
   Using the SDK on older host distributions (e.g., Ubuntu 20.04 LTS) with Scarthgap TI-based BSPs
   can cause issues when building U-Boot or Linux kernel tools for host use. If you encounter an
   "undefined reference" error, a workaround is to prepend the host's binutils to the PATH.

   .. code-block:: console

      host$ export PATH=/usr/bin:$PATH

   Run this after sourcing the SDK *environment-setup* file.

   Note, SDK issue has not been observed on newer distributions, such as Ubuntu 22.04, which appear to work
   without requiring any modifications.

.. _am62l-fpsc-head-development-build-uboot:
.. include:: /bsp/ti-common/development/standalone_build_u-boot_binman.rsti
   :end-before: .. get-binaries-marker

Get the needed binaries
.......................

To build the bootloader, you need to **copy** these **files** to your |u-boot-repo-name|
**build directory** and rename them to fit with *mkimage* script:

*  **ARM Trusted firmware binaries**:
      * bl1.bin
      * bl31.bin
      * binary blobs

If you already built our BSP with Yocto, you can get the
bl1.bin, bl31.bin and binary blobs from the directory mentioned
here: |ref-bsp-images|

Or you can download the files here: |link-boot-tools|

.. warning::

   Make sure you rename the files you need so that they are compatible with the
   *mkimage tool*.

Build the bootloader
....................

Build tiboot3.bin, tispl.bin and u-boot.img:

   .. code-block:: console
      :substitutions:

      host:~/|u-boot-repo-name|$ make |u-boot-defconfig|
      host:~/|u-boot-repo-name|$ make BL1=/path/to/bl1.bin BL31=/path/to/bl31.bin BINMAN_INDIRS=/path/to/binary_blobs

.. include:: /bsp/ti-common/development/standalone_build_u-boot_binman.rsti
   :start-after: .. get-binaries-marker
   :end-before: .. build-uboot-fixed-ram-size-marker
.. include:: /bsp/ti-common/development/standalone_build_kernel.rsti

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/ti-common/development/netboot.rsti

.. include:: /bsp/development/development_manifests.rsti

.. include:: /bsp/development/master_manifest.rsti

.. _am62l-fpsc-head-format-sd:

.. include:: /bsp/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _am62l-fpsc-head-device-tree:
.. include:: /bsp/device-tree.rsti

.. code-block::
   :substitutions:

   k3-am62l3-libra-fpsc-lvds-ac209.dtbo

.. _am62l-fpsc-head-ubootexternalenv:
.. include:: /bsp/dt-overlays.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART0 device in
|dt-carrierboard|.dtsi:

.. code-block::

   main_uart0_pins_default: main-uart0-default-pins {
      pinctrl-single,pins = <
         AM62LX_IOPAD(0x01b4, PIN_INPUT, 0)      /* (D13) UART0_RXD */
         AM62LX_IOPAD(0x01b8, PIN_OUTPUT, 0)     /* (C13) UART0_TXD */
      >;
      bootph-all;
   };

The first argument of the macro AM62LX_IOPAD(pa, val, muxmode) is the pad offset
address within the I/O controller (in this example 0x1b4, corresponding UART0_RXD).
The second argument (val) specifies the pad configuration, such as input/output
and pull-up/pull-down. Third argument (muxmode) selects the functional mux mode
for the pad, i.e. which peripheral signal is connected to it. In this case, 0
corresponds to the default mux option for UART0.

The device tree representation for UART0 pinmuxing:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L150`

RS232
-----

The FPSC Standard supports 3 UART units. On the |sbc|, TTL level signals
of UART0 (the standard console) and WKUP_UART0 are routed to a FT4232H UART
to USB converter expansion. This USB is brought out at USB-C connector X14.
UART4 is connected to a multi-protocol transceiver for RS-232 and RS-485,
available at pin header connector |ref-serial| at the RS-232 level,
or at the RS-485 level. The muxing of the used transceivers is done by switch
|ref-S5| on the baseboard.
For more information about the correct setup please refer to the |som|/|sbc|
Hardware Manual section UARTs. The switch |ref-S5| need to be set correctly.

*  Display the current settings of a terminal in a human-readable format:

   .. code-block:: console

      target:~$ stty -a

*  With a simple echo and cat, basic communication can be tested. Example:

   .. code-block:: console
      :substitutions:

      target:~$ echo 123 > /dev/|serial-uart|

   .. code-block:: console

      host:~$ cat /dev/ttyUSB2


The device tree representation for RS232:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L327`

.. _am62l-fpsc-head-network:

Network
-------

|sbc|-|soc| provides two ethernet interfaces. A gigabit Ethernet is provided by our
module and board.

.. warning::

   The naming convention of the Ethernet interfaces in the hardware (ETH0
   and ETH1) do not align with the network interfaces (end0 and end1) in
   Linux. So, be aware of these differences:

   | ETH1 = end0
   | ETH0 = end1

.. include:: /bsp/peripherals/network.rsti
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

.. include:: /bsp/peripherals/network.rsti
   :start-after: .. kernel-network-environment-marker

.. include:: /bsp/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L272`
and
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L355`

DT configuration for the e.MMC interface can be found here:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L263`

.. include:: emmc.rsti

.. include:: ../peripherals/spi-master.rsti
  :end-before: .. peripherals-spi-nor-flash-marker

.. include:: ../peripherals/spi-nor-flash-no-boot.rsti
   :end-before: .. code-block-mtdinfo-all-marker

.. code-block:: console
   :substitutions:

   root@|yocto-machinename|:~$ mtdinfo --all
   Count of MTD devices:           5
   Present MTD devices:            mtd0, mtd1, mtd2, mtd3, mtd4
   Sysfs interface supported:      yes

   mtd0
   Name:                           ospi.tiboot3
   Type:                           nor
   Eraseblock size:                131072 bytes, 128.0 KiB
   Amount of eraseblocks:          4 (524288 bytes, 512.0 KiB)
   Minimum input/output unit size: 1 byte
   Sub-page size:                  1 byte
   Character device major/minor:   90:0
   Bad blocks are allowed:         false
   Device is writable:             true

   mtd1
   Name:                           ospi.tispl
   Type:                           nor
   Eraseblock size:                131072 bytes, 128.0 KiB
   Amount of eraseblocks:          16 (2097152 bytes, 2.0 MiB)
   Minimum input/output unit size: 1 byte
   Sub-page size:                  1 byte
   Character device major/minor:   90:2
   Bad blocks are allowed:         false
   Device is writable:             true

   mtd2
   Name:                           ospi.u-boot
   Type:                           nor
   Eraseblock size:                131072 bytes, 128.0 KiB
   Amount of eraseblocks:          32 (4194304 bytes, 4.0 MiB)
   Minimum input/output unit size: 1 byte
   Sub-page size:                  1 byte
   Character device major/minor:   90:4
   Bad blocks are allowed:         false
   Device is writable:             true

   mtd3
   Name:                           ospi.env
   Type:                           nor
   Eraseblock size:                131072 bytes, 128.0 KiB
   Amount of eraseblocks:          2 (262144 bytes, 256.0 KiB)
   Minimum input/output unit size: 1 byte
   Sub-page size:                  1 byte
   Character device major/minor:   90:6
   Bad blocks are allowed:         false
   Device is writable:             true

   mtd4
   Name:                           ospi.env.backup
   Type:                           nor
   Eraseblock size:                131072 bytes, 128.0 KiB
   Amount of eraseblocks:          2 (262144 bytes, 256.0 KiB)
   Minimum input/output unit size: 1 byte
   Sub-page size:                  1 byte
   Character device major/minor:   90:8
   Bad blocks are allowed:         false
   Device is writable:             true

.. include:: ../peripherals/spi-nor-flash-no-boot.rsti
   :start-after:  .. code-block-mtdinfo-all-marker

The definition of the SPI master node in the device tree can be found here:

:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L335`

.. include:: gpios.rsti

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L251`

.. include:: /bsp/peripherals/i2c-bus.rsti

General I²C bus configuration from SoM (e.g. |dt-som|.dtsi):
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L172`

General I²C bus configuration from carrierboard (e.g. |dt-carrierboard|.dts)
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L233`

EEPROM
------

The system features two I2C EEPROM devices distributed across the SoM and
carrier board:

On the |som| SoM:

*  Board Detection EEPROM

   *  Bus: I2C-1
   *  Address: 0x50
   *  Purpose: Factory configuration for board identification

Device Tree Reference for SoM EEPROMs:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L249`

And on the |sbc| carrier board:

*  Board Detection EEPROM

   *  Bus: I2C-2
   *  Address: 0x51
   *  Purpose: Reserved for carrier board identification

Device Tree Reference for Carrier Board:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L238`

.. include:: /bsp/peripherals/eeprom.rsti

.. include:: /bsp/peripherals/rtc.rsti

DT representation for I²C RTCs:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l-phycore-fpsc.dtsi#L257`


And the addions on the carrierboard:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L228`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed of up to 480 Mbit/s (High-Speed
'HS'). The USB subsystem has two independent USB controller cores. Both cores
are capable of acting as a USB peripheral device or a USB host. Each is
connected to a USB 2.0 PHY.

.. include:: /bsp/peripherals/usb-host.rsti

DT representation for USB Host:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L382`

CAN FD
------

The |sbc| has two CAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. note::

   The switches S6 and S7 are switching the 120 Ohm bus termination resistors.
   For proper functionality of the CAN FD interface, the bus needs to be
   terminated. If no external bus termination resistors are mounted, the
   switches S6 (for CAN FD1) and S7 (for CAN FD2) need to be set to ON.

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-rdk-fpsc.dts#L306`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/peripherals/display.rsti

Device tree description of LVDS-0 can be found here:
:linux-phytec-ti:`tree/v6.12.35-11.01.05-phy/arch/arm64/boot/dts/ti/k3-am62l3-libra-fpsc-lvds-ac209.dtso#L16`

.. include:: /bsp/am6x/peripherals/pm.rsti

.. include:: /bsp/peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti
