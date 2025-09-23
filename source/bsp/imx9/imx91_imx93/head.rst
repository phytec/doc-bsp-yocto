.. Download links
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-91-93/#downloads
.. |link-image-91| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx91-1/phytec-qt6demo-image-phyboard-segin-imx91-1.rootfs.wic.xz
.. |link-image-93| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx93-2/phytec-qt6demo-image-phyboard-segin-imx93-2.rootfs.wic.xz
.. |link-partup-package-91| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx91-1/phytec-qt6demo-image-phyboard-segin-imx91-1.rootfs.partup
.. |link-partup-package-93| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx93-2/phytec-qt6demo-image-phyboard-segin-imx93-2.rootfs.partup
.. |link-boot-tools| replace:: for |link-boot-tools-91|_ or for |link-boot-tools-93|_
.. |link-boot-tools-91| replace:: i.MX 91
.. _link-boot-tools-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx91-1/imx-boot-tools/
.. |link-boot-tools-93| replace:: i.MX 93
.. _link-boot-tools-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx93-2/imx-boot-tools/
.. |link-boot-tools-cmd-91| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx91-1/imx-boot-tools/
.. |link-boot-tools-cmd-93| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD24.2.1/images/ampliphy-vendor/phyboard-segin-imx93-2/imx-boot-tools/
.. _`static-pdf-dl`: ../../../_static/imx93-head.pdf

.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx93

.. General Substitutions
.. |doc-id| replace:: L-1069e.Ax
.. |kit| replace:: **phyBOARD-Segin i.MX 93 and phyBOARD-Nash i.MX 93 Kit**
.. |kit-ram-size| replace:: 1GiB
.. |sbc| replace:: phyBOARD-Segin/Nash i.MX 91/93
.. |sbc-segin| replace:: phyBOARD-Segin i.MX 91/93
.. |sbc-segin-91| replace:: phyBOARD-Segin i.MX 91
.. |sbc-segin-93| replace:: phyBOARD-Segin i.MX 93
.. |sbc-nash| replace:: phyBOARD-Nash i.MX 93
.. |soc| replace:: i.MX 93
.. |socfamily| replace:: i.MX 9
.. |som| replace:: phyCORE-|soc|
.. |debug-uart| replace:: ttyLP0
.. |serial-uart| replace:: ttyLP6
.. |bluetooth-uart| replace:: UART5
.. |expansion-connector| replace:: X16


.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: git://github.com/phytec/linux-phytec-imx.git
.. |kernel-socname-91| replace:: imx91
.. |kernel-socname-93| replace:: imx93
.. |kernel-tag| replace:: v6.6.52-2.2.0-phy9
.. |emmcdev| replace:: mmcblk0

.. Bootloader
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-multiple-defconfig-note| replace:: In command above replace ``<defconfig>`` with ``imx93-phycore_defconfig`` or ``imx91-phycore_defconfig``
.. |u-boot-multiple-dtb-note| replace:: In command above replace ``<dtb>`` with ``imx93-phyboard-segin.dtb``
.. |u-boot-imx-mkimage-tag| replace:: lf-6.6.52-2.2.0
.. |u-boot-soc-name| replace:: iMX9
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://git.phytec.de/u-boot-imx

.. IMX93 specific
.. |u-boot-socname-config| replace:: PHYCORE_IMX93
.. |u-boot-tag| replace:: v2024.04-2.2.0-phy9


