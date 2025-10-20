.. Download links
.. _`static-pdf-dl`: ../_static/head-sec.pdf

.. |secure-boot-link| replace:: :ref:`secure-boot-head`
.. |secure-key-storage-link| replace:: :ref:`secure-key-storage-head`
.. |phytec-pki-link| replace:: :ref:`phytec-pki-head`

.. Yocto
.. |branding-name| replace:: SECURIphy
.. |yocto-codename| replace:: Walnascar
.. |distro-secure-vendor| replace:: securiphy-vendor
.. |distro-secure| replace:: securiphy
.. |distro-provisioning| replace:: securiphy-provisioning
.. |distro-provisioning-vendor| replace:: securiphy-vendor-provisioning
.. |image-secure-name| replace:: phytec-securiphy-image


.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-----------------+----------------------------------+
| Security Manual |                                  |
+=================+==================================+
| Document Title  | Security Manual |yocto-codename| |
+-----------------+----------------------------------+
| Document Type   | Security Manual                  |
+-----------------+----------------------------------+
| Last modified   | XXXX/XX/XX                       |
+-----------------+----------------------------------+
| Is Branch of    | Security Manual                  |
+-----------------+----------------------------------+

+------------------+--------------+--------------+-----------+
|| Compatible BSPs || BSP Release || BSP Release || Security |
||                 || Type        || Date        || Support  |
||                 ||             ||             || Status   |
+==================+==============+==============+===========+
|                  |              |              |           |
+------------------+--------------+--------------+-----------+

This manual applies to all |yocto-codename| based PHYTEC releases.

Introduction
============

PHYTEC's Yocto distribution Securiphy (former Ampliphy-secure) supports
different Security mechanism. The security features have impact to the
bootloader, the Linux kernel, Device Tree, and root filesystem. This manual
describes how Security featuresis used and implemented on various PHYTEC
platforms. Note, that different modules use different bootloaders and flash
storage devices, which affects the way things are handled. Make sure to
read the correct sections fitting your platform.

.. note::

   This manual contains machine-specific paths and variable contents. Make sure
   you are using the correct machine and device names for your application when
   executing any commands.

.. _head-security-overview:
.. include:: common/security-overview.rsti

.. include:: common/distro-using.rsti
.. _secure-boot-head:
.. include:: common/secure-boot.rsti
.. include:: common/activate-secureboot.rsti
.. include:: common/kernel-module-signing.rsti
.. include:: common/devicetree-overlay.rsti
.. _secure-key-storage-head:
.. include:: common/secure-key-storage.rsti
.. include:: common/secure-storage.rsti
.. include:: common/hardening.rsti
.. include:: common/physical-security.rsti
.. _phytec-pki-head:
.. include:: common/phytec-pki.rsti
.. include:: common/vulnerabilities.rsti
.. include:: common/soc-configuration-tools.rsti
