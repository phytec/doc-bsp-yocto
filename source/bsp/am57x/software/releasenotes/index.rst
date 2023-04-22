.. _ReleaseNotes-57:

Release Notes
=============

This document highlights the key features and support included in the BSP-Yocto-TISDK-AM57xx-PD20.1.3 software release for the phyCORE-AM57x SOM and development kit.

.. list-table:: Board Support Package Status
   :widths: 50 50
   :stub-columns: 1

   * - BSP Operating system
     - Linux
   * - Release Status
     - **RELEASED**
   * - Release Date
     - 2022-10-04
   * - Repository
     - `PHYTEC Public Repos <https://stash.phytec.com/projects/PUB>`_
   * - Binaries
     - `BSP-Yocto-TISDK-AM57xx-PD20.1.3 <http://artifactory.phytec.com/artifactory/am57xx-images-released-public/BSP-Yocto-TISDK-AM57xx-PD20.1.3/>`_

New in this Release
-------------------

**U-Boot Bootloader**

* Add and enable ADIN1300 PHY support
* PCM-057-40300111I MACHINE support added

**Linux Kernel**

* Add and enable support for using external PCIe reference clock
* PCM-057-40300111I support added
* Add and enable support for Analog Devices ethernet PHYs, including ADIN1300

**Yocto**

* Fix git branch in iso-codes and lz4 recipes in meta-phytec
* PCM-057-40300111I support added (machine target am5728-pcm-057-40300111i) in meta-phytec-extra

Software Versioning
-------------------

The BSP-Yocto-TISDK-AM57xx-PD20.1.3 software release is mostly based off of TI's `v06.02.00.81 Processor SDK Linux <https://software-dl.ti.com/processor-sdk-linux/esd/docs/06_02_00_81/linux/Release_Specific_PLSDK_Release_Notes.html>`_ release and shares much of the same components and features.

.. list-table:: Software Versioning
   :widths: 50 50 75
   :stub-columns: 1

   * - Tested Build Environment
     - Ubuntu 18.04
     - `Ubuntu 18.04 Release Downloads <https://releases.ubuntu.com/18.04/>`_
   * - Linux Kernel
     - 4.19.79 (tag: BSP-Yocto-TISDK-AM57xx-PD20.1.3)
     - `PHYTEC Linux kernel repository <https://stash.phytec.com/projects/PUB/repos/linux-phytec-ti/browse?at=BSP-Yocto-TISDK-AM57xx-PD20.1.3>`_
   * - U-Boot Bootloader
     - 2019.01 (tag: BSP-Yocto-TISDK-AM57xx-PD20.1.3)
     - `PHYTEC U-Boot bootloader repository <https://stash.phytec.com/projects/PUB/repos/uboot-phytec/browse?at=BSP-Yocto-TISDK-AM57xx-PD20.1.3>`_
   * - Yocto
     - 2.6 (Thud) (tag: BSP-Yocto-TISDK-AM57xx-PD20.1.3)
     - `PHYTEC Meta Layer repository <https://stash.phytec.com/projects/PUB/repos/meta-phytec/browse?at=BSP-Yocto-TISDK-AM57xx-PD20.1.3>`_
   * - Qt	
     - 5.11.3
     - 
   * - OpenCL
     - 1.1.19
     - 
   * - OpenCV
     - 3.1
     - 
   * - Wayland
     - 1.16
     - 
   * - Gstreamer
     - 1.14.4
     - 
   * - TI-DL
     - 1.04.00
     - 
  
PHYTEC Meta Layer
-----------------

This BSP release supports the phyCORE-AM57x development kit which includes the PCM-057-41300111I SOM variant by default. The BSP allows for different SOMs to be used with the kit carrier board (PCM-948) depending on what is detected during boot. Here is a summary of the Yocto Machine Configuration support introduced in the PHYTEC Meta Layer for this release:

.. note::
  The MACHINE=am57xx-phycore-kit software will support all phyCORE-AM57x SOM variants. The SOM's on-board EEPROM is read during boot in order to load the appropriate software components for the detected SOM variant and falls back to a minimal configuration when the SOM variant is unknown.

  See Using the PHYTEC EEPROM Flashtool for more information.