.. Devicetree
.. |dt-carrierboard| replace:: imx93-phyboard-segin
.. |standalone_build_kernel_dtb_location_note| replace:: , or imx91-phyboard-segin.dtb, or imx93-phyboard-nash.dtb.
.. |standalone_build_kernel_cp_sdcard_note| replace:: **NOTE:** *For phyBOARD-Segin i.MX 91 replace* ``imx93-phyboard-segin.dtb`` *with* ``imx91-phyboard-segin.dtb``, *or for phyBOARD-Nash i.MX 93 with* ``imx93-phyboard-nash.dtb``.
.. |dt-som| replace:: imx93-phycore-som
.. |dtbo-rpmsg| replace:: ``imx93-phycore-rpmsg.dtbo``
.. |dtbo-npu| replace:: ``imx93-phycore-npu.dtbo``

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`scarthgap`
.. |yocto-codename| replace:: scarthgap
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: wic.xz
.. |installing_os_image_wic_note| replace:: **NOTE:** *The WIC image for* **phyBOARD-Segin i.MX 91** is: ``phytec-qt6demo-image-phyboard-segin-imx91-1.rootfs.wic.xz`` , *and for* **phyBOARD-Nash i.MX 93** *it is* ``phytec-qt6demo-image-phyboard-nash-imx93-1.rootfs.wic.xz``.
.. |installing_os_image_partup_note| replace:: **NOTE:** *The partup package for* **phyBOARD-Segin i.MX 91** *is* ``phytec-qt6demo-image-phyboard-segin-imx91-1.rootfs.partup`` , *and for* **phyBOARD-Nash i.MX 93** *it is* ``phytec-qt6demo-image-phyboard-nash-imx93-1.rootfs.partup``.
.. |installing_os_image_yocto_imageext_note| replace:: **NOTE:** *The WIC image for* **phyBOARD-Segin i.MX 91** *is* ``phytec-qt6demo-image-phyboard-segin-imx91-1.rootfs.wic.xz`` , *and for* **phyBOARD-Nash i.MX 93** *it is* ``phytec-qt6demo-image-phyboard-nash-imx93-1.rootfs.wic.xz``.
.. use imx93 as default machinename
.. |yocto-machinename| replace:: phyboard-segin-imx93-2
.. and define explicitly imx91 and imx93 machinenames for more specific cases
.. |yocto-machinename-91| replace:: phyboard-segin-imx91-1
.. |yocto-machinename-93| replace:: phyboard-segin-imx93-2
.. use imx93 manifest as default manifestname
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX93-PD24.2.y
.. and define explicitly imx91 and imx93 manifestname for more specific cases
.. |yocto-manifestname-91| replace:: BSP-Yocto-NXP-i.MX91-PD24.2.y
.. |yocto-manifestname-93| replace:: BSP-Yocto-NXP-i.MX93-PD24.2.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (scarthgap) <yocto-man-scarthgap>`
.. |yocto-sdk-rev| replace:: 5.0.x
.. |yocto-sdk-a-core| replace:: cortexa55

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S3) <imx93-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx93-head-images>`
.. |ref-debugusbconnector| replace:: UART1 console on PEB-EVAL-01 for **phyBOARD-Segin** and X-37
   USB-C debug for **phyBOARD-Nash**
.. |ref-dt| replace:: :ref:`device tree <imx93-head-device-tree>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx93-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx93-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx93-head-development>`
.. |ref-usb-otg| replace:: :ref:`X8 (USB micro/OTG connector) <imx93-head-components>`


