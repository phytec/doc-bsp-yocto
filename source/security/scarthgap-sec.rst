.. Download links
.. _`static-pdf-dl`: ../_static/scarthgap-sec.pdf

.. |secure-boot-link| replace:: :ref:`secure-boot-scarthgap`
.. |secure-key-storage-link| replace:: :ref:`secure-key-storage-scarthgap`
.. |phytec-pki-link| replace:: :ref:`phytec-pki-scarthgap`
.. |physical-security-link| replace:: :ref:`physical-security-scarthgap`

.. Yocto
.. |branding-name| replace:: securiPHY
.. |yocto-codename| replace:: Scarthgap
.. |distro-secure-vendor| replace:: securiphy-vendor
.. |distro-secure| replace:: securiphy
.. |distro-provisioning| replace:: securiphy-provisioning
.. |distro-provisioning-vendor| replace:: securiphy-vendor-provisioning
.. |image-secure-name| replace:: phytec-securiphy-image

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-------------------------------------+--------------+--------------+-----------+
|| Compatible BSPs                    || BSP Release || BSP Release || Security |
||                                    || Type        || Date        || Support  |
||                                    ||             ||             || Status   |
+=====================================+==============+==============+===========+
| BSP-Yocto-Ampliphy-i.MX6UL-PD24.1.0 | Major        | 2024-07-19   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.0 | Major        | 2024-04-02   | none      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.1 | Minor        | 2024-04-09   | none      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.2 | Minor        | 2024-06-26   | none      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX8MP-PD24.1.0      | Major        | 2024-11-07   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX8MM-PD25.1.0      | Major        | 2025-03-28   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX91-PD24.2.1       | Major        | 2025-03-21   | none      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX91-PD24.2.2       | Major        | 2025-06-30   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX93-PD24.2.0       | Major        | 2024-10-08   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX93-PD24.2.1       | Minor        | 2025-03-21   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX93-PD24.2.2       | Minor        | 2025-06-30   | full      |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM62Ax-PD24.1.0  | Major        | 2024-06-27   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM62Ax-PD24.1.2  | Minor        | 2025-03-24   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM62x-PD24.1.0   | Major        | 2024-06-27   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM62x-PD24.1.2   | Minor        | 2025-03-19   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM64x-PD24.1.0   | Major        | 2024-06-27   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM64x-PD24.1.1   | Minor        | 2024-12-19   | partly    |
+-------------------------------------+--------------+--------------+-----------+
| BSP-Yocto-Ampliphy-AM64x-PD25.1.0   | Major        | 2025-03-24   | partly    |
+-------------------------------------+--------------+--------------+-----------+

This manual applies to all |yocto-codename| based PHYTEC releases.

Introduction
============

PHYTEC's Yocto distribution securiPHY (former Ampliphy-secure) supports
different security mechanism. The security features have impact on the
bootloader, the Linux kernel, Device Tree, and root filesystem. This manual
describes how security features are used and implemented on various PHYTEC
platforms. Note that different modules use different bootloaders and flash
storage devices, which affects the way things are handled. Make sure to
read the correct sections fitting your platform.

.. note::

   This manual contains machine-specific paths and variable contents. Make sure
   you are using the correct machine and device names for your application when
   executing any commands.

.. _scarthgap-security-overview:
.. include:: common/security-overview.rsti

.. include:: common/distro-using.rsti
.. _secure-boot-scarthgap:
.. include:: common/secure-boot.rsti

There are two different Yocto classes for creation of a signed FIT-image.

* PHYTEC ``sources/meta-phytec/classes/fitimage.bbclass``

   * With FIT-image recipes you can define custom, more refined FIT-images.
   * Example for FIT-image recipes are in ``sources/meta-ampliphy/recipes-images/fitimage/``
   * To create custom FIT-image, you need to specify some variables in the
     recipe:

      * FITIMAGE_SLOTS: Use this to list all slot classes for which the
        FIT-image should contain images. A value of "kernel fdt fdtapply",
        for example, will create a manifest with images for two slot classes -
        kernel and devicetree.
      * FITIMAGE_SLOT_<slotclass>: For each slot class, set this to the image
        (recipe) name which builds the artifact you intend to place in the slot
        class.
      * FITIMAGE_SLOT_<slotclass>[type]: For each slot class, set this to the
        type of image you intend to place in this slot. Possible types are the
        kernel, fdt, fdto, fdtapply, or ramdisk.
      * FITIMAGE_SLOT_<slotclass>[file]: For slot type kernel, fdt, fdt0 and
        fdtapply set this to the file of the image you intend to place in this
        slot.
      * FITIMAGE_SLOT_<slotclass>[fstype]: For slot type ramdisk, set this to
        the filesystem type of image you intend to place in this slot.
      * FITIMAGE_SLOT_<slotclass>[name]: For slot type fdtapply, set this to
        the final device tree and configuration name.