.. list-table:: Yocto MACHINE Summary - Default Kit Software
   :widths: 25 25 25 25 25 25 25
   :header-rows: 1

   * - Yocto MACHINE
     - Description
     - Kit Part Numbers
     - Supported SOM Part Numbers
     - Compatible Modules
     - U-Boot defconfig
     - Included Device Tree Files
   * - **am57xx-phycore-kit**
     - Default Linux image for PHYTEC Development Kit
     - KPCM-057-L |br| KPCM-057-SYS
     - PCM-057-00001100I |br| PCM-057-10200110I |br| PCM-057-10201111I |br| PCM-057-10203110C |br| PCM-057-10203111I |br| PCM-057-11302111I |br| PCM-057-40200110C |br| PCM-057-40201111I |br| PCM-057-40300111I |br| PCM-057-40A00111I |br| PCM-057-41201111I |br| PCM-057-41300111I |br| PCM-057-50201111I |br| PCM-057-50500111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_defconfig
     - am5716-phycore-kit-10203110c.dtb |br| am5716-phycore-kit-10203111i.dtb |br| am5726-phycore-kit-00001100i.dtb |br| am5726-phycore-kit-10201111i.dtb |br| am5726-phycore-kit-40201111i.dtb |br| am5728-phycore-kit-40300111i.dtb |br| am5726-phycore-kit-41201111i.dtb |br| am5726-phycore-kit-50201111i.dtb |br| am5728-phycore-kit-10200110i.dtb |br| am5728-phycore-kit-40200110c.dtb |br| am5728-phycore-kit-40a00111i.dtb |br| am5728-phycore-kit-41300111i.dtb |br| am5728-phycore-kit-50500111i.dtb |br| am5729-phycore-kit-10306111i.dtb |br| am5746-phycore-kit-11305111i.dtb |br| am5748-phycore-kit-11304111i.dtb |br| am5749-phycore-kit-11302111i.dtb |br| am57xx-phycore-kit.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo     
   * - am57xx-phycore-kit-rt
     - Default Linux image for PHYTEC Development Kit - with Linux-RT patches
     - KPCM-057-L |br| KPCM-057-SYS
     - PCM-057-00001100I |br| PCM-057-10200110I |br| PCM-057-10201111I |br| PCM-057-10203110C |br| PCM-057-10203111I |br| PCM-057-11302111I |br| PCM-057-40200110C |br| PCM-057-40201111I |br| PCM-057-40300111I |br| PCM-057-40A00111I |br| PCM-057-41201111I |br| PCM-057-41300111I |br| PCM-057-50201111I |br| PCM-057-50500111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12 |br| 
     - am57xx_phycore_kit_defconfig
     - am5716-phycore-kit-10203110c.dtb |br| am5716-phycore-kit-10203111i.dtb |br| am5726-phycore-kit-00001100i.dtb |br| am5726-phycore-kit-10201111i.dtb |br| am5726-phycore-kit-40201111i.dtb |br| am5728-phycore-kit-40300111i.dtb |br| am5726-phycore-kit-41201111i.dtb |br| am5726-phycore-kit-50201111i.dtb |br| am5728-phycore-kit-10200110i.dtb |br| am5728-phycore-kit-40200110c.dtb |br| am5728-phycore-kit-40a00111i.dtb |br| am5728-phycore-kit-41300111i.dtb |br| am5728-phycore-kit-50500111i.dtb |br| am5729-phycore-kit-10306111i.dtb |br| am5746-phycore-kit-11305111i.dtb |br| am5748-phycore-kit-11304111i.dtb |br| am5749-phycore-kit-11302111i.dtb |br| am57xx-phycore-kit.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo

.. note::
  As an alternative to using the default kit software, you can use SOM specific software to only support the SOM variant you are working with. This would free up the EEPROM for user-specific applications.

