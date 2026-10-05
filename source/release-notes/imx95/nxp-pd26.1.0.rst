.. |ref-bsp-man-imx95-fpsc| replace:: :ref:`here <imx95-fpsc-pd26.1.0_nxp-bsp-manual>`

=============================
BSP-Yocto-NXP-i.MX95-PD26.1.0
=============================

Release Notes
=============

- Linux kernel v6.18.20-2.0.0-phy7 (LTS kernel)
- U-Boot v2026.04-2.0.0-phy4
- System Manager 6.18.20-2.0.0-phy1
- Optional Executable Image 6.18.20-2.0.0-phy1
- Yocto 6.0 (wrynose)

Tested Yocto Images
-------------------
- phytec-chromium-image
- phytec-headless-image
- phytec-mfg-image
- phytec-provisioning-image
- phytec-qt6demo-image
- phytec-securiphy-image
- phytec-vision-image

Build Environment
-----------------
- Ubuntu 26.04 64-bit

Supported Machines
------------------
imx95-phyflex-libra-rdk-2

Changes
-------
- ON/OFF button can now be used to shut down the system from Linux
  (bug from ALPHA2 has been fixed)

New Features
------------
- Watchdog support (U-Boot and Linux)
- Suspend to RAM support
- CPU core deactivation (sleep) support
- Audio support (PEB-AV-10)
- SoM detection: read out and evaluates the factory EEPROM data on the
  SoM in OEI and U-Boot (prerequisite for the support of multiple RAM configurations)
- CAN (CAN FD) support
- USB-A 2.0 Host Ports (X16) in U-Boot
- ISP (Dewarping)
- UMS via USB-C Port (X18) in U-Boot
- Security support
  * Secure Boot
  * Secure Storage (Integrity, Encryption)
  * Secure Key Storage (TPM, TEE)
- RAUC update support