.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx93-head-ubootexternalenv>`


.. M-Core specific
.. |mcore| replace:: M33 Core
.. |ref-m-core-connections| replace:: :ref:`X16 <imx93-head-components>`
.. |mcore-jtag-dev| replace:: MIMX8MM6_M4
.. |mcore-sdk-version| replace:: 2.13.0


.. Dont include /bsp/global-defaults.rsti , but define
   contents specifically here below, to be able to embed
   individual links/URLs for imx91 and imx93.
.. |dl-server-link| replace:: |dl-server-link-91|_ or |dl-server-link-93|_ BSP downloads
.. |dl-server-link-91| replace:: i.MX 91
.. _dl-server-link-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/
.. |dl-server-link-93| replace:: i.MX 93
.. _dl-server-link-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/

.. |dl-sdk-link| replace:: |dl-sdk-91|_ or |dl-sdk-93|_ downloads
.. |dl-sdk-91| replace:: i.MX 91 SDK
.. _dl-sdk-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD24.2.1/sdk/ampliphy-vendor/
.. |dl-sdk-93| replace:: i.MX 93 SDK
.. _dl-sdk-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD24.2.1/sdk/ampliphy-vendor/

.. |dlpage-bsp-link| replace:: our |dlpage-bsp-91|_ or |dlpage-bsp-93|_
.. |dlpage-bsp-91| replace:: i.MX 91 BSP
.. _dlpage-bsp-91: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX91-PD24.2.1
.. |dlpage-bsp-93| replace:: i.MX 93 BSP
.. _dlpage-bsp-93: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX93-PD24.2.1

.. |dt-somnetwork-link| replace:: for |dt-somnet-91|_ or |dt-somnet-93|_
.. |dt-somnet-91| replace:: phyCORE i.MX 91
.. _dt-somnet-91: https://github.com/phytec/linux-phytec-imx/blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L56
.. |dt-somnet-93| replace:: phyCORE i.MX 93
.. _dt-somnet-93: https://github.com/phytec/linux-phytec-imx/blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L61

.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   can be found here: for |dt-sbcnet-91-segin|_ or |dt-sbcnet-93-segin|_ or |dt-sbcnet-93-nash|_
.. |dt-sbcnet-91-segin| replace:: phyBOARD-Segin i.MX 91
.. _dt-sbcnet-91-segin: https://github.com/phytec/linux-phytec-imx/blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L119
.. |dt-sbcnet-93-segin| replace:: phyBOARD-Segin i.MX 93
.. _dt-sbcnet-93-segin: https://github.com/phytec/linux-phytec-imx/blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L118
.. |dt-sbcnet-93-nash| replace:: phyBOARD-Nash i.MX 93
.. _dt-sbcnet-93-nash: https://github.com/phytec/linux-phytec-imx/blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L87


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

======================= ================ ================ ==========
Compatible BSPs         BSP Release Type BSP Release Date BSP Status

======================= ================ ================ ==========
|yocto-manifestname-91| Head             ----/--/--       Development
|yocto-manifestname-93| Head             ----/--/--       Development
======================= ================ ================ ==========


.. include:: ../../intro.rsti

Supported Hardware
------------------

On our web page, you can see all supported Machines with the available Article
Numbers for this BSP manual:

* For BSP release |yocto-manifestname-91|, see |dlpage-bsp-91|_
* For BSP release |yocto-manifestname-93|, see |dlpage-bsp-93|_

If you choose a specific **Machine Name** in the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware.

.. tip::

   **Console examples in this BSP manual only focus on phyBOARD-Segin i.MX 93.
   Similar commands can also be executed for/on phyBOARD-Nash i.MX 93**

.. _imx93-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx93-head-getting-started:
.. include:: /bsp/getting-started.rsti
   :end-before: .. getting_started_get_image_cmd_start_label

For i.MX 91:

.. code-block:: console
   :substitutions:

   host:~$ wget |link-partup-package-91|
   host:~$ wget |link-image-91|

For i.MX 93:

.. code-block:: console
   :substitutions:

   host:~$ wget |link-partup-package-93|
   host:~$ wget |link-image-93|


.. include:: /bsp/getting-started.rsti
   :start-after: .. getting_started_get_image_cmd_end_label

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the
   following position:

.. image:: images/SD_Card_Boot.png

*  Insert the SD card
*  Connect the targets debug console with your host.
   Use |ref-debugusbconnector|.
*  Power up the board
*  Open serial/usb port with 115200 baud and 8N1 (you should see u-boot/linux
   start on the console

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti
   :end-before: .. building_bsp_phylinux_cmd_start_label

For i.MX 91:

   .. code-block:: console
      :substitutions:

      host:~/yocto$ DISTRO=|yocto-distro| MACHINE=|yocto-machinename-91| ./phyLinux init -p |kernel-socname-91| -r |yocto-manifestname-91|

For i.MX 93:

   .. code-block:: console
      :substitutions:

      host:~/yocto$ DISTRO=|yocto-distro| MACHINE=|yocto-machinename-93| ./phyLinux init -p |kernel-socname-93| -r |yocto-manifestname-93|

.. include:: /bsp/building-bsp.rsti
   :start-after: .. building_bsp_phylinux_cmd_end_label

.. _imx93-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx93.bin** or **bl31-imx91.bin**: ARM Trusted Firmware binary
*  **lpddr4_dmem_1d_v202201.bin, lpddr4_dmem_2d_v202201.bin,
   lpddr4_imem_1d_v202201.bin,
   lpddr4_imem_2d_v202201.bin**: DDR PHY firmware images
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which
   is bootable.
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
*  **imx93-11x11-evk_m33_\*.bin**, binaries of demo applications for the
   Cortex-M33 MCU; can be manually loaded and started with U-Boot or Linux;
   are not part of builds for i.MX 91;

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S3)
--------------------

.. tip::

   Hardware revision baseboard:

   *  |sbc-segin|: 1472.5
   *  |sbc-nash|: 1616.0, 1616.1, 1616.2

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx93-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx93-head-development:

Development
===========

.. include:: ../../imx-common/development/host_network_setup.rsti
.. include:: ../../imx-common/development/netboot.rsti

Working with UUU-Tool
---------------------

The Universal Update Utility Tool (UUU-Tool) from NXP is a software to execute
on the host to load and run the bootloader on the board through SDP (Serial
Download Protocol). For detailed information visit
https://github.com/nxp-imx/mfgtools or download the `Official UUU-tool
documentation <https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/imx-processors/140261/1/UUU.pdf>`_.

Host preparations for UUU-Tool Usage
....................................

*  Follow the instructions from https://github.com/nxp-imx/mfgtools#linux.

*  If you built UUU from source, add it to ``PATH``:

   This BASH command adds UUU only temporarily to ``PATH``. To add it
   permanently, add this line to ``~/.bashrc``.

   .. code-block:: console

      export PATH=~/mfgtools/uuu/:"$PATH"

*  Set udev rules (documented in ``uuu -udev``):

   .. code-block:: console

      host:~$ sudo sh -c "uuu -udev >> /etc/udev/rules.d/70-uuu.rules"
      host:~$ sudo udevadm control --reload

Get Images
..........

Download imx-boot from our server or get it from your Yocto build directory at
build/deploy/images/|yocto-machinename|/. For flashing a wic image to eMMC,
you will also need |yocto-imagename|-|yocto-machinename|.wic.

Prepare Target
..............

Set the |ref-bootswitch| to **USB Serial Download**. Also, connect USB port
|ref-usb-otg| to your host.

Starting bootloader via UUU-Tool
................................

Execute and power up the board:

.. code-block:: console

   host:~$ sudo uuu -b spl imx-boot

You can see the bootlog on the console via |ref-debugusbconnector|, as usual.

.. note::
   The default boot command when booting with UUU-Tool is set to fastboot. If
   you want to change this, please adjust the environment variable bootcmd_mfg
   in U-boot prompt with setenv bootcmd_mfg. Please note, when booting with
   UUU-tool the default environment is loaded. Saveenv has no effect. If you
   want to change the boot command permanently for UUU-boot, you need to change
   this in U-Boot code.

Flashing U-boot Image to eMMC via UUU-Tool
...........................................

.. warning::

   UUU flashes U-boot into eMMC BOOT (hardware) boot partitions, and it sets
   the BOOT_PARTITION_ENABLE in the eMMC! This is a problem since we want the
   bootloader to reside in the eMMC USER partition. Flashing next U-Boot version
   .wic image and not disabling BOOT_PARTITION_ENABLE bit will result in device
   always using U-boot saved in BOOT partitions. To fix this in U-Boot:

   .. code-block:: console
      :substitutions:

      u-boot=> mmc partconf |u-boot-emmc-devno| 0 0 0
      u-boot=> mmc partconf |u-boot-emmc-devno|
      EXT_CSD[179], PARTITION_CONFIG:
      BOOT_ACK: 0x0
      BOOT_PARTITION_ENABLE: 0x0
      PARTITION_ACCESS: 0x0

   or check :ref:`Disable booting from eMMC boot partitions <emmc-disable-boot-part>`
   from Linux.

   This way the bootloader is still flashed to eMMC BOOT partitions but it is
   not used!

   When using **partup** tool and ``.partup`` package for eMMC flashing this is
   done by default, which makes partup again superior flash option.

Execute and power up the board:

.. code-block:: console

   host:~$ sudo uuu -b emmc imx-boot

Flashing wic Image to eMMC via UUU-Tool
...........................................

Execute and power up the board:

.. code-block:: console
   :substitutions:

   host:~$ sudo uuu -b emmc_all imx-boot |yocto-imagename|-|yocto-machinename|.wic

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

.. include:: ../../imx-common/development/standalone_build_u-boot_imxmkimage.rsti
   :end-before: .. standalone_u_boot_imxmkimage_boot_file_start_label

*  **ARM Trusted firmware binary** (*mkimage tool* compatible format
   **bl31.bin**): bl31-imx91.bin or bl31-imx93.bin
*  **OPTEE image** (optional): tee.bin
*  **DDR firmware files** (*mkimage tool* compatible format
   **lpddr4_[i,d]mem_\*d_\*.bin**):
   lpddr4_dmem_1d_*.bin, lpddr4_dmem_2d_*.bin, lpddr4_imem_1d_*.bin,
   lpddr4_imem_2d_*.bin
*  **Container image**: mx93a1-ahab-container.img or mx91a0-ahab-container.img

.. include:: ../../imx-common/development/standalone_build_u-boot_imxmkimage.rsti
   :start-after: .. standalone_u_boot_imxmkimage_boot_file_end_label
   :end-before: .. standalone_u_boot_imxmkimage_boot_file_download_cmds_start_label

For i.MX 91:

.. code-block:: console
   :substitutions:

   host:~$ mkdir ./artefacts && cd ./artefacts
   host:~/artefacts$ wget \
                       |link-boot-tools-cmd-91|/bl31-imx91.bin \
                       |link-boot-tools-cmd-91|/tee.bin \
                       |link-boot-tools-cmd-91|/lpddr4_dmem_1d_v202201.bin \
                       |link-boot-tools-cmd-91|/lpddr4_dmem_2d_v202201.bin \
                       |link-boot-tools-cmd-91|/lpddr4_imem_1d_v202201.bin \
                       |link-boot-tools-cmd-91|/lpddr4_imem_2d_v202201.bin \
                       |link-boot-tools-cmd-91|/mx91a0-ahab-container.img
   host:~/artefacts$ cd ..

For i.MX 93:

.. code-block:: console
   :substitutions:

   host:~$ mkdir ./artefacts && cd ./artefacts
   host:~/artefacts$ wget \
                       |link-boot-tools-cmd-93|/bl31-imx93.bin \
                       |link-boot-tools-cmd-93|/tee.bin \
                       |link-boot-tools-cmd-93|/lpddr4_dmem_1d_v202201.bin \
                       |link-boot-tools-cmd-93|/lpddr4_dmem_2d_v202201.bin \
                       |link-boot-tools-cmd-93|/lpddr4_imem_1d_v202201.bin \
                       |link-boot-tools-cmd-93|/lpddr4_imem_2d_v202201.bin \
                       |link-boot-tools-cmd-93|/mx93a1-ahab-container.img
   host:~/artefacts$ cd ..

.. include:: ../../imx-common/development/standalone_build_u-boot_imxmkimage.rsti
   :start-after: .. standalone_u_boot_imxmkimage_boot_file_download_cmds_end_label


.. include:: ../../imx-common/development/standalone_build_kernel.rsti

.. include:: ../../imx-common/development/format_sd-card.rsti

Enabling JTAG Debug Interface on phyBOARD Nash
----------------------------------------------

The |soc| has a JTAG debug interface which can be used to debug software running
on the SoC. The JTAG interface is routed through the pinmux and is not enabled
by default. To enable the JTAG interface, please add this overlay to your
``bootenv.txt`` file:

.. code-block::

   imx93-phyboard-nash-jtag.dtbo

.. note::
   JTAG and the MIPI CSI interface cannot be used at the same time, since they
   share the same pins. Jumper ``JP15`` switches signals between JTAG and
   MIPI CSI. It needs to be set to use JTAG.

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx93-head-device-tree:
.. include:: /bsp/device-tree.rsti

::

   imx93-phyboard-segin-peb-av-02.dtbo
   imx93-phyboard-segin-peb-eval-01.dtbo
   imx93-phyboard-segin-peb-wlbt-05.dtbo
   imx93-phycore-npu.dtbo
   imx93-phycore-rpmsg.dtbo
   imx91-imx93-phycore-no-emmc.dtbo
   imx91-imx93-phycore-no-eth.dtbo

Available overlays for phyboard-segin-imx91-1.conf are:

::

   imx91-phyboard-segin-peb-av-02.dtbo
   imx91-phyboard-segin-peb-eval-01.dtbo
   imx91-phyboard-segin-peb-wlbt-05.dtbo
   imx91-imx93-phycore-no-emmc.dtbo
   imx91-imx93-phycore-no-eth.dtbo

Available overlays for phyboard-nash-imx93-1.conf are:

::

   imx93-phyboard-nash-jtag.dtbo
   imx93-phyboard-nash-peb-av-10.dtbo
   imx93-phyboard-nash-peb-wlbt-07.dtbo
   imx93-phyboard-nash-pwm-fan.dtbo
   imx93-phyboard-nash-vm016.dtbo
   imx93-phycore-npu.dtbo
   imx93-phycore-rpmsg.dtbo
   imx91-imx93-phycore-no-emmc.dtbo
   imx91-imx93-phycore-no-eth.dtbo

.. _imx93-head-ubootexternalenv:
.. include:: ../dt-overlays.rsti

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
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L263`

