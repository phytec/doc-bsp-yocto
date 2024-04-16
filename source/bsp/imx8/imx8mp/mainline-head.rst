.. Download links
.. |dlpage-bsp| replace:: our BSP
.. _dlpage-bsp: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX8MP-PD23.1.0
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-8m-plus/#downloads
.. _dl-server: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/
.. _dl-sdk: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD23.1.0/sdk/ampliphy-vendor-xwayland/
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/phytec-qt6demo-image-phyboard-pollux-imx8mp-3.wic
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/phytec-qt6demo-image-phyboard-pollux-imx8mp-3.partup
.. |link-boot-tools| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX8MP/BSP-Yocto-NXP-i.MX8MP-PD23.1.0/images/ampliphy-vendor-xwayland/phyboard-pollux-imx8mp-3/imx-boot-tools/
.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx8mp

.. IMX8(MP) specific
.. _overlaycallback: https://git.phytec.de/u-boot-imx/tree/board/phytec/phycore_imx8mp/phycore-imx8mp.c?h=v2022.04_2.2.2-phy5#n149


.. General Substitutions
.. |doc-id| replace:: PD24.1.y BSP Manual
.. |kit| replace:: **phyCORE-i.MX8M Plus Kit**
.. |kit-ram-size| replace:: 2GiB
.. |sbc| replace:: phyBOARD-Pollux
.. |soc| replace:: i.MX 8M Plus
.. |socfamily| replace:: i.MX 8
.. |som| replace:: phyCORE-i.MX8MP
.. |debug-uart| replace:: ttymxc0
.. |serial-uart| replace:: ttymxc1
.. |expansion-connector| replace:: X6


.. Linux Kernel
.. |kernel-socname| replace:: imx8mp
.. |kernel-tag| replace:: v6.6-y
.. |emmcdev| replace:: mmcblk2

.. Bootloader
.. |u-boot-offset| replace:: 32
.. |u-boot-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 2

.. IMX8(MP) specific
.. |u-boot-socname-config| replace:: IMX8MP
.. |u-boot-tag| replace:: v2024.01-y


.. Devicetree
.. |dt-carrierboard| replace:: imx8mp-phyboard-pollux-rdk
.. |dt-som| replace:: imx8mp-phycore-som
.. |dtbo-rpmsg| replace:: imx8mp-phycore-rpmsg.dtbo

.. IMX8(MP) specific
.. |dt-somnetwork| replace:: :imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n50`

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`kirkstone`
.. |yocto-bsp-name| replace:: BSP-Yocto-IMX8MP
.. _yocto-bsp-name: `dl-server`_
.. |yocto-codename| replace:: master
.. |yocto-distro| replace:: ampliphy-xwayland
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: wic
.. |yocto-machinename| replace:: phyboard-pollux-imx8mp-3
.. |yocto-manifestname| replace:: BSP-Yocto-i.MX8MP-PD24.1.0
.. |yocto-manifestname-master| replace:: BSP-Yocto-Ampliphy-i.MX8MP-master
.. |yocto-manifestname-y| replace:: BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.y
.. |yocto-ref-manual| replace:: Yocto Reference Manual (master)
.. _yocto-ref-manual: https://phytec.github.io/doc-bsp-yocto/yocto/manual-index.html#kirkstone
.. _yocto-ref-manual-kernel-and-bootloader-config: https://phytec.github.io/doc-bsp-yocto/yocto/scarthgap.html#kernel-and-bootloader-configuration

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S3) <imx8mp-mainline-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx8mp-mainline-head-images>`
.. |ref-debugusbconnector| replace:: :ref:`(X1) <imx8mp-mainline-head-components>`
.. |ref-dt| replace:: :ref:`device tree <imx8mp-mainline-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx8mp-mainline-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx8mp-mainline-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx8mp-mainline-head-development>`
.. |ref-usb-otg| replace:: :ref:`X5 (upper connector) <imx8mp-mainline-head-components>`
.. |ref-disable-emmc-part| replace:: :ref:`Disable booting from eMMC boot partitions <emmc-disable-boot-part>`