Other Features
--------------
- Boot from e.MMC
- Boot from SD card
- Boot via USB serial download (uuu)
- LVDS display support (onboard and PEB-AV-10)
- GPU support
- VPU support
- RTC support
- USB-A 2.0 host mode support
- Debug UART support
- GBit Ethernet support (SoM + Carrier board)
- Power Management support (frequency scaling)
- Thermal Management support
- U-Boot standard boot (https://docs.u-boot.org/en/v2026.04/develop/bootstd.html#u-boot-standard-boot)
- Camera support
    * VM-016 phyCAM-M / phyCAM-L
    * VM-017 phyCAM-M / phyCAM-L
    * VM-020 phyCAM-M / phyCAM-L
    * VM-024 phyCAM-M
- ISP support (Debayer, AEC, AWB)
- Chromium support (chromium image)
- ampliphy-boot
- RS232/485 support
- TPM support
- PWM fan support
- USB-C (X18) device and host mode support
- JTAG support (J-Link; A55 & M33)
- ON/OFF + Reset button support
- i2c device support (EEPROM, LEDs, GPIO expanders, temperature sensors)

Known Issues and Limitations
----------------------------
- GPU performance may be very low; As of release date, NXP is investigating
  this issue as it is present on their EVK as well. Our BSP documentation explains a workaround that
  yields better performance.
- Sporadic artifacts when capturing camera images with yavta
- when trying to write to non-optimal aligned blocks, e.MMC becomes unresponsive. Cause of this
  behaviour has not been determined, yet.
- writing to EEPROM needs 5ms delay between page writes, otherwise i2c transfer errors may be seen

i.MX 95 phyFLEX Libra RDK
=========================

The BSP Manual for i.MX 95 phyFLEX Libra RDK can be found
|ref-bsp-man-imx95-fpsc|.

Part Number Summary
-------------------

Hardware Summary
................

+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+
| Part Number        | Hardware Description      | Configuration Details (SoC / RAM / eMMC / NOR / Eth PHY / RTC / Temp Rating) | PCB Version |
+====================+===========================+==============================================================================+=============+
| PFL-G-02-PT002.A1  | i.MX95 phyFLEX-FPSC-G SoM | i.MX959 6x1.8GHz / 8GB / 64GB / - / Yes / Yes / Industrial                   | 1620.3      |
+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+
| PFL-G-02-SP001.A0  | i.MX95 phyFLEX-FPSC-G SoM | i.MX959 6x1.8GHz / 8GB / 64GB / - / Yes / Yes / Industrial                   | 1620.3      |
+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+
| PD-05032-001A.A2   | phyFLEX Libra SBC         | - / - / - / 64MB / - / - / - /                                               | 1618.2      |
+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+
| PD-05032-ALPHA.A2  | phyFLEX Libra SBC         | - / - / - / 64MB / - / - / - /                                               | 1618.2      |
+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+
| PD-05032-S-SP001.A0| phyFLEX Libra SBC         | - / - / - / 64MB / - / - / - /                                               | 1618.3      |
+--------------------+---------------------------+------------------------------------------------------------------------------+-------------+

Kit Summary
...........

+-----------------------+---------------------------+---------------------------------------------+
| Part Number           | Yocto Machine             | Hardware Description                        |
+=======================+===========================+=============================================+
| KPD-05032-ALPHA.A2    | imx95-phyflex-libra-rdk-2 | Libra i.MX95 ALPHA-KIT                      |
+-----------------------+---------------------------+---------------------------------------------+
| KPD-05032-Vid-L01.A2  | imx95-phyflex-libra-rdk-2 | Embed Imag Kit i.MX 95 Libra Linux L01      |
+-----------------------+---------------------------+---------------------------------------------+
| KPD-05032-Vid-L02.A2  | imx95-phyflex-libra-rdk-2 | Embed Imag Kit i.MX 95 Libra Linux L02      |
+-----------------------+---------------------------+---------------------------------------------+

Supported Boot Sources
......................

The following keywords might be used in the Status column:

-  Supported: Feature is tested and works.
-  Unsupported: Feature is not implemented.
-  Partly Supported: Some parts of the feature are supported, but not the full
   functionality. More detailed description is in the Notes column.
-  Untested: Feature has been implemented, but not or not fully tested/validated.
-  Broken: Feature has been implemented, but does not work due to a bug.

+------------------------+--------------------+--------------------+-------------------------------+
| Boot Source            | Release Status     | Upstream Status    | Notes                         |
+========================+====================+====================+===============================+
| eMMC                   | Supported          | Unsupported        |                               |
+------------------------+--------------------+--------------------+-------------------------------+
| SD-Card                | Supported          | Unsupported        |                               |
+------------------------+--------------------+--------------------+-------------------------------+
| SPI NOR Flash          | Unsupported        | Unsupported        |                               |
+------------------------+--------------------+--------------------+-------------------------------+
| Ethernet               | Supported          | Unsupported        | only kernel; no SFP+          |
+------------------------+--------------------+--------------------+-------------------------------+
| USB Serial downloader  | Supported          | Unsupported        | USB-C (X18)                   |
| (UUU)                  |                    |                    |                               |
+------------------------+--------------------+--------------------+-------------------------------+

Supported Features
..................

+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Feature                | Sub-Feature       | Release Status     | Upstream Status    | Notes                         |
+========================+===================+====================+====================+===============================+
| RAM / EEPROM Detection | 4 GB RAM          | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | 8 GB RAM          | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | 16 GB RAM         | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Read out and      | Supported          | Unsupported        |                               |
|                        | evaluate EEPROM   |                    |                    |                               |
|                        | data              |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | RAM detection     | Unsupported        | Unsupported        |                               |
|                        | and fallback      |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| eMMC                   |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| SD-Card                |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| SPI NOR Flash          |                   | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Ethernet               | SoM Ethernet      | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Board Ethernet    | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | SFP+              | Untested           | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Bootflow               | Extension Support | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | ampliphy-boot     | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Watchdog          | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| USB Serial downloader  |                   | Supported          | Unsupported        |                               |
| (UUU flash + boot)     |                   |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| USB-C (Host & Device)  |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| USB-A (Host)           |                   | Supported          | Unsupported        | USB 2.0 only                  |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| M.2 Key-E              | WiFi              | Untested           | Unsupported        | Intel AX210                   |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Bluetooth         | Untested           | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| M.2 Key-M              | SSD               | Untested           | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| LEDs                   |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| EEPROM                 |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| GPIO expanders         |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| RTC                    |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Temp Sensor            |                   | Unsupported        | Unsupported        |                               |
| (Baseboard i3c)        |                   |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Temp Sensor (SoM)      |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| RS485                  |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| RS232                  |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| CAN                    |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| LVDS On-Board          | AC209             | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| MIPI DSI               |                   | Unsupported        | Unsupported        | Not available on this hardware|
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| HDMI (PEB-AV-20)       |                   | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| PEB-AV-10              | LVDS AC209        | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Audio             | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| GPU                    |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| VPU                    |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| QT6 demo               |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| ADC                    | i.MX95 internal   | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| SPI Bus                | ADC               | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Suspend to RAM         |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Deactivate Cores       |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Frequency Scaling      |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Thermal Management     |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| JTAG                   |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| ON/OFF + Reset Button  |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| PWM Fan                |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Chromium               |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| NPU                    |                   | Untested           | Unsupported        | Basic support from NXP        |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Cortex M7 core         |                   | Unsupported        | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| MIPI-CSI 1 and 2       | vm-016 phyCAM-M   | Supported          | Unsupported        |                               |
| (phyCAM)               | vm-016 phyCAM-L   |                    |                    |                               |
|                        | vm-017 phyCAM-M   |                    |                    |                               |
|                        | vm-017 phyCAM-L   |                    |                    |                               |
|                        | vm-020 phyCAM-M   |                    |                    |                               |
|                        | vm-020 phyCAM-L   |                    |                    |                               |
|                        | vm-024 phyCAM-M   |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| ISP                    | Debayer           | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Auto White        | Supported          | Unsupported        |                               |
|                        | Balance           |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Auto Exposure     | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| Security               | Secure Boot       | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Secure Storage    | Supported          | Unsupported        |                               |
|                        | (Integrity,       |                    |                    |                               |
|                        | Encryption)       |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Secure Key        | Supported          | Unsupported        |                               |
|                        | Storage - TPM     |                    |                    |                               |
|                        | Support           |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
|                        | Secure Key        | Supported          | Unsupported        |                               |
|                        | Storage - TEE     |                    |                    |                               |
|                        | Support           |                    |                    |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
| RAUC                   |                   | Supported          | Unsupported        |                               |
+------------------------+-------------------+--------------------+--------------------+-------------------------------+
