.. Download links
.. _`static-pdf-dl`: ../_static/rauc-walnascar.pdf

.. RAUC
.. |yocto-codename| replace:: Walnascar
.. |rauc-manual| replace:: RAUC Update & Device Management Manual

.. References
.. |ref-rauc-switch-keyrings| replace:: :ref:`walnascar_rauc-switch-keyrings`
.. |ref-rauc-use-case-usb-update| replace:: :ref:`walnascar_rauc-use-case-usb-update`
.. |ref-rauc-use-case-http-streaming| replace:: :ref:`walnascar_rauc-use-case-http-streaming`
.. |ref-yocto-bsp-customization| replace:: :ref:`walnascar_bsp-customization`

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
| Last Modified         | 2026-01-29                            |
+-----------------------+---------------------------------------+
| Is Branch of          | |rauc-manual|                         |
+-----------------------+---------------------------------------+

+-------------------------------------+------------------+------------------+----------------+
| Compatible BSPs                     | BSP Release Type | BSP Release Date | BSP Status     |
+=====================================+==================+==================+================+
| BSP-Yocto-NXP-i.MX8MP-PD26.1.0      | Major            | TBD              | in development |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-NXP-i.MX91-PD26.1.0       | Major            | TBD              | in development |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-NXP-i.MX93-PD26.1.0       | Major            | TBD              | in development |
+-------------------------------------+------------------+------------------+----------------+
| BSP-Yocto-NXP-i.MX95-ALPHA2         | Major            | TBD              | in development |
+-------------------------------------+------------------+------------------+----------------+

This manual was tested using the Yocto version |yocto-codename|.

.. include:: common/intro.rsti
.. include:: common/system-config.rsti
.. include:: common/design-considerations.rsti
.. include:: common/initial-setup.rsti
.. include:: common/creating-bundles.rsti
.. include:: common/updating.rsti
.. _walnascar_rauc-switch-keyrings:
.. include:: common/switch-keyrings.rsti

Use Case Examples
=================
.. _walnascar_rauc-use-case-usb-update:
.. include:: common/use-case/usb-update.rsti
.. include:: common/use-case/downgrade-barrier.rsti
.. _walnascar_rauc-use-case-http-streaming:
.. include:: common/use-case/http-streaming.rsti
.. include:: common/use-case/adaptive-updates.rsti

.. include:: common/reference.rsti