.. IMX8(MP) specific
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   on the |sbc| can be found here:
   :imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n150`.
.. |pollux-fan-note| replace::
   Starting with BSP-Yocto-i.MX8MP-PD22.1.1 we have to switch from PWM fan
   to GPIO fan due to availability. The PWM fan will not be supported
   anymore and will not function with the new release.

.. |ref-serial| replace:: :ref:`X2 <imx8mp-head-components>`
.. |ref-jp3| replace:: :ref:`JP3 <imx8mp-head-components>`
.. |ref-jp4| replace:: :ref:`JP4 <imx8mp-head-components>`
.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx8mp-head-ubootexternalenv>`


.. M-Core specific
.. |mcore| replace:: M7 Core
.. |mcore-zephyr-docs| replace:: https://docs.zephyrproject.org/latest/boards/phytec/mimx8mp_phyboard_pollux/doc/index.html
.. |mcore-jtag-dev| replace:: MIMX8MM6_M4
.. |mcore-sdk-version| replace:: 2.13.0

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
| Release Date          | 2024/04/XX           |
+-----------------------+----------------------+
| Is Branch of          | |doc-id| |soc| BSP   |
|                       | Manual Head          |
+-----------------------+----------------------+

The table below shows the Compatible BSPs for this manual:

================ ================ ================= ==============
Compatible BSP'S BSP Release Type BSP Release  Date BSP Status

================ ================ ================= ==============
PD24.1.0         Major            2024/04/xx        in development
================ ================ ================= ==============


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

.. _imx8mp-mainline-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx8mp-mainline-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the following
   position:

.. image:: images/SD_Card_Boot.png

*  Insert the SD card
*  Connect the target and the host with **mirco USB** on |ref-debugusbconnector|
   debug USB
*  Power up the board

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx8mp-mainline-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx8mp.bin**: ARM Trusted Firmware binary
*  **lpddr4_pmu_train_1d_dmem_202006.bin,
   lpddr4_pmu_train_1d_imem_202006.bin,
   lpddr4_pmu_train_2d_dmem_202006.bin,
   lpddr4_pmu_train_2d_imem_202006.bin**: DDR PHY firmware images
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx8mp-phyboard-pollux-rdk*.dtb**: Kernel device tree file
*  **phytec-qt6demo-image\*.tar.gz**: Root file system
*  **phytec-qt6demo-image\*.wic**: SD card image

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

.. _imx8mp-mainline-head-bootswitch:
.. include:: bootmode-switch.rsti

Flash eMMC
----------

To boot from eMMC, make sure that the BSP image is flashed correctly to the eMMC
and the |ref-bootswitch| is set to **eMMC**.

.. warning::
   When eMMC and SD card are flashed with the same (identical) image, the UUIDs
   of the boot partitions are also identical. If the SD card is connected when
   booting, this leads to non-deterministic behavior as Linux mounts the boot
   partition based on UUID.

   .. code-block:: console

      target:~$ blkid

   can be run to inspect whether the current setup is affected. If ``mmcblk2p1``
   and ``mmcblk1p1`` have an identical UUID, the setup is affected.

Flash eMMC from Network
.......................

|soc| boards have an Ethernet connector and can be updated over a network. Be
sure to set up the development host correctly. The IP needs to be set to
192.168.3.10, the netmask to 255.255.255.0, and a TFTP server needs to be
available. From a high-level point of view, an eMMC device is like an SD card.
Therefore, it is possible to flash the **WIC image** (``<name>.wic``) from
the Yocto build system directly to the eMMC. The image contains the
bootloader, kernel, device tree, device tree overlays, and root file system.

Flash eMMC from Network in U-Boot on Target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These steps will show how to update the eMMC via a network.

.. tip::

   A working network is necessary! |ref-setup-network-host|