* Poky ``sources/poky/meta/classes-recipe/kernel-fitimage.bbclass``

   * This is the standard upstream FIT-image class in Yocto mainly for u-boot,
     which builts one FIT-image with initramfs and without initramfs.

Initially, the PHYTEC FIT-image class was used to create the FIT-images, because
it supports barebox and u-boot and you can define more refined FIT-images.
Since security has increasingly become an integral part of the SoC
manufacturer's BSPs, which use the kernel-fitimage, PHYTEC has decided to
gradually switch to this class, too.

Configuration Class for Signing Images
--------------------------------------
All variables to adjust the bootloader and kernel fitImage signing process can
be found in the ``source/meta-ampliphy/secureboot.bbclass``

First of all, the necessary variables for signing the bootloader for the
different SoC types need to be defined. The variable ``BOOTLOADER_SIGN`` is
obsolete, because the ``DISTRO_FEATURES="secureboot"`` includes the bootloader
signing.

.. code-block:: bash
.. include:: common/activate-secureboot.rsti
.. include:: common/kernel-module-signing.rsti
.. include:: common/devicetree-overlay.rsti
.. _secure-key-storage-scarthgap:
.. include:: common/secure-key-storage.rsti

Secure Key Storage Initialization with phySecureKeyStorage Tool
---------------------------------------------------------------

The tool `physecurekeystorage-install <https://git.phytec.de/meta-ampliphy/tree/recipes-securiphy/secure-key-storage/secure-key-storage>`_
is part of the ramdisk userspace of phytec-provisioning-initramfs and included
in the meta-ampliphy layer of the PHYTEC Standard BSP.

The ``physecurekeystorage-install`` tool can initialize all supported secure key
storages of your machine, but always only one can be active.
For example, the phyBOARD-Polis-imx8mm supports Trusted TEE, Trusted TPM,
Trusted CAAM and Secure CAAM, but initialized is only Trusted TPM.

.. code-block:: console

   target:~$ physecurekeystorage-install -h

   PHYTEC Install Script v1.7 for Secure Key Storage

   Usage:  physecurekeystorage-install [PARAMETER] [ACTION]

   Example:
      physecurekeystorage-install --newkeystorage trustedtpm
      physecurekeystorage-install --deletekeystorage
      physecurekeystorage-install --loadkeystorage
      physecurekeystorage-install --pkcs11testkey

   One of the following action can be selected:
      -n | --newkeystorage <value>  Create new Secure Key Storage
                              trustedcaam (only NXP controller)
                              trustedtee
                              trustedtpm
                              securecaam (black blob only NXP Vendor BSP)
      -d | --deletekeystorage Erase the existing Secure Key Storage
      -l | --loadkeystorage   Load the existing Secure Key Storage
      -p | --pkcs11testkey    Create an ECC testkey with user pin 1234
      -h | --help             This Help
      -v | --version          The version of physecurekeystorage-install

.. include:: common/secure-storage.rsti

Boot Process Flow
-----------------

* bootloader verifies FIT-image with linux-kernel image, device tree, and
  ramdisk before they are executed
* Linux kernel executes the ramdisk (read-only filesystem)
* The bootscript loads the authenticated encrypted filesystem encryption key
  with the CAAM, TEE or TPM unit in the RAM and encrypts the filesystem. After
  the encryption, the root filesystem will be switched and the boot process
  continues.

Starting the Build Process
--------------------------

Filesystem integrity and encryption are included in the ``DISTRO_FEATURES``
``secureboot`` and ``securestorage``.

You can choose in the ``sources/meta-ampliphy/conf/distro/common-secure.inc``
between

  * ``fileauthorenc``: use integrity or encrypted filesystem
  * ``fileauthandenc``: use integrity and encrypted filesystem

This configuration is important for the RAUC update system because the use of
integrity and encrypted filesystem are stacked and the number of device-mappers
is doubled to use integrity or encrypted filesystem.

.. code-block:: bash

   DISTRO_FEATURES += "securestorage"
   #possible types: fileauthorenc , fileauthandenc
   SECURE_STORAGE_TYPE = "fileauthandenc"
   OVERRIDES_append = ":securestorage:${SECURE_STORAGE_TYPE}"

This configuration changes the RAUC ``system.conf`` configuration in the rootfs
image for the target, too. The device changes from the ``/dev/mtdblockX`` to the
device mapper ``/dev/dm-x``. With this changes the integrity and the encryption are
retained during an update.