.. list-table:: Yocto MACHINE Summary - Non-Standard SOM Configurations
   :widths: 25 25 25 25 25
   :header-rows: 1

   * - Yocto MACHINE
     - Supported SOM Part Number
     - Compatible Modules
     - U-Boot defconfig
     - Included Device Tree Files
   * - am5716-pcm-057-10203110c
     - PCM-057-10203110C
     - PCM-949 |br| PCM-957
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5716-phycore-kit-10203110c.dtb |br| am57xx-phytec-wlan-wilink8.dtbo 
   * - am5716-pcm-057-10203111i
     - PCM-057-10203111I
     - PCM-949 |br| PCM-957 
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5716-phycore-kit-10203111i.dtb |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5726-pcm-057-00001100i
     - PCM-057-00001100I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_128M16_x2_defconfig
     - am5726-phycore-kit-00001100i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5726-pcm-057-10201111i
     - PCM-057-10201111I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5726-phycore-kit-10201111i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5726-pcm-057-40201111i
     - PCM-057-40201111I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_256M16_x4_defconfig
     - am5726-phycore-kit-40201111i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5726-pcm-057-41201111i
     - PCM-057-41201111I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_256M16_x4_defconfig
     - am5726-phycore-kit-41201111i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5726-pcm-057-50201111i
     - PCM-057-50201111I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_512M16_x4_defconfig
     - am5726-phycore-kit-50201111i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-pcm-057-40a00111i
     - PCM-057-40A00111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12  
     - am5728_phycore_kit_nand_defconfig
     - am5728-phycore-kit-40a00111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-pcm-057-10200110i
     - PCM-057-10200110I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5728-phycore-kit-10200110i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-pcm-057-40200110c
     - PCM-057-40200110C
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_256M16_x4_defconfig
     - am5728-phycore-kit-40200110c.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-pcm-057-41300111i
     - PCM-057-41300111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_256M16_x4_defconfig
     - am5728-phycore-kit-41300111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-pcm-057-50500111i
     - PCM-057-50500111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_512M16_x4_defconfig
     - am5728-phycore-kit-50500111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5729-pcm-057-10306111i
     - PCM-057-10306111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5729-phycore-kit-10306111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5746-pcm-057-11305111i
     - PCM-057-11305111I
     - PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5746-phycore-kit-11305111i.dtb |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5748-pcm-057-11304111i
     - PCM-057-11304111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5748-phycore-kit-11304111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5749-pcm-057-11302111i
     - PCM-057-11302111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am57xx_phycore_kit_256M16_x2_defconfig
     - am5749-phycore-kit-11302111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo
   * - am5728-phycore-kit-40300111i
     - PCM-057-40300111I
     - LCD-018-070-KAP |br| PCM-949 |br| PCM-957 |br| VM-009-M12
     - am572x_phycore_kit_256M16_x4_defconfig
     - am5728-phycore-kit-40300111i.dtb |br| am57xx-phytec-lcd-018.dtbo |br| am57xx-phytec-vm-0xx.dtbo |br| am57xx-phytec-wlan-wilink8.dtbo

Part Number Summary
-------------------