*  Load your image via network to RAM:

   .. code-block::
      :substitutions:

      u-boot=> dhcp ${loadaddr} |yocto-imagename|-|yocto-machinename|.wic
      BOOTP broadcast 1
      DHCP client bound to address 192.168.3.11 (101 ms)
      Using ethernet@30be0000 device
      TFTP from server 192.168.3.10; our IP address is 192.168.3.11
      Filename '|yocto-imagename|-|yocto-machinename|.wic'.
      Load address: 0x40480000
      Loading: ######################################
               ######################################
               ######################################
               ...
               ...
               ...
               ######################################
               #############
               11.2 MiB/s
      done
      Bytes transferred = 911842304 (36599c00 hex)

*  Write the image to the eMMC:

   .. code-block::

      u-boot=> mmc dev 2
      switch to partitions #0, OK
      mmc2(part 0) is current device
      u-boot=> setexpr nblk ${filesize} / 0x200
      u-boot=> mmc write ${loadaddr} 0x0 ${nblk}

      MMC write: dev # 2, block # 0, count 1780942 ... 1780942 blocks written: OK

Flash eMMC via Network in Linux on Target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can update the eMMC from your target.

.. tip::

   A working network is necessary! |ref-setup-network-host|

Take a compressed or uncompressed image on the host and send it with ssh through
the network (then uncompress it, if necessary) to the eMMC of the target with a
one-line command:

.. code-block:: console
   :substitutions:

   target:~$ ssh <USER>@192.168.3.10 "dd if=<path_to_file>/|yocto-imagename|-|yocto-machinename|.wic" | dd of=/dev/mmcblk2 conv=fsync

Flash eMMC via Network in Linux on Host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to install the OS at eMMC from your Linux host. As before,
you need a complete image on your host.

.. tip::

   A working network is necessary! |ref-setup-network-host|

Show your available image files on the host:

.. code-block:: console
   :substitutions:

   host:~$ ls
   |yocto-imagename|-|yocto-machinename|.wic

Send the image with the ``dd`` command combined with ssh through the network
to the eMMC of your device:

.. code-block:: console
   :substitutions:

   host:~$ dd if=|yocto-imagename|-|yocto-machinename|.wic status=progress | ssh root@192.168.3.11 "dd of=/dev/mmcblk2 conv=fsync"

Flash eMMC U-Boot image via Network from running U-Boot
.......................................................

Update the standalone U-Boot image imx-boot is also possible from U-Boot. This
can be used if the bootloader on eMMC is located in the eMMC user area.

.. tip::

   A working network is necessary! |ref-setup-network-host|

Load image over tftp into RAM and then write it to eMMC:

.. code-block::
   :substitutions:

   u-boot=> dhcp ${loadaddr} imx-boot
   u-boot=> setexpr nblk ${filesize} / 0x200
   u-boot=> mmc dev 2
   u-boot=> mmc write ${loadaddr} |u-boot-mmc-flash-offset| ${nblk}

.. hint::
   The hexadecimal value represents the offset as a multiple of 512 byte
   blocks. See the `offset table <#offset-table>`__ for the correct value
   of the corresponding SoC.

Flash eMMC from USB
...................

Flash eMMC from USB in U-Boot on Target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   This step only works if the size of the image file is less than 1GB due to
   limited usage of RAM size in the Bootloader after enabling OPTEE.

These steps will show how to update the eMMC via a USB device. Configure the
|ref-bootswitch| to SD Card and insert an SD card. Power on the board and stop
in U-Boot prompt. Insert a USB device with the copied WIC image to the USB slot.

Load your image from the USB device to RAM:

.. code-block::

   u-boot=> usb start
   starting USB...
   USB0:   USB EHCI 1.00
   scanning bus 0 for devices... 2 USB Device(s) found
          scanning usb for storage devices... 1 Storage Device(s) found
   u-boot=> fatload usb 0:1 ${loadaddr} *.wic
   497444864 bytes read in 31577 ms (15 MiB/s)

Write the image to the eMMC:

.. code-block::

   u-boot=> mmc dev 2
   switch to partitions #0, OK
   mmc2(part 0) is current device
   u-boot=> setexpr nblk ${filesize} / 0x200
   u-boot=> mmc write ${loadaddr} 0x0 ${nblk}

   MMC write: dev # 2, block # 0, count 1024000 ... 1024000 blocks written: OK
   u-boot=> boot

