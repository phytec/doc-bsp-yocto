.. Download links
.. _`static-pdf-dl`: ../_static/wrynose-sec.pdf

.. |secure-boot-link| replace:: :ref:`secure-boot-wrynose`
.. |activate-secureboot-link| replace:: :ref:`activate-secureboot-wrynose`
.. |secure-key-storage-link| replace:: :ref:`secure-key-storage-wrynose`
.. |physical-security-link| replace:: :ref:`physical-security-wrynose`
.. |phytec-pki-link| replace:: :ref:`phytec-pki-wrynose`
.. |provisioning-scripts-link| replace:: :ref:`provisioning-scripts-wrynose`

.. Yocto
.. |branding-name| replace:: securiPHY
.. |yocto-codename| replace:: Wrynose
.. |distro-secure-vendor| replace:: securiphy-vendor
.. |distro-secure| replace:: securiphy
.. |distro-provisioning| replace:: securiphy-provisioning
.. |distro-provisioning-vendor| replace:: securiphy-vendor-provisioning
.. |image-secure-name| replace:: phytec-securiphy-image
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual <yocto-man-wrynose>`
.. |rauc-manual| replace:: :ref:`Phytec RAUC Manual <rauc-man-wrynose>`

==========================================
|yocto-codename| -- |branding-name| Manual
==========================================

.. sectnum::

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+--------------------------------+--------------+--------------+-----------+
|| Compatible BSPs               || BSP Release || BSP Release || Security |
||                               || Type        || Date        || Support  |
||                               ||             ||             || Status   |
+================================+==============+==============+===========+
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
.. _secure-boot-wrynose:
.. include:: common/secure-boot.rsti
.. _provisioning-scripts-wrynose:
.. include:: common/provisioning-scripts.rsti
.. _activate-secureboot-wrynose:
.. include:: common/activate-secureboot.rsti
.. include:: common/kernel-module-signing.rsti
.. include:: common/devicetree-overlay.rsti
.. _secure-key-storage-wrynose:
.. include:: common/secure-key-storage.rsti
.. include:: common/secure-storage.rsti
.. include:: common/recover-securiphy.rsti
.. include:: common/hardening.rsti
.. _physical-security-wrynose:
.. include:: common/physical-security.rsti
.. _phytec-pki-wrynose:
.. include:: common/phytec-pki.rsti
.. include:: common/vulnerabilities.rsti
.. include:: common/soc-configuration-tools.rsti