.. list-table:: Hardware Summary
   :widths: 50 50 75 50
   :header-rows: 1

   * - Hardware Description
     - Part Number
     - Configuration Details (DDR3 / DDR ECC / eMMC or NAND / QSPI NOR / Controller / EEPROM / Ethernet PHY / RTC / Temp)
     - PCB Version
   * - phyCORE-AM57x SOM
     - PCM-057-10200110I.A0	
     - 1GB (1 bank) / No / 4GB eMMC / No / AM5728 / Yes / Yes / No / Industrial	
     - 1428.3
   * - 
     - PCM-057-10201111I.A0	
     - 1GB (1 bank) / No / 4GB eMMC / No / AM5726 / Yes / Yes / Yes / Industrial	
     - 1428.3
   * - 
     - PCM-057-10203111I.A0
     - 1GB (1 bank) / No / 4GB eMMC / No / AM5716 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-10306111I.A0
     - 1GB (1 bank) / No / 8GB eMMC / No / AM5729 / Yes / Yes / Yes / Industrial
     - 1428.5
   * - 
     - PCM-057-11302111I.A0
     - 1GB (1 bank) / Yes / 8GB eMMC / No / AM5749 / Yes / Yes / Yes / Industrial
     - 1428.5
   * - 
     - PCM-057-11304111I.A0
     - 1GB (1 bank) / Yes / 8GB eMMC / No / AM5748 / Yes / Yes / Yes / Industrial
     - 1428.5
   * - 
     - PCM-057-11305111I.A0
     - 1GB (1 bank) / Yes / 8GB eMMC / No / AM5746 / Yes / Yes / Yes / Industrial
     - 1428.5
   * - 
     - PCM-057-40200110C.A0
     - 2GB (2 banks) / No / 4GB eMMC / No / AM5728 / Yes / Yes / No / Commercial
     - 1428.3
   * - 
     - PCM-057-40201111I.A0
     - 2GB (2 banks) / No / 4GB eMMC / No / AM5726 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-40A00111I.A0
     - 2GB (2 banks) / No / 1GB NAND / No / AM5728 / Yes / Yes / Yes/ Industrial
     - 1428.3
   * - 
     - PCM-057-41201111I.A0
     - 2GB (2 banks) / Yes / 4GB eMMC / No / AM5726 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-41201111I.A1
     - 2GB (2 banks) / Yes / 4GB eMMC / No / AM5726 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-41300111I.A1
     - 2GB (2 banks) / Yes / 8GB eMMC / No / AM5728 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-41300111I.A2
     - 2GB (2 banks) / Yes / 8GB eMMC / No / AM5728 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-50201111I.A0
     - 4GB (2 banks) / No / 4GB eMMC / No / AM5726 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-50500111I.A0
     - 4GB (2 banks) / No / 32GB eMMC / No / AM5728 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - 
     - PCM-057-40300111I.A0
     - 2GB (2 banks) / No / 8GB eMMC / No / AM5728 / Yes / Yes / Yes / Industrial
     - 1428.3
   * - phyCORE-AM57x Carrier Board
     - PCM-948.A3
     - 
     - 1435.2
   * - 
     - PCM-948.A4
     - 
     - 1435.2
   * - 
     - PCM-948.A5
     - 
     - 1435.3
   * - phyCORE-AM57x Development Kit
     - KPCM-057-LINUX.A1
     - PCM-057-41300111I.A2 SOM + PCM-948.A5 Carrier Board (Default Kit)
     -      

Compatible Modules and Accessories
----------------------------------

.. list-table:: Compatible Add-Ons
   :widths: 50 50 50 75
   :header-rows: 1

   * - Module Name
     - Part Number
     - PCB Version
     - Description
   * - 7" Display with Capacitive Touch
     - LCD-018-070-KAP
     - 1365.1
     - EDT ETM0700G0DH6 TTL 7" display with capacitive touch
   * - Expansion Bus Prototyping Board
     - PCM-957
     - 1351.0
     - Expansion Bus Breakout and Prototype Board
   * - WiFi/Bluetooth Module
     - PCM-949
     - 1418.0
     - TI WiLink8 Module
   * - Camera Module
     - VM-009-M12
     - 1339.0
     - ON Semi MT9M131 Module     

Linux Device Tree Summary
-------------------------

This is a summary of how the device tree source files (.dts) and the various include files (.dtsi) are broken down in the kernel. These files describe the hardware in a hierarchical and modular way to the kernel, connecting device drivers to the interfaces brought out by the carrier board. This BSP also makes extensive use of device tree overlays (.dtso). This summary uses the Development Kit's default software (minimal configuration) as an example:

