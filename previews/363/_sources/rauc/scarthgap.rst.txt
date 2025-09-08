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
.. include:: common/initial-setup.rsti
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

.. include:: common/reference.rsti