.. _imx93-head-network:

Network
-------

|sbc| provides two ethernet interfaces.

*  On |sbc-segin| we have:

   *  a 100 megabit Ethernet provided by |som|
   *  and 100 megabit Ethernet provided by phyBOARD.

*  On |sbc-nash| we have:

   *  a 100 megabit Ethernet provided by |som|
   *  and 1 gigabit Ethernet provided by phyBOARD.

.. include:: /bsp/imx-common/peripherals/network.rsti

.. include:: wireless-network.rsti

.. include:: ../../peripherals/wireless-network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L209`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L217`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L206`

DT configuration for the eMMC interface can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L192`
* for |sbc-segin-93| or |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L194`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: ../peripherals/gpios.rsti

.. include:: /bsp/peripherals/adc.rsti

On |sbc-nash| the ADC lines are accessible on X16 expansion connector:

========= ========
ADC input X16 pin
========= ========
ADC_IN0        47
ADC_IN2        49
========= ========

.. include:: ../peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin-peb-eval-01.dtso#L33`
or :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin-peb-eval-01.dtso#L33`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C3 bus configuration (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L88`
or :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L82`

General I²C2 bus configuration for |dt-carrierboard|.dts:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L151`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L159`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L117`


EEPROM
------

There are two different I2C EEPROM flashes populated on |som| SoM and on the
|sbc|. For now only the one on the |som| is enabled, and it is used for board
detection.

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in |som| file can be found in our PHYTEC git:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L172`
or :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L170`

