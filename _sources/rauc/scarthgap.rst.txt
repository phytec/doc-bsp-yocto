.. Download links
.. _`static-pdf-dl`: ../_static/rauc-scarthgap.pdf

.. RAUC
.. |yocto-codename| replace:: Scarthgap
.. |rauc-manual| replace:: RAUC Update & Device Management Manual

.. References
.. |ref-rauc-switch-keyrings| replace:: :ref:`scarthgap_rauc-switch-keyrings`
.. |ref-rauc-use-case-usb-update| replace:: :ref:`scarthgap_rauc-use-case-usb-update`
.. |ref-rauc-use-case-http-streaming| replace:: :ref:`scarthgap_rauc-use-case-http-streaming`
.. |ref-yocto-bsp-customization| replace:: :ref:`scarthgap_bsp-customization`

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+---------------------------------------------------------------+
| |rauc-manual|                                                 |
+=======================+=======================================+
| Document Title        | |rauc-manual| |yocto-codename|        |
+-----------------------+---------------------------------------+
| Document Type         | RAUC Update & Device Management       |
|                       | Manual                                |
+-----------------------+---------------------------------------+
| Last Modified         | 2025-02-10                            |
+-----------------------+---------------------------------------+
| Is Branch of          | |rauc-manual|                         |
+-----------------------+---------------------------------------+

+-------------------------------------+------------------+------------------+------------+
| Compatible BSPs                     | BSP Release Type | BSP Release Date | BSP Status |
+=====================================+==================+==================+============+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.0 | Major            | 2024-04-02       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.1 | Minor            | 2024-04-09       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.2 | Minor            | 2024-06-26       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-NXP-i.MX8MP-PD24.1.0      | Major            | 2024-11-07       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-NXP-i.MX93-PD24.2.0       | Major            | 2024-10-08       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-i.MX6UL-PD24.1.0 | Major            | 2024-07-19       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-AM62Ax-PD24.1.0  | Major            | 2024-06-27       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-AM62x-PD24.1.0   | Major            | 2024-06-27       | released   |
+-------------------------------------+------------------+------------------+------------+
| BSP-Yocto-Ampliphy-AM64x-PD24.1.0   | Major            | 2024-06-27       | released   |
+-------------------------------------+------------------+------------------+------------+

This manual was tested using the Yocto version |yocto-codename|.

.. include:: common/intro.rsti
.. include:: common/system-config.rsti
.. include:: common/design-considerations.rsti

Initial Setup
=============

To use RAUC, the flash device needs to be written with a complete Linux system
and bootloader. The preferred method to do this is using the included tool
`partup <https://partup.readthedocs.io/en/latest/>`_.

Flash Storage
-------------

To flash the device with the correct partitions/volumes, use a partup package
built with the ``ampliphy-rauc`` or ``ampliphy-vendor-rauc`` distribution.
Prebuilt partup packages can be found in the BSP release. It is also possible to
build an image with this distribution yourself using Yocto. Separate build
directories are created, storing the images and packages for the RAUC system.
Initialize the build directory with the OE init script:

.. code-block:: console

   host:~$ source sources/poky/oe-init-build-env

Change the distribution to ``ampliphy-rauc`` (for i.MX6, AM6x, i.MX8
mainline BSP) or ``ampliphy-vendor-rauc`` (for i.MX8, i.MX9 vendor BSP):

.. code-block::
   :caption: build/conf/local.conf

   DISTRO ?= "ampliphy-rauc"

Any image built with this distro now includes a full A/B system. Build the image
as usual:

.. code-block:: console

   host:~$ bitbake phytec-headless-image

The resulting partup package is stored in the ``deploy-ampliphy-vendor-rauc``
directory, e.g.:

.. code-block::

   deploy-ampliphy-vendor-rauc/images/phyboard-segin-imx93-2/phytec-headless-image-phyboard-segin-imx93-2.partup

This partup package contains all the necessary data and configuration to flash
an eMMC. `Partup <https://github.com/phytec/partup>`__ can be obtained from its
`release page <https://github.com/phytec/partup/releases>`_. Also, see its
README for detailed `installation instructions
<https://github.com/phytec/partup#installation>`_. Partup is already installed
in our Ampliphy images, ``phytec-headless-image`` and can be directly used e.g.
from an SD card.

.. note::
   To flash the initial RAUC system, a booted non-RAUC system is needed first on
   a different flash device. E.g. you could boot a regular
   ``phytec-headless-image`` image with distro ``ampliphy`` from an SD card.