Flash eMMC from USB in Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These steps will show how to flash the eMMC on Linux with a USB stick. You only
need a complete image saved on the USB stick and a bootable WIC image. (e.g.
|yocto-imagename|-|yocto-machinename|.wic). Set the |ref-bootswitch| to SD Card.

*  Insert and mount the USB stick:

   .. code-block:: console

      [   60.458908] usb-storage 1-1.1:1.0: USB Mass Storage device detected
      [   60.467286] scsi host0: usb-storage 1-1.1:1.0
      [   61.504607] scsi 0:0:0:0: Direct-Access                               8.07 PQ: 0 ANSI: 2
      [   61.515283] sd 0:0:0:0: [sda] 3782656 512-byte logical blocks: (1.94 GB/1.80 GiB)
      [   61.523285] sd 0:0:0:0: [sda] Write Protect is off
      [   61.528509] sd 0:0:0:0: [sda] No Caching mode page found
      [   61.533889] sd 0:0:0:0: [sda] Assuming drive cache: write through
      [   61.665969]  sda: sda1
      [   61.672284] sd 0:0:0:0: [sda] Attached SCSI removable disk
      target:~$ mount /dev/sda1 /mnt

*  Now show your saved image files on the USB Stick:

   .. code-block:: console
      :substitutions:

      target:~$ cd /mnt
      target:~$ ls
      |yocto-imagename|-|yocto-machinename|.wic

*  Show list of available MMC devices:

   .. code-block:: console

      target:~$ ls /dev | grep mmc
      mmcblk1
      mmcblk1p1
      mmcblk1p2
      mmcblk2
      mmcblk2boot0
      mmcblk2boot1
      mmcblk2p1
      mmcblk2p2
      mmcblk2rpmb

*  The eMMC device can be recognized by the fact that it contains two boot
   partitions: (mmcblk2boot0; mmcblk2boot1)
*  Write the image to the phyCORE-|soc| eMMC (MMC device 2 without partition):

   .. code-block:: console
      :substitutions:

      target:~$ dd if=|yocto-imagename|-|yocto-machinename|.wic of=/dev/mmcblk2 conv=fsync

*  After a complete write, your board can boot from eMMC.

   .. tip::

      Before this will work, you need to configure the |ref-bootswitch| to
      **eMMC**.

Flash eMMC from SD Card
.......................

Even if there is no network available, you can update the eMMC. For that, you
only need a ready-to-use image file (``*.wic``) located on the SD card.
Because the image file is quite large, you have to enlarge your SD card to use
its full space (if it was not enlarged before). To enlarge your SD card, see
Resizing ext4 Root Filesystem.

Alternatively, flash a partup package to the SD card, as described in
|ref-getting-started|. This will ensure the full space of the SD card is used.

Flash eMMC from SD card in U-Boot on Target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   This step only works if the size of the image file is less than 1GB due to
   limited usage of RAM size in the Bootloader after enabling OPTEE. If the
   image file is too large use the `Updating eMMC from SD card in
   Linux on Target` subsection.

*  Flash an SD card with a working image and create a third FAT partition. Copy
   the WIC image (for example |yocto-imagename|.wic) to this
   partition.
*  Configure the |ref-bootswitch| to SD Card and insert the SD Card.
*  Power on the board and stop in U-Boot.
*  Load the image:

   .. code-block::
      :substitutions:

      u-boot=> fatload mmc 1:3 ${loadaddr} |yocto-imagename|-|yocto-machinename|.wic
      reading
      911842304 bytes read in 39253 ms (22.2 MiB/s)

*  Switch the mmc dev to eMMC:

   .. code-block::

      u-boot=> mmc list
      FSL_SDHC: 1 (SD)
      FSL_SDHC: 2 (eMMC)
      u-boot=> mmc dev 2
      switch to partitions #0, OK
      mmc2(part 0) is current device