.. include:: ../../peripherals/rtc.rsti

DT representation for I²C RTCs:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L169`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L177`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L126`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed of up to 480 Mbps (HighSpeed
'HS'). The USB subsystem has two independent USB controller cores. Both cores
are capable of acting as a USB peripheral device or a USB host, but on the |sbc|
one of them is used as a host-only port (USB-A connector).

.. include:: /bsp/peripherals/usb-host.rsti

The OTG port provides an additional pin for over-current protection, which is
not used on the |sbc|. Since it's not used, the driver part is also disabled
from within the device tree. In case this pin is used, activate this
over-current in the device tree and set the correct polarity (active high/low)
according to the device specification. For the correct setup, please refer to
the Kernel documentation under
Linux/Documentation/devicetree/bindings/usb/ci-hdrc-usb2.txt.

DT representation for USB Host:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L188`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L196`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L185`

RS232/RS485
-----------

The |sbc-nash| i.MX 93 SoC provides one RS232/RS485 serial port.

.. warning::
   RS232 with HW flow control and RS485 are not working due to HW bug on the
   |sbc-nash| PCB revision 1616.0

.. include:: /bsp/peripherals/rs232.rsti
.. include:: /bsp/peripherals/rs485.rsti

The device tree representation for RS232 and RS485:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L178`

CAN FD
------

The |sbc| has one flexCAN interface supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon the Linux network layer. Using
this framework, the CAN interfaces behave like an ordinary Linux network device,
with some additional features special to CAN. More information can be found in
the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: ../peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L143`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L151`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L109`

