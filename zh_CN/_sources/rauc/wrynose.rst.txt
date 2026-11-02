.. Download links
.. _`static-pdf-dl`: ../_static/rauc-wrynose.pdf

.. RAUC
.. |yocto-codename| replace:: Wrynose
.. |rauc-manual| replace:: RAUC Update & Device Management Manual

.. References
.. |ref-rauc-switch-keyrings| replace:: :ref:`wrynose_rauc-switch-keyrings`
.. |ref-rauc-use-case-usb-update| replace:: :ref:`wrynose_rauc-use-case-usb-update`
.. |ref-rauc-use-case-http-streaming| replace:: :ref:`wrynose_rauc-use-case-http-streaming`
.. |ref-yocto-bsp-customization| replace:: :ref:`wrynose_bsp-customization`

===============================
|yocto-codename| -- RAUC Manual
===============================

.. sectnum::

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+-------------------------------------+------------------+------------------+----------------+
| Compatible BSPs                     | BSP Release Type | BSP Release Date | BSP Status     |
+=====================================+==================+==================+================+
| BSP-Yocto-Ampliphy-AM62x-PD26.1.0   | Major            | 2026/09/29       | Released       |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-Ampliphy-AM62Ax-PD26.1.0  | Major            | 2026/10/01       | Released       |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-Ampliphy-AM62Px-PD26.1.0  | Major            | 2026/10/01       | Released       |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-Ampliphy-AM64x-PD26.1.0   | Major            | 2026/09/30       | Released       |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-Ampliphy-AM67x-PD26.1.0   | Major            | 2026/10/01       | Released       |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-NXP-i.MX95-PD26.1.0       | Major            | 2026/10/01       | Released       |
+-------------------------------------+------------------+------------------+----------------+

This manual was tested using the Yocto version |yocto-codename|.

.. _rauc-man-wrynose:

.. include:: common/intro.rsti
.. include:: common/system-config.rsti
.. include:: common/design-considerations.rsti
.. include:: common/initial-setup.rsti
.. include:: common/creating-bundles.rsti
.. include:: common/updating.rsti
.. _wrynose_rauc-switch-keyrings:
.. include:: common/switch-keyrings.rsti

Use Case Examples
=================
.. _wrynose_rauc-use-case-usb-update:
.. include:: common/use-case/usb-update.rsti
.. include:: common/use-case/downgrade-barrier.rsti
.. _wrynose_rauc-use-case-http-streaming:
.. include:: common/use-case/http-streaming.rsti
.. include:: common/use-case/adaptive-updates.rsti

.. include:: common/reference.rsti
