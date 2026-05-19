.. Download links
.. _`static-pdf-dl`: ../_static/walnascar-sec.pdf

.. |secure-boot-link| replace:: :ref:`secure-boot-walnascar`
.. |activate-secureboot-link| replace:: :ref:`activate-secureboot-walnascar`
.. |secure-key-storage-link| replace:: :ref:`secure-key-storage-walnascar`
.. |physical-security-link| replace:: :ref:`physical-security-walnascar`
.. |phytec-pki-link| replace:: :ref:`phytec-pki-walnascar`
.. |provisioning-scripts-link| replace:: :ref:`provisioning-scripts-walnascar`

.. Yocto
.. |branding-name| replace:: securiPHY
.. |yocto-codename| replace:: Walnascar
.. |distro-secure-vendor| replace:: securiphy-vendor
.. |distro-secure| replace:: securiphy
.. |distro-provisioning| replace:: securiphy-provisioning
.. |distro-provisioning-vendor| replace:: securiphy-vendor-provisioning
.. |image-secure-name| replace:: phytec-securiphy-image
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual <yocto-man-walnascar>`
.. |rauc-manual| replace:: :ref:`Phytec RAUC Manual <rauc-man-walnascar>`

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+--------------------------------+--------------+--------------+-----------+
|| Compatible BSPs               || BSP Release || BSP Release || Security |
||                               || Type        || Date        || Support  |
||                               ||             ||             || Status   |
+================================+==============+==============+===========+
| BSP-Yocto-NXP-i.MX91-PD26.1.0  | Major        | 2026-03-30   | full      |
+--------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX93-PD26.1.0  | Major        | 2026-03-30   | full      |
+--------------------------------+--------------+--------------+-----------+
| BSP-Yocto-NXP-i.MX8MP-PD26.1.0 | Major        | 2026-06-10   | full      |
+--------------------------------+--------------+--------------+-----------+

This manual applies to all |yocto-codename| based PHYTEC releases.

.. note::

   This manual contains machine-specific paths and variable contents. Make sure
   you are using the correct machine and device names for your application when
   executing any commands.

.. include:: common/introduction.rsti
.. include:: common/provisioning.rsti
.. include:: common/booting-securiphy.rsti
.. include:: common/key-management.rsti
.. include:: common/build-securiphy.rsti
.. include:: common/update-securiphy.rsti
.. _secure-boot-walnascar:
.. include:: common/secure-boot.rsti
.. _provisioning-scripts-walnascar:
.. include:: common/provisioning-scripts.rsti
.. _activate-secureboot-walnascar:
.. include:: common/activate-secureboot.rsti
.. include:: common/kernel-module-signing.rsti
.. include:: common/devicetree-overlay.rsti
.. _secure-key-storage-walnascar:
.. include:: common/secure-key-storage.rsti
.. include:: common/secure-storage.rsti
.. include:: common/recover-securiphy.rsti
.. include:: common/hardening.rsti
.. _physical-security-walnascar:
.. include:: common/physical-security.rsti
.. _phytec-pki-walnascar:
.. include:: common/phytec-pki.rsti
.. include:: common/vulnerabilities.rsti
.. include:: common/soc-configuration-tools.rsti