Audio on |sbc-segin|
--------------------

On |sbc-segin| the TI TLV320AIC3007 audio codec is used. It uses I2S
for data transmission and I2C for codec control. The audio signals available
are:

* Stereo LINE IN,
* Stereo LINE OUT,
* Output where D-Class 1W speaker can be connected

.. include:: /bsp/peripherals/audio.rsti
   :end-before: .. audio_alsa_configuration_start_label

.. include:: /bsp/peripherals/audio.rsti
   :start-after: .. audio_playback_start_label
   :end-before: .. audio_capture_start_label

If Speaker volume it too low you can increase its volume with (values 0-3):

.. code-block:: console

   target:~$ amixer -c 0 sset Class-D 3

.. hint::

   Speaker output is only mono so when stereo track is played only left channel
   will be played by speaker.

Capture
.......

``arecord`` is a command-line tool for capturing audio streams which use Line In
as the default input source.

.. code-block:: console

   target:~$ arecord -t wav -c 2 -r 44100 -f S16_LE test.wav

.. hint::

   Since playback and capture share hardware interfaces, it is not possible to
   use different sampling rates and formats for simultaneous playback and
   capture operations.

Device Tree Audio configuration:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L62`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L62`

Audio on |sbc-nash|
-------------------

.. warning::

   Due to HW bug Audio is broken on |sbc-nash| PCB revision: 1616.0