eMMC
....

While running a non-RAUC system from an SD card on the target, copy the
``.partup`` package built with distro ``ampliphy-rauc`` or
``ampliphy-vendor-rauc`` to the running target first:

.. code-block:: console

   host:~$ scp phytec-headless-image-phyboard-segin-imx93-2.partup 192.168.3.11:/root

Then install the partup package to the eMMC:

.. code-block:: console

   target:~$ partup install phytec-headless-image-phyboard-segin-imx93-2.partup /dev/mmcblk0

Now the target can boot the flashed A/B system.

NAND
....

.. note::

   There are scripts provided with the bootloader barebox that previously were
   used to initialize NAND flash with an A/B system: ``rauc_init_nand``,
   ``rauc_flash_nand_from_tftp`` and ``rauc_flash_nand_from_mmc``. These scripts
   are deprecated. It is advised to use the script ``rauc-flash-nand`` provided
   in the Linux environment with PHYTEC's distribution *Ampliphy*.

With raw NAND flash the kernel, device tree, and root filesystem are written
individually. Initialize the NAND flash with the correct volumes from a Linux on
the target:

.. code-block:: console

   target:~$ rauc-flash-nand -k /path/to/zImage -d /path/to/oftree -r /path/to/root.ubifs

The initialization script will automatically utilize all available space of NAND
flash. The NAND device is also determined automatically by finding the device
root in ``/proc/mtd``.

On i.MX6 and i.MX6UL devices with barebox, use bbu (barebox update) to flash the
bootloader:

.. code-block:: console

   target:~$ bbu.sh -f /path/to/barebox.bin

The A/B system on NAND Flash is now ready to be booted.

Bootloader
----------

Booting the A/B System by Default
.................................

Booting the A/B system is done mostly automatically by the bootloader since the
Yocto release *hardknott*. For devices with eMMC flash storage, the
corresponding setting is written into the bootloader environment during the
building of the BSP. In particular, if the distribution ``ampliphy-rauc`` or
``ampliphy-vendor-rauc`` is used, as described previously, the bootloader should
automatically start the A/B system and have the variables set for RAUC
accordingly.

This automatic setting can be manually changed by setting one variable in the
bootloader. The procedure is described in more detail in the following chapters
for U-Boot and barebox.

U-Boot
......

After a successful boot into a Linux environment, this command is used to view
the available parameters:

.. code-block:: console

   target:~$ fw_printenv

You may see this parameter along with others in the output:

.. code-block::

   doraucboot=1

To manually disable or enable booting the A/B system with RAUC, set this
variable to ``0`` or ``1``:

.. code-block:: console

   target:~$ fw_setenv doraucboot 1

This parameter can also be edited in U-Boot. Restart your board and hit any key
to stop the automatic boot. The environment variables can now be viewed:

.. code-block::

   u-boot=> printenv

and set:

.. code-block::

   u-boot=> setenv doraucboot 1
   u-boot=> saveenv

Barebox
.......

In barebox, the system to be booted can be selected directly by its name. To
boot the A/B system, including RAUC, ``bootchooser`` is used. To boot e.g. a
regular SD card without RAUC use ``mmc`` instead, or ``nand`` for NAND devices:

.. code-block::

   barebox$ nv boot.default=bootchooser

.. include:: common/creating-bundles.rsti
.. include:: common/updating.rsti
.. _scarthgap_rauc-switch-keyrings:
.. include:: common/switch-keyrings.rsti

Use Case Examples
=================
.. _scarthgap_rauc-use-case-usb-update:
.. include:: common/use-case/usb-update.rsti
.. include:: common/use-case/downgrade-barrier.rsti
.. _scarthgap_rauc-use-case-http-streaming:
.. include:: common/use-case/http-streaming.rsti
.. include:: common/use-case/adaptive-updates.rsti

Reference
=========

Boot Logic Implementation
-------------------------

.. tip::

   The implementation details described in this chapter serve as a reference
   guide. PHYTEC BSPs that have RAUC support include these by default and the
   changes are already incorporated.

U-Boot Environment Variables
............................

For U-Boot, the boot logic that selects the correct partitions to boot from is
implemented in its environment. As a reference, these are the most important
U-Boot variables that are used for the A/B system with RAUC:

+-------------------+--------------------------------------------------------+
| Name              | Function                                               |
+===================+========================================================+
| BOOT_ORDER        | Contains a space-separated list of boot targets in the |
|                   | order they should be tried. This parameter is          |
|                   | automatically set by RAUC.                             |
+-------------------+--------------------------------------------------------+
| BOOT_<slot>_LEFT  | Contains the number of remaining boot attempts to      |
|                   | perform for the respective slot. This parameter is     |
|                   | automatically set by RAUC.                             |
+-------------------+--------------------------------------------------------+
| ``raucinit``      | Contains the boot logic that sets the partitions so    |
|                   | the correct system is loaded.                          |
+-------------------+--------------------------------------------------------+
| ``doraucboot``    | Enables booting the A/B system if set to 1 and         |
|                   | disables it if set to 0.                               |
+-------------------+--------------------------------------------------------+
| ``raucargs``      | Sets the Kernel bootargs like console, root, and RAUC  |
|                   | slot.                                                  |
+-------------------+--------------------------------------------------------+
| ``raucrootpart``  | Sets the root filesystem partitions of the device.     |
+-------------------+--------------------------------------------------------+
| ``raucbootpart``  | Sets the boot partitions of the device.                |
+-------------------+--------------------------------------------------------+

These environment variables are defined in ``include/env/phytec/rauc.env`` in
the u-boot source code.

.. note::

   A change in the partition layout, e.g. when using an additional data
   partition, may require changing the variables ``raucrootpart`` and
   ``raucbootpart``. Make sure to rebuild your image with the new bootloader
   environment after you have made the appropriate changes.

Barebox Bootchooser Framework
.............................

For the barebox, the boot logic that selects the correct partitions to boot from
is implemented using the bootchooser and state framework. See the barebox
documentation for detailed information about these: `Barebox Bootchooser
Framework <https://www.barebox.org/doc/latest/user/bootchooser.html>`_, `Barebox
State Framework <https://www.barebox.org/doc/latest/user/state.html>`_.

First, the state framework configuration needs to be added to the barebox device
tree. Check out the |ref-yocto-bsp-customization|
chapter in the Yocto reference manual. The state framework configuration is
already included with our BSP for the supported SoC and can be directly included
in the main barebox device tree. E.g. for i.MX6 based module:

.. code-block:: devicetree

   #include "imx6qdl-phytec-state.dtsi"

Afterward, rebuild the image and flash the new bootloader.

.. warning::

   Be aware that by adding the state framework configuration, the first 160
   bytes of the EEPROM are occupied and can no longer be used for user-specific
   purposes.

The following device tree snippet shows an example of the state framework
configuration used with the BSP. As can be seen, the EEPROM is used as a backend
for the state information:

.. code-block:: devicetree

   / {
       aliases {
           state = &state;
       };

       state: imx6qdl_phytec_boot_state {
           magic = <0x883b86a6>;
           compatible = "barebox,state";
           backend-type = "raw";
           backend = <&backend_update_eeprom>;
           backend-stridesize = <54>;

           #address-cells = <1>;
           #size-cells = <1>;
           bootstate {
               #address-cells = <1>;
               #size-cells = <1>;
               last_chosen {
                   reg = <0x0 0x4>;
                   type = "uint32";
               };
               system0 {
                   #address-cells = <1>;
                   #size-cells = <1>;
                   remaining_attempts {
                       reg = <0x4 0x4>;
                       type = "uint32";
                       default = <3>;
                   };
                   priority {
                       reg = <0x8 0x4>;
                       type = "uint32";
                       default = <21>;
                   };
                   ok {
                       reg = <0xc 0x4>;
                       type = "uint32";
                       default = <0>;
                   };
               };
               system1 {
                   #address-cells = <1>;
                   #size-cells = <1>;
                   remaining_attempts {
                       reg = <0x10 0x4>;
                       type = "uint32";
                       default = <3>;
                   };
                   priority {
                       reg = <0x14 0x4>;
                       type = "uint32";
                       default = <20>;
                   };
                   ok {
                       reg = <0x18 0x4>;
                       type = "uint32";
                       default = <0>;
                   };
               };
           };
       };
   };

   &eeprom {
       status = "okay";
       partitions {
           compatible = "fixed-partitions";
           #size-cells = <1>;
           #address-cells = <1>;
           backend_update_eeprom: state@0 {
               reg = <0x0 0x100>;
               label = "update-eeprom";
           };
       };
   };

To be able to boot from two systems alternately, the bootchooser needs to be
aware of the state framework configuration. For each system, a boot script is
required. For a system with NAND flash, the boot script of the first system may
look like the following:

.. code-block:: sh
   :caption: /env/boot/system0

   #!/bin/sh

   [ -e /env/config-expansions ] && /env/config-expansions

   [ ! -e /dev/nand0.root.ubi ] && ubiattach /dev/nand0.root

   global.bootm.image="/dev/nand0.root.ubi.kernel0"
   global.bootm.oftree="/dev/nand0.root.ubi.oftree0"
   global.linux.bootargs.dyn.root="root=ubi0:root0 ubi.mtd=root rootfstype=ubifs"

The second boot script has the same structure but uses the partitions containing
the second system. Machines with eMMC flash use similar boot scripts, albeit the
mounting and boot arguments look different.

Run the following commands to create the required bootchooser non-volatile
environment variables:

.. code-block::

   barebox$ nv bootchooser.state_prefix=state.bootstate
   barebox$ nv bootchooser.system0.boot=system0
   barebox$ nv bootchooser.system1.boot=system1
   barebox$ nv bootchooser.targets="system0 system1"

eMMC Boot Partitions
--------------------

With eMMC flash storage it is possible to use the dedicated boot partitions for
redundantly storing the bootloader.

By default, bundles built with our BSP (e.g. ``phytec-headless-bundle``) contain
the bootloader for updating eMMC boot partitions accordingly.

Note, that the U-Boot environment still resides in the user area before the
first partition. The user area also still contains the bootloader which the
image first shipped during its initialization process.

To manually write the bootloader to the eMMC boot partitions, first disable the
write protection:

.. code-block:: console

   target:~$ echo 0 > /sys/block/mmcblk2boot0/force_ro
   target:~$ echo 0 > /sys/block/mmcblk2boot1/force_ro

Write the bootloader to the eMMC boot partitions:

.. code-block:: console

   target:~$ dd if=imx-boot of=/dev/mmcblk2boot0 bs=1k seek=33
   target:~$ dd if=imx-boot of=/dev/mmcblk2boot1 bs=1k seek=33

This example is valid for the i.MX 8M Mini SoC. Note, that other SoCs may have
different bootloader files and require different offsets where the bootloader is
expected, specified by the seek parameter. See the following table for the
different offsets being required by each SoC:

+--------------+------------------+-----------------------+--------------+-------------+
| SoC          | Offset User Area | Offset Boot Partition | eMMC Device  | Bootloader  |
+==============+==================+=======================+==============+=============+
| i.MX 6       | 1 kiB            | 0 kiB                 | /dev/mmcblk3 | barebox.bin |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 6UL     | 1 kiB            | 0 kiB                 | /dev/mmcblk1 | barebox.bin |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 8M      | 33 kiB           | 33 kiB                | /dev/mmcblk0 | imx-boot    |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 8M Mini | 33 kiB           | 33 kiB                | /dev/mmcblk2 | imx-boot    |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 8M Nano | 32 kiB           | 0 kiB                 | /dev/mmcblk2 | imx-boot    |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 8M Plus | 32 kiB           | 0 kiB                 | /dev/mmcblk2 | imx-boot    |
+--------------+------------------+-----------------------+--------------+-------------+
| i.MX 93      | 32 kiB           | 0 kiB                 | /dev/mmcblk0 | imx-boot    |
+--------------+------------------+-----------------------+--------------+-------------+
| AM62x        | N/A              | 0 kiB                 | /dev/mmcblk0 | tiboot3.bin |
| AM62Ax       |                  | 512 kiB               |              | tispl.bin   |
| AM64x        |                  | 2560 kiB              |              | u-boot.img  |
+--------------+------------------+-----------------------+--------------+-------------+

Bootloader Offsets
..................

Note that the offset is different, depending on whether the bootloader resides
in the user area or the boot partitions of the eMMC.

After a bootloader has been written to the eMMC boot partitions, booting from
these can be enabled by using the following command:

.. code-block:: console

   target:~$ mmc bootpart enable 1 0 /dev/mmcblk2

This also means that only the bootloaders written in the eMMC boot partitions
are used. The bootloader in the user area is not used anymore. These steps are
also executed by RAUC internally when updating the target system with a bundle.

To disable booting from the eMMC boot partitions simply enter the following
command:

.. code-block:: console

   target:~$ mmc bootpart enable 0 0 /dev/mmcblk2

After this command, the eMMC user area is used to provide the bootloader.

When using U-Boot, a similar command is also available in the bootloader:

.. code-block::

   u-boot=> mmc partconf 2 0 0 0  # disable
   u-boot=> mmc partconf 2 0 1 0  # enable