Setup Secure Storage on your Device
-----------------------------------

The filesystem encryption ensures the target has a unique key or an equal key
per device.

The filesystem encryption process flow:

* The filesystem encryption key is generated and stored encrypted with CAAM,
  TEE, or TPM.
* Encryption is initialized.
* The partition is formatted.
* Data is copied to the encrypted partition.

First Boot
..........

From a high-level point of view, an eMMC device is like an SD card. Therefore,
it is possible to flash the image phytec-provisioning-image
from the Yocto build system directly to the SD card. The image contains the
signed bootloader and signed FIT-image with an initramfs.

If your filesystem is not initialized, is damaged, or the key blob is deleted,
then you can reinstall the encrypted filesystem with the following instructions.

* Boot the phytec-provisioning-image from the SD card or load the provisioning
  fitImage with tftp to the memory in the bootloader
* The device stops with the following message because there is no encrypted key
  stored in the folder ``/mnt/config/secrets``:

The default user is root with the password root:

.. note::

   If there is no login in 60s, then the system goes to power off

   .. code-block:: console

      Login timed out after 60 second
      [ERROR] Key and Filesystem Initialization
      The system will poweroff in 10 seconds
      reboot: Power down

* If this is your first boot from the device and no image is on the eMMC,
  please flash an image to the eMMC.

Key Generation for Secure Storage
.................................

Please follow the instructions in the chapter |secure-key-storage-link|

Secure Storage Initialization with phySecureStorage Tool
........................................................

The tool ``physecurestorage-install`` is part of the initramfs userspace of the
phytec-provisioning-image.

The ``physecurestorage-install`` tool can initialize the filesystem with encryption,
integrity, or both methods together.

.. code-block:: console

   target:~$ physecurestorage-install -h

   PHYTEC Install Script v1.5 for Secure Storage

   Usage:  physecurestorage-install [PARAMETER] [ACTION]

   Example:
   physecurestorage-install --flashpath /dev/mmcblk0
   --filesystem /media/phytec-security-image.ext4
   --flashlayout 5,6
   --newsecurestorage intenc

   One of the following action can be selected:
      -n | --newsecurestorage <value>   Create new Secure Storage of type
                              int     Root File System with integrity
                              enc     Encrypted root file system
                              intenc  Encrypted root file system with integrity
      -h | --help             This Help
      -v | --version          The version of the physecurestorage-install

   The following PARAMETER must be set for new Secure Storage:
      -p | --flashpath <flash device>
      -s | --filesystem <path to root as tgz or ext4>
      -l | --flashlayout <value>    partition number for the rootfs partitions
                           5,6       rootfs partitions are 5 and 6
      -L | --labelname <value>      label name for the partition

* The parameter <flashpath> is the eMMC device.
* The parameter <filesystem> is the path to tar.gz archive of the filesystem,
  which should be installed on the flash device.
* Please copy the filesystem image, <IMAGENAME>-<MACHINE>.tar.gz, to a USB or
  MMC drive so that it can be installed on the target. If partup packages are
  used for initial flashing, then mount the partup package as type squashfs
  first and find the root filesystem there.
* The parameter <flashlayout> contains the rootfs partition.
* The parameter RAUC initializes both RAUC rootfs partitions.
* After the installation, power off the system:

.. code-block:: console

   target:~$ poweroff -f

* Restart the system. After a successful installation, the system will boot to
  the kernel login console.

Recover an Initialized Device
.............................

If your filesystem is damaged or the key blob is deleted, then you can
reinstall the encrypted filesystem with the following options.

   1. Reinitialize your device with the phytec-provisioning-image from the SD
      card (Boot in ramdisk)
   2. Boot in rescue mode of the existing flash image with minimal tools support

The following commands are for starting the rescue mode with a booted device
from eMMC:

   * Stop booting in the bootloader. The Protection Shield Level low is in
     default with password: root
   * Add Linux bootargs in the bootloader and boot the fitImage from the eMMC:

      * for barebox (i.MX6 and i.MX6UL)

      .. code-block::

         barebox$ global linux.bootargs.rescue="rescue=1"
         barebox$ boot

      * for u-boot:

      .. code-block::

         u-boot=> run loadraucimage
         u-boot=> run raucargs
         u-boot=> setenv bootargs ${bootargs} rescue=1
         u-boot=> bootm ${loadaddr}

.. include:: common/hardening.rsti
.. _physical-security-scarthgap:
.. include:: common/physical-security.rsti
.. _phytec-pki-scarthgap:
.. include:: common/phytec-pki.rsti
.. include:: common/vulnerabilities.rsti
.. include:: common/soc-configuration-tools.rsti