*  Flash your WIC image (for example |yocto-imagename|.wic)
   from the SD card to eMMC. This will partition the card and copy imx-boot,
   Image, dtb, dtbo, and root file system to eMMC.

   .. code-block::

      u-boot=> setexpr nblk ${filesize} / 0x200
      u-boot=> mmc write ${loadaddr} 0x0 ${nblk}

      MMC write: dev # 2, block # 0, count 1780942 ... 1780942 blocks written: OK

*  Power off the board and change the |ref-bootswitch| to eMMC.

Flash eMMC from SD card in Linux on Target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also flash the eMMC on Linux. You only need a partup package or WIC
image saved on the SD card.

*  Show your saved partup package or WIC image files on the SD card:

   .. code-block:: console
      :substitutions:

      target:~$ ls
      |yocto-imagename|-|yocto-machinename|.partup
      |yocto-imagename|-|yocto-machinename|.wic

*  Show list of available MMC devices:

   .. code-block:: console

      target:~$ ls /dev | grep mmc
      mmcblk1
      mmcblk1p1
      mmcblk1p2
      mmcblk2
      mmcblk2boot0
      mmcblk2boot1
      mmcblk2p1
      mmcblk2p2
      mmcblk2rpmb

*  The eMMC device can be recognized by the fact that it contains two boot
   partitions: (mmcblk2\ **boot0**; mmcblk2\ **boot1**)
*  Write the image to the phyCORE-|soc| eMMC (MMC device 2 **without**
   partition) using `partup`_:

   .. code-block:: console
      :substitutions:

      target:~$ partup install |yocto-imagename|-|yocto-machinename|.partup /dev/mmcblk2

   Flashing the partup package has the advantage of using the full capacity of
   the eMMC device, adjusting partitions accordingly.

   .. note::

      Alternatively, ``dd`` may be used instead:

      .. code-block:: console
         :substitutions:

         target:~$ dd if=|yocto-imagename|-|yocto-machinename|.wic of=/dev/mmcblk2 conv=fsync

      Keep in mind that the root partition does not make use of the full space when
      flashing with ``dd``.

*  After a complete write, your board can boot from eMMC.

   .. warning::

      Before this will work, you need to configure the |ref-bootswitch| to eMMC.

RAUC
----

The RAUC (Robust Auto-Update Controller) mechanism support has been added to
meta-ampliphy. It controls the procedure of updating a device with new firmware.
This includes updating the Linux kernel, Device Tree, and root filesystem.
PHYTEC has written an online manual on how we have intergraded RAUC into our
BSPs: `L-1006e.A5 RAUC Update & Device Management Manual
<https://www.phytec.de/cdocuments/?doc=fgByJg>`__.

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx8mp-mainline-head-development:

Development
===========

.. include:: /bsp/imx-common/development/host_network_setup.rsti

Booting the Kernel from a Network
---------------------------------

Booting from a network means loading the kernel and device tree over TFTP and
the root file system over NFS. The bootloader itself must already be loaded from
another available boot device.

Place Images on Host for Netboot
................................

*  Copy the kernel image to your tftp directory:

   .. code-block:: console

      host:~$ cp Image /srv/tftp

*  Copy the devicetree to your tftp directory:

   .. code-block:: console

      host:~$ cp oftree /srv/tftp

*  Make sure other users have read access to all the files in the tftp directory,
   otherwise they are not accessible from the target:

   .. code-block:: console

      host:~$ sudo chmod -R o+r /srv/tftp

*  Extract the rootfs to your nfs directory:

   .. code-block:: console
      :substitutions:

      host:~$ sudo tar -xvzf |yocto-imagename|-|yocto-machinename|.tar.gz -C /srv/nfs

.. note::
   Make sure you extract with sudo to preserve the correct ownership.

Booting from an Embedded Board
..............................

Boot the board into the U-boot prompt and press any key to hold.

*  To boot from a network, call:

   .. code-block:: console

      u-boot=> run netboot

.. include:: /bsp/imx-common/development/uuu.rsti
.. include:: /bsp/imx8/development/development_manifests.rsti
.. standalone build needs to be reworked (maybe more generic to make this file
   reuse it)