To use audio with |sbc-nash| an additional adapter for the Audio/Video
connector is needed. The PEB-AV-10 (1531.1 revision) can be bought separately to
the Kit. PEB-AV-10 is populated with a TI TLV320AIC3007 audio codec. Audio
support is done via the I2S interface and controlled via I2C.

There is a 3.5mm headset jack with OMTP standard and an 8-pin header to connect
audio devices with the AV-Connector.  The 8-pin header contains a mono speaker,
headphones, and line-in signals.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash-peb-av-10.dtso#L56`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

The device tree of PEB-AV-02 can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin-peb-av-02.dtso`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin-peb-av-02.dtso`

The device tree of PEB-AV-10 for |sbc-nash| can be found here:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash-peb-av-10.dtso`

.. include:: peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: ../peripherals/bbnsm-power-key.rsti

.. include:: ../peripherals/pxp.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

.. include:: /bsp/imx9/imx91_imx93/peripherals/tpm.rsti

Device tree TPM configuration can be found here:
:linux-phytec-imx:`blob/v6.6.52-2.2.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L161`

.. +---------------------------------------------------------------------------+
.. i.MX 93 M33 Core
.. +---------------------------------------------------------------------------+

.. include:: ../mcu.rsti

.. +---------------------------------------------------------------------------+
.. i.MX 93 NPU
.. +---------------------------------------------------------------------------+

.. include:: /bsp/imx9/imx91_imx93/peripherals/npu.rsti
