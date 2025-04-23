.. Download links
.. _`static-pdf-dl`: ../_static/kirkstone-sec.pdf

.. Yocto
.. |yocto-codename| replace:: Kirkstone
.. |security-manual| replace:: Security Manual
.. |distro| replace:: ampliphy-vendor-secure

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+------------------------------------------------------------+
| |security-manual|                                          |
+=======================+====================================+
| Document Title        | |security-manual| |yocto-codename| |
+-----------------------+------------------------------------+
| Document Type         | Security Manual                    |
+-----------------------+------------------------------------+
| Release Date          | XXXX/XX/XX                         |
+-----------------------+------------------------------------+
| Is Branch of          | |security-manual|                  |
+-----------------------+------------------------------------+

+-------------------------------------+--------------+--------------+-------------------+
|| Compatible BSPs                    || BSP Release || BSP Release || Security Support |
||                                    || Type        || Date        || Status           |
+=====================================+==============+==============+===================+
| BSP-Yocto-Ampliphy-i.MX6-PD22.1.0   | Major        | 14.12.2022   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX6-PD22.1.1   | Minor        | 20.06.2023   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX6UL-PD22.1.0 | Major        | 11.08.2022   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX6UL-PD22.1.1 | Minor        | 23.05.2023   | full              |
+-------------------------------------+--------------+--------------+-------------------+

This manual applies to all |yocto-codename| based PHYTEC releases.

Introduction
============

PHYTEC's Yocto distribution Ampliphy (former Yogurt) supports different
Security mechanism. The security features have inpact to the bootloader,
the Linux kernel, Device Tree, and root filesystem.
This manual describes how Security featuresis used and implemented on various
PHYTEC platforms. Note, that different modules use different bootloaders and flash
storage devices, which affects the way things are handled. Make sure to
read the correct sections fitting your platform.

.. note::

   This manual contains machine-specific paths and variable contents. Make sure
   you are using the correct machine and device names for your application when
   executing any commands.

.. _kirkstone-security-overview:
.. include:: common/security-overview.rsti

Enable Security
===============

.. note::
   Distro ampliphy-(vendor)-secure and ampliphy-(vendor)-provisioning are sample Yocto distros like ampliphy with additional security pre-configurations.
   Additional security measurements for production usage are necessary and depend on your threat model.

   PHYTEC services can support your implementation.

Distro ampliphy-(vendor)-secure
-------------------------------

The distro ampliphy-(vendor)-secure with the phytec-security-image is an example of a production image with secure-update support.
The phytec-security-image.rootfs.wic or phytec-security-image.rootfs.partup can boot only from an eMMC!

Distro ampliphy-(vendor)-provisioning
-------------------------------------

The distro ampliphy-(vendor)-provisioning with the phytec-provisioning-image is for the production or the first initialization
of your device in a secure area.
The phytec-provisioning-image.rootfs can boot directly from an SD card to a Kernel with a minimal initramfs to

    * install the phytec-security-image.rootfs as wic or partup to the eMMC
    * initialize the secure key storage on the device
    * initialize the secure storage on the device

Enable Security Features in your own Distro
-------------------------------------------
Activate the following DISTRO_FEATURES in your distrobution

+-----------------+----------------------------------------------------------------+
| DISTRO_FEATURES | Description                                                    |
+=================+================================================================+
| secureboot      | for building a signed bootloader and kernel FIT-Image          |
+-----------------+----------------------------------------------------------------+
| securestorage   || All necessary tools and configurations for file encryption and|
|                 || integrity initialization on the board                         |
+-----------------+----------------------------------------------------------------+
| protectionshield| * Three levels low, medium, and high                           |
|                 | * Four examples:  users root, phyadmin, phyuser, phyread       |
|                 | * Password protection for bootloader and kernel serial and ssh |
+-----------------+----------------------------------------------------------------+
| hardening       | Example kernel reduction for machine features                  |
+-----------------+----------------------------------------------------------------+
| kernelmodsign   || Enabled Linux kernel module signing, so only modules signed   |
|                 || with a specific key can be loaded.                            |
+-----------------+----------------------------------------------------------------+
| update          | Activate rauc A/B update system                                |
+-----------------+----------------------------------------------------------------+

.. include:: common/secure-boot.rsti
.. include:: common/activate-secureboot.rsti
.. include:: common/kernel-module-signing.rsti
.. include:: common/devicetree-overlay.rsti
.. include:: common/secure-key-storage.rsti
.. include:: common/secure-storage.rsti
.. include:: common/hardening.rsti
.. include:: common/physical-security.rsti
.. include:: common/soc-configuration-tools.rsti
.. include:: common/phytec-pki.rsti