.. include:: /bsp/imx8/development/upstream_manifest.rsti
.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx8mp-mainline-head-device-tree:
.. include:: /bsp/device-tree.rsti

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
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n536`

RS232/RS485
-----------

The phyCORE-|soc| supports up to 4 UART units. On the |sbc|, TTL level signals
of UART1 (the standard console) and UART4 are routed to Silicon Labs CP2105 UART
to USB converter expansion. This USB is brought out at Micro-USB connector X1.
UART3 is at X6 (Expansion Connector) at TTL level. UART2 is connected to a
multi-protocol transceiver for RS-232 and RS-485, available at pin header
connector |ref-serial| at the RS-232 level, or at the RS-485 level. The
configuration of the multi-protocol transceiver is done by jumpers |ref-jp3| and
|ref-jp4| on the baseboard. For more information about the correct setup please
refer to the phyCORE-|soc|/|sbc| Hardware Manual section UARTs.

We use the same device tree node for RS-232 and RS-485. RS-485 mode can be
enabled with ioctl TIOCSRS485. Also, full-duplex support is also configured
using ioctls. Have a look at our small example application rs485test, which is
also included in the BSP. The jumpers |ref-jp3| and |ref-jp4| need to be set
correctly.

.. include:: /bsp/imx8/peripherals/rs232-485.rsti

The device tree representation for RS232 and RS485:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n341`

.. _imx8mp-mainline-head-network:

Network
-------

|sbc|-|soc| provides two ethernet interfaces. A gigabit Ethernet is provided by our
module and board.

.. warning::

   The naming convention of the Ethernet interfaces in the hardware (ethernet0
   and ethernet1) do not align with the network interfaces (eth0 and eth1) in
   Linux. So, be aware of these differences:

   | ethernet1 = eth0
   | ethernet0 = eth1

.. include:: /bsp/imx-common/peripherals/network.rsti
   :end-before: .. u-boot-network-environment-marker

U-boot network-environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

* We currently use dynamic IP addresses in U-Boot. This is enabled by this variable:

   .. code-block::

      u-boot=> printenv ip_dyn
      ip_dyn=yes

*  Set up path for NFS. A modification could look like this:

   .. code-block::

      u-boot=> setenv nfsroot /home/user/nfssrc

Please note that these modifications will only affect the bootloader settings.

.. include:: /bsp/imx-common/peripherals/network.rsti
   :start-after: .. kernel-network-environment-marker

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n380`

DT configuration for the eMMC interface can be found here:
:imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n223`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: /bsp/imx-common/emmc.rsti

.. include:: ../peripherals/spi-master.rsti
   :end-before: .. peripherals-spi-nor-flash-marker

The definition of the SPI master node in the device tree can be found here:
:imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n76`

.. include:: ../peripherals/gpios.rsti

.. include:: /bsp/peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n229`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C1 bus configuration (e.g. |dt-som|.dtsi):
:imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n110`

General I²C2 bus configuration (e.g. |dt-carrierboard|.dts)
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n212`


EEPROM
------

