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
.. include:: common/hardening.rsti
.. _physical-security-scarthgap:
.. include:: common/physical-security.rsti
.. _phytec-pki-scarthgap:
.. include:: common/phytec-pki.rsti
.. include:: common/vulnerabilities.rsti
.. include:: common/soc-configuration-tools.rsti