.. list-table:: Linux Device Tree Summary
   :widths: 50 75 50
   :header-rows: 1

   * - Hardware Target
     - Device Tree File Descriptions
     - Filename
   * - phyCORE-AM57x kit
     - Default dts Build Target (includes the other's below)
     - am57xx-phycore-kit.dts
   * - 
     - SOM (silicon-specific) - adds support and enables silicon-specific features
     - 	am571x-phycore-som.dtsi
   * - 
     - SOM Variant - adds support specific to the PCM-057-10203110C SOM variant
     - am5716-pcm-057-10203110c.dtsi
   * - 
     - Carrier Board (silicon-specific) - enables circuits supported by the silicon
     - am571x-pcm-948.dtsi
   * - 
     - WiLink8 WiFi Module overlay
     - am57xx-phytec-wlan-wilink8.dtso

Supported Interfaces
--------------------

The following table outlines the supported interfaces of the default phyCORE-AM57x development kit. The development kit carrier board implements as many interfaces as possible in order to allow users to evaluate a wide range of features supported by phyCORE-AM57x SOM. Due to there being a limit to the number of pins that can be brought out of the SoC and SOM, not all interfaces will be compatible with each other at the same time on the development kit implementation and some interfaces will have caveats for use.
















.. list-table:: Supported Interfaces
   :widths: 25 25 25 25 25 50 
   :header-rows: 1

   * - Interface
     - Detail
     - Implemented
     - Tested
     - Status in Device tree
     - Notes
   * - UART
     - uart0
     - Yes
     - Yes
     - Okay
     - Default serial console |br| - Connected to CP2105 header
   * -  
     - uart1
     - Yes
     - No
     - Reserved
     - Reserved for co-processor firmware usage
   * - 
     - mcu_uart0
     - Yes
     - Yes
     - Disabled
     - 
   * - I2C
     - i2c0
     - Yes
     - Yes
     - Okay
     - 
   * - 
     - i2c1
     - Yes
     - Yes
     - Okay  
     - 
   * - 
     - mcu_i2c0
     - Yes
     - Yes
     - Disabled
     - 
   * - 
     - mcu_i2c1
     - Yes
     - Yes
     - Disabled
     - 
   * - Ethernet
     - eth0 (cpsw ethernet)
     - Yes
     - Yes
     - Okay
     - DP83867IRRGZ SOM PHY
   * - 
     - eth1 (pru-icssg0 ethernet)
     - Yes
     - Yes
     - Okay
     - DP83867IRRGZ CB PHY
   * - 
     - eth2 (pru-icssg0 ethernet)
     - Yes
     - Yes
     - Okay
     - DP83867IRRGZ CB PHY
   * - eMMC/SD/SDIO
     - mmc0
     - Yes
     - Yes
     - Okay
     - eMMC Flash Memory on the SOM
   * - 
     - mmc1
     - Yes
     - Yes
     - Okay
     - SD Card Slot on Dev Kit Carrier Board
   * - USB
     - usb0
     - Yes
     - Yes
     - Okay
     - Connected to USB 3.0 HUB |br| - USB super speed signals (serdes0) muxed between USB HUB and mPCIe with device tree overlay |br| - USB2.0 speeds still supported when mPCIe enabled
   * - CAN
     - can0
     - Yes
     - Yes
     - Okay
     - Full Duplex CAN brought out to X2 10pin header
   * - 
     - can1
     - Yes
     - Yes
     - Okay
     - Full Duplex CAN brought out to X3 10pin header
   * - SPI
     - spi0
     - Yes
     - Yes
     - Okay
     - Connected to Infineon Trusted Platform Module (TPM) SLB9670
   * - OSPI
     - ospi0
     - Yes
     - Yes
     - Okay
     - NOR Serial Flash on SOM
   * - GPIO
     - User LEDs
     - Yes
     - Yes
     - Okay
     - User LEDs populated on SOM and Carrier Board
   * -  
     - User Buttons
     - Yes
     - No
     - No
     - 
   * - 
     - General Purpose
     - No
     - No
     - No
     - GPIOs can be configured "on the fly", See Blink and GPIO Peripheral Interface Guides
   * - Memory
     - SOM EEPROM
     - Yes
     - Yes
     - Okay
     - M24C32 on i2c0 
   * - 
     - Carrier Board EEPROM
     - Yes
     - Yes
     - Okay
     - M24C02 on i2c1
   * - 
     - OSPI NOR Flash
     - Yes
     - Yes
     - Okay
     - MT35XU512ABA
   * - RTC
     - SOM RTC
     - Yes
     - Yes
     - Okay
     - RV-3028-C7 on I2C0
   * - mPCIe
     - serdes0
     - Yes
     - Yes
     - Disabled
     - mPCIe at the X31 connector |br| - Enabled with device tree overlay |br| - serdes0 signals muxed between USB HUB and mPCIe
   * - PRU-ICSSG
     - pru_icssg0
     - Yes
     - Yes
     - Okay
     - Connected to eth1 and eth2 
   * -  
     - pru_icssg1
     - Yes
     - Yes
     - No
     - Supported with Pinger Lite Expansion Board

.. note:: 
  For technical support, please visit `PHYTEC's Support Portal <http://support.phytec.com/>`_!

.. |br| raw:: html

      <br>
