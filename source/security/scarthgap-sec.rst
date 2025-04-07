.. Download links
.. _`static-pdf-dl`: ../_static/scarthgap-sec.pdf

.. Yocto
.. |yocto-codename| replace:: Scarthgap
.. |security-manual| replace:: Security Manual
.. |distro| replace:: securiphy-vendor

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
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.0 | Major        | 2024-04-02   |                   |
+-------------------------------------+--------------+--------------+-------------------+

This manual applies to all |yocto-codename| based PHYTEC releases.

Introduction
============

PHYTEC's Yocto distribution Securiphy (former Ampliphy-secure) supports different
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

.. _scarthgap-security-overview:
.. include:: common/security-overview.rsti


Enable SECURIphy
================

.. note::
   Distro securiphy-(vendor) and securiphy-(vendor)-provisioning are sample Yocto distros like ampliphy with additional security pre-configurations.
   Additional security measurements for production usage are necessary and depend on your threat model.

   PHYTEC services can support your implementation.

Distro securiphy-(vendor)
-------------------------

The distro securiphy-(vendor) with the phytec-security-image is an example of a production image with secure-update support.
The phytec-security-image.rootfs.wic or phytec-security-image.rootfs.partup can boot only from an eMMC!

For devices based on the TI K3 controller (AM6 series) the :code:`MACHINE` variable in the :code:`$BUILDDIR/conf/local.conf`
should be set to secure-machine-name.

Distro securiphy-(vendor)-provisioning
--------------------------------------

The distro securiphy-(vendor)-provisioning with the phytec-provisioning-image is for the production or the first initialization
of your device based on a NXP controller in a secure area.
The phytec-provisioning-image.rootfs can boot directly from an SD card to a Kernel with a minimal initramfs to

    * install the phytec-security-image.rootfs as wic or partup to the eMMC
    * initialize the secure key storage on the device
    * initialize the secure storage on the device

For devices based on the TI K3 controller (AM6 series) use the distro ampliphy and build the phytec-headless-image to boot
from sd-card. The :code:`MACHINE` variable in the :code:`$BUILDDIR/conf/local.conf` should be set to secure-machine-name.

The secure-machine-name for TI K3 controller
--------------------------------------------

The secure-machine-name is the machine with secure boot enabled, so it will be built with signed bootloaders.
For the TI K3 controller exist different machines for

    * General Purpose (GP): The device is not capable of secure operation
    * High Secure - Field Securable (HS-FS): is the state of a K3 device before it has been eFused with customer security keys.
    * High Secure - Security Enforced (HS-SE): devices enforce an authenticated boot flow for secure boot.

+----------------+---------------------------+---------------------------+
| Board          | HS-FS device              | HS-SE device              |
+================+===========================+===========================+
| phyCORE-AM62Ax | phyboard-lyra-am62axx-2   |                           |
+----------------+---------------------------+---------------------------+
| phyCORE-AM62x  | phyboard-lyra-am62xx-3    | phyboard-lyra-am62xx-4    |
+----------------+---------------------------+---------------------------+
| phyCORE-AM64x  | phyboard-electra-am64xx-2 | phyboard-electra-am64xx-3 |
+----------------+---------------------------+---------------------------+
| phyCORE-AM68x  | phyboard-izar-am68x-2     | phyboard-izar-am68x-3     |
+----------------+---------------------------+---------------------------+

For NXP controller based boards do not exists different machines for devices with activated and not activated
Secure boot, because signed images can be booted independence of the device state.

Enable securiphy Features in your own Distro
--------------------------------------------
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
.. include:: common/hardening.rsti
.. include:: common/phytec-pki.rsti