There are two different i2c EEPROM flashes populated on |som| SoM and on the
|sbc|. Both can be used with the sysfs interface in Linux. The ID page of the
I2C EEPROM populated on the SoM is also used for board detection.

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in phyCORE-|soc| file imx8mp-phycore-som.dtsi can be
found in our PHYTEC git:
:imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n199`

RTC
---

RTCs can be accessed via ``/dev/rtc*``. Because PHYTEC boards have often more than
one RTC, there might be more than one RTC device file.

*  To find the name of the RTC device, you can read its sysfs entry with:

   .. code-block:: console

      target:~$ cat /sys/class/rtc/rtc*/name

*  You will get, for example:

   .. code-block::

      rtc-rv3028 0-0052
      snvs_rtc 30370000.snvs:snvs-rtc-lp

.. tip::

   This will list all RTCs including the non-I²C RTCs. Linux assigns RTC device
   IDs based on the device tree/aliases entries if present.

Date and time can be manipulated with the ``hwclock`` tool and the date command.
To show the current date and time set on the target:

.. code-block:: console

   target:~$ date
   Thu Jan  1 00:01:26 UTC 1970

Change the date and time with the date command. The date command sets the time
with the following syntax "YYYY-MM-DD hh:mm:ss (+|-)hh:mm":

.. code-block:: console

   target:~$ date -s "2022-03-02 11:15:00 +0100"
   Wed Mar  2 10:15:00 UTC 2022

.. note::

   Your timezone (in this example +0100) may vary.

Using the date command does not change the time and date of the RTC, so if we
were to restart the target those changes would be discarded. To write to the RTC
we need to use the ``hwclock`` command. Write the current date and time (set
with the date command) to the RTC using the ``hwclock`` tool and reboot the
target to check if the changes were applied to the RTC:

.. code-block:: console

   target:~$ hwclock -w
   target:~$ reboot
       .
       .
       .
   target:~$ date
   Wed Mar  2 10:34:06 UTC 2022

To set the time and date from the RTC use:

.. code-block:: console

   target:~$ date
   Thu Jan  1 01:00:02 UTC 1970
   target:~$ hwclock -s
   target:~$ date
   Wed Mar  2 10:45:01 UTC 2022

.. include:: ../../peripherals/rtc.rsti
   :start-after: .. rtc_parameter_start_label

DT representation for I²C RTCs:
:imx-dt:`imx8mp-phycore-som.dtsi?h=v5.15.71_2.2.2-phy3#n207`

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
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n351`

CAN FD
------

The |sbc| two flexCAN interfaces supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon then the Linux network layer.
Using this framework, the CAN interfaces behave like an ordinary Linux network
device, with some additional features special to CAN. More information can be
found in the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n175`

Video
-----

Videos with Gstreamer
.....................

One example video is installed by default in the BSP at `/usr/share/qtphy/videos/`.
Start the video playback with one of these commands:

.. code-block:: console

   target:~$ gst-launch-1.0 -v filesrc location=/usr/share/qtphy/videos/caminandes_3_llamigos_720p_vp9.webm ! decodebin name=decoder decoder. ! videoconvert ! waylandsink fullscreen=true

*  Or:

.. code-block:: console

   target:~$ gst-play-1.0 /usr/share/qtphy/videos/caminandes_3_llamigos_720p_vp9.webm --videosink waylandsink

.. note::
   The mainline BSP currently only supports software rendering.

Display
-------

The |sbc| supports LVDS output via the LVDS1 connector on the carrier board. The
LVDS interface is enabled by default.

Weston Configuration
....................

Weston will work without any additional configuration. Configuration options are
done at /etc/xdg/weston/weston.ini.

Device tree description of LVDS-1 can be found here:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n264`

.. include:: /bsp/qt6.rsti

.. include:: ../peripherals/pm.rsti
   :end-before: .. suspend_to_ram_start_label

.. include:: ../peripherals/tm.rsti

The device tree description of GPIO Fan can be found here:
:imx-dt:`imx8mp-phyboard-pollux-rdk.dts?h=v5.15.71_2.2.2-phy3#n33`

.. include:: /bsp/peripherals/watchdog.rsti

snvs Power Key
--------------

The X_ONOFF pin connected to the ON/OFF button can be pressed long to trigger
Power OFF without SW intervention. With the *snvs_pwrkey* driver, the KEY_POWER
event is also reported to userspace when the button is pressed. On default, systemd
is configured to ignore such events. The function of Power OFF without SW
intervention are not configured. Triggering a power off with systemd when pushing
the ON/OFF button can be configured under ``/etc/systemd/logind.conf`` and set using:

.. code-block::

   HandlePowerKey=poweroff

.. include:: ../peripherals/ocotp-ctrl.rsti

Reading the registers using ``/dev/mem`` will cause the system to hang unless the
*ocotp_root_clk* is enabled. To enable this clock permanent, add to the device
tree:

.. code-block::

   &clk {
           init-on-array = <IMX8MP_CLK_OCOTP_ROOT>;
   };
