.. Download links
.. _`static-pdf-dl`: ../_static/scarthgap-sec.pdf

.. |secure-key-storage-init-link| replace:: :ref:`secure-key-storage-init`

.. Yocto
.. |branding-name| replace:: SECURIphy
.. |yocto-codename| replace:: Scarthgap
.. |security-manual| replace:: Security Manual
.. |distro-secure-vendor| replace:: securiphy-vendor
.. |distro-secure| replace:: securiphy
.. |distro-provisioning| replace:: securiphy-provisioning
.. |distro-provisioning-vendor| replace:: securiphy-vendor-provisioning

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
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.0 | Major        | 2024-04-02   | none              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.1 | Minor        | 2024-04-09   | none              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX8MP-PD24.1.2 | Minor        | 2024-06-26   | none              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-NXP-i.MX8MP-PD24.1.0      | Major        | 2024-11-07   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-NXP-i.MX93-PD24.2.0       | Major        | 2024-10-08   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-NXP-i.MX93-PD24.2.1       | Minor        | 2025-03-21   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-i.MX6UL-PD24.1.0 | Major        | 2024-07-19   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM62Ax-PD24.1.0  | Major        | 2024-06-27   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM62Ax-PD24.1.2  | Minor        | 2025-03-24   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM62x-PD24.1.0   | Major        | 2024-06-27   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM62x-PD24.1.2   | Minor        | 2025-03-19   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM64x-PD24.1.0   | Major        | 2024-06-27   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM64x-PD24.1.1   | Minor        | 2024-12-19   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-Ampliphy-AM64x-PD25.1.0   | Major        | 2025-03-24   | partly            |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-NXP-i.MX8MM-PD25.1.0      | Major        | 2025-03-28   | full              |
+-------------------------------------+--------------+--------------+-------------------+
| BSP-Yocto-NXP-i.MX91-PD24.2.1       | Major        | 2025-03-21   | none              |
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

.. include:: common/distro-using.rsti
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
.. include:: common/vulnerabilities.rsti
