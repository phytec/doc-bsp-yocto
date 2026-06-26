.. Download links
.. |dlpage-bsp-91| replace:: i.MX 91 BSP
.. _dlpage-bsp-91: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX91-PD26.1.0
.. |dlpage-bsp-93| replace:: i.MX 93 BSP
.. _dlpage-bsp-93: https://www.phytec.de/bsp-download/?bsp=BSP-Yocto-NXP-i.MX93-PD26.1.0
.. |dlpage-bsp-link| replace:: our |dlpage-bsp-91|_ or |dlpage-bsp-93|_
.. |dlpage-product| replace:: https://www.phytec.de/produkte/system-on-modules/phycore-imx-91-93/#downloads
.. |dl-server| replace:: `i.MX 91 BSP downloads <dl-server-91_>`_ or `i.MX 93 BSP downloads <dl-server-93_>`_
.. |dl-server-91| replace:: i.MX 91
.. _dl-server-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/
.. |dl-server-93| replace:: i.MX 93
.. _dl-server-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/
.. |dl-server-link| replace:: |dl-server-91|_ or |dl-server-93|_ BSP downloads
.. |dl-sdk-91| replace:: i.MX 91 SDK
.. _dl-sdk-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD26.1.0/sdk/ampliphy-vendor/
.. |dl-sdk-93| replace:: i.MX 93 SDK
.. _dl-sdk-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/sdk/ampliphy-vendor/
.. |dl-sdk-link| replace:: |dl-sdk-91|_ or |dl-sdk-93|_ downloads
.. |link-image| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx93-2/phytec-qt6demo-image-phyboard-segin-imx93-2.rootfs.wic.xz
.. |link-partup-package| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx93-2/phytec-qt6demo-image-phyboard-segin-imx93-2.rootfs.partup
.. |link-boot-tools| replace:: for |link-boot-tools-91|_ or for |link-boot-tools-93|_
.. |link-boot-tools-91| replace:: i.MX 91
.. _link-boot-tools-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx91-1/imx-boot-tools/
.. |link-boot-tools-93| replace:: i.MX 93
.. _link-boot-tools-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx93-2/imx-boot-tools/
.. |link-bsp-images| replace:: for |link-bsp-images-91|_ or for |link-bsp-images-93|_
.. |link-bsp-images-91| replace:: i.MX 91
.. _link-bsp-images-91: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX91/BSP-Yocto-NXP-i.MX91-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx91-1/
.. |link-bsp-images-93| replace:: i.MX 93
.. _link-bsp-images-93: https://download.phytec.de/Software/Linux/BSP-Yocto-i.MX93/BSP-Yocto-NXP-i.MX93-PD26.1.0/images/ampliphy-vendor/phyboard-segin-imx93-2/
.. _`static-pdf-dl`: ../../../_static/imx93-head.pdf

.. _releasenotes: https://git.phytec.de/phy2octo/tree/releasenotes?h=imx93

.. General Substitutions
.. |kit| replace:: **phyBOARD-Segin i.MX 93 and phyBOARD-Nash i.MX 93 Kit**
.. |kit-ram-size| replace:: 1GiB
.. |sbc| replace:: phyBOARD-Segin/Nash i.MX 91/93
.. |sbc-segin| replace:: phyBOARD-Segin i.MX 91/93
.. |sbc-segin-91| replace:: phyBOARD-Segin i.MX 91
.. |sbc-segin-93| replace:: phyBOARD-Segin i.MX 93
.. |sbc-nash| replace:: phyBOARD-Nash i.MX 93
.. |soc| replace:: i.MX 93
.. |socfamily| replace:: i.MX 9
.. |som| replace:: phyCORE-|soc|
.. |debug-uart| replace:: ttyLP0
.. |serial-uart| replace:: ttyLP6
.. |bluetooth-uart| replace:: UART5
.. |expansion-connector| replace:: X16
.. |netboot-script| replace:: net_boot_fit.scr.uimg
.. |can0-interface| replace:: can0
.. |can-network-file| replace:: 11-can.network

.. Linux Kernel
.. |kernel-defconfig| replace:: imx9_phytec_defconfig
.. |kernel-primary-ethernet| replace:: end0
.. |kernel-recipe-path| replace:: meta-phytec/recipes-kernel/linux/linux-phytec-imx_*.bb
.. |kernel-repo-name| replace:: linux-phytec-imx
.. |kernel-repo-url| replace:: git://github.com/phytec/linux-phytec-imx.git
.. |kernel-socname| replace:: imx93
.. |kernel-tag| replace:: v6.12.34-2.1.0-phy9
.. |emmcdev| replace:: mmcblk0

.. Bootloader
.. |bootloader-offset| replace:: 32
.. |bootloader-offset-boot-part| replace:: 0
.. |u-boot-mmc-flash-offset| replace:: 0x40
.. |u-boot-emmc-devno| replace:: 0
.. |u-boot-defconfig| replace:: imx93-phycore_defconfig
.. |u-boot-multiple-defconfig-note| replace:: In command above replace ``<defconfig>`` with ``imx93-phycore_defconfig`` or ``imx91-phycore_defconfig``
.. |u-boot-multiple-dtb-note| replace:: In command above replace ``<dtb>`` with ``imx93-phyboard-segin.dtb``
.. |u-boot-imx-mkimage-tag| replace:: lf-6.12.34_2.1.0
.. |u-boot-soc-name| replace:: iMX9
.. |u-boot-recipe-path| replace:: meta-phytec/recipes-bsp/u-boot/u-boot-imx_*.bb
.. |u-boot-repo-name| replace:: u-boot-imx
.. |u-boot-repo-url| replace:: git://github.com/phytec/u-boot-imx.git

.. IMX93 specific
.. |u-boot-socname-config| replace:: PHYCORE_IMX93
.. |u-boot-tag| replace:: v2025.04-2.1.0-phy9

.. Devicetree
.. |dt-carrierboard| replace:: imx93-phyboard-segin
.. |dt-som| replace:: imx93-phycore-som
.. |dtbo-rpmsg| replace:: ``imx93-phycore-rpmsg.dtbo``
.. |dtbo-npu| replace:: ``imx93-phycore-npu.dtbo``

.. IMX93 specific
.. |dt-somnet-91| replace:: phyCORE i.MX 91
.. _dt-somnet-91: https://github.com/phytec/linux-phytec-imx/blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L56
.. |dt-somnet-93| replace:: phyCORE i.MX 93
.. _dt-somnet-93: https://github.com/phytec/linux-phytec-imx/blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L61
.. |dt-somnetwork| replace:: for |dt-somnet-91|_ or |dt-somnet-93|_

.. Yocto
.. |yocto-bootenv-link| replace:: :yocto-bootenv:`walnascar`
.. use imx93 as default BSP name
.. |yocto-bsp-name| replace:: BSP-Yocto-i.MX93
.. _yocto-bsp-name: `dl-server-93`_
.. |yocto-codename| replace:: Walnascar
.. |yocto-distro| replace:: ampliphy-vendor
.. |yocto-imagename| replace:: phytec-qt6demo-image
.. |yocto-imageext| replace:: wic.xz
.. use imx93 as default machinename
.. |yocto-machinename| replace:: phyboard-segin-imx93-2
.. use imx93 manifest as default manifestname
.. |yocto-manifestname| replace:: BSP-Yocto-NXP-i.MX93-PD26.1.y
.. and define explicitly imx91 and imx93 manifestname for more specific cases
.. |yocto-manifestname-91| replace:: BSP-Yocto-NXP-i.MX91-PD26.1.y
.. |yocto-manifestname-93| replace:: BSP-Yocto-NXP-i.MX93-PD26.1.y
.. |yocto-ref-manual| replace:: :ref:`Yocto Reference Manual (walnascar) <yocto-man-walnascar>`
.. |yocto-sdk-rev| replace:: 5.2.2
.. |yocto-sdk-a-core| replace:: cortexa55

.. Ref Substitutions
.. |ref-bootswitch| replace:: :ref:`bootmode switch (S3) <imx93-head-bootswitch>`
.. |ref-bsp-images| replace:: :ref:`BSP Images <imx93-head-images>`
.. |ref-debugusbconnector| replace:: UART1 console on PEB-EVAL-01 for **phyBOARD-Segin** and X-37
   USB-C debug for **phyBOARD-Nash**
.. |ref-dt| replace:: :ref:`device tree <imx93-head-device-tree>`
.. |ref-supported-hardware| replace:: :ref:`Supported Hardware <imx93-head-supported-hardware>`
.. |ref-getting-started| replace:: :ref:`Getting Started <imx93-head-getting-started>`
.. |ref-network| replace:: :ref:`Network Environment Customization <imx93-head-network>`
.. |ref-setup-network-host| replace:: :ref:`Setup Network Host <imx93-head-development>`
.. |ref-usb-otg| replace:: :ref:`X8 (USB micro/OTG connector) <imx93-head-components>`

.. IMX93 specific
.. |sbc-network| replace::
   The device tree set up for EQOS Ethernet IP core where the PHY is populated
   can be found here: for |dt-sbcnet-91-segin|_ or |dt-sbcnet-93-segin|_ or |dt-sbcnet-93-nash|_
.. |dt-sbcnet-91-segin| replace:: phyBOARD-Segin i.MX 91
.. _dt-sbcnet-91-segin: https://github.com/phytec/linux-phytec-imx/blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L113
.. |dt-sbcnet-93-segin| replace:: phyBOARD-Segin i.MX 93
.. _dt-sbcnet-93-segin: https://github.com/phytec/linux-phytec-imx/blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L114
.. |dt-sbcnet-93-nash| replace:: phyBOARD-Nash i.MX 93
.. _dt-sbcnet-93-nash: https://github.com/phytec/linux-phytec-imx/blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L93

.. |ubootexternalenv| replace:: U-boot External Environment subsection of the
   :ref:`device tree overlay section <imx93-head-ubootexternalenv>`

.. M-Core specific
.. |mcore| replace:: M33 Core
.. |ref-m-core-connections| replace:: :ref:`X16 <imx93-head-components>`
.. |mcore-jtag-dev| replace:: MIMX8MM6_M4
.. |mcore-sdk-version| replace:: 2.13.0

.. |jtag-target-interface| replace:: S
.. |jtag-soc-doc-link| replace:: https://kb.segger.com/NXP_i.MX_93

.. Powerkey specific
.. |powerkey-driver| replace:: bbnsm_pwrkey
.. |systemd-logind-conf-path-powerkey| replace:: ``/usr/lib/systemd/logind.conf.d/00-systemd-conf-imx.conf``
.. |powerkey-input-dev| replace:: 44440000.bbnsm\:pwrkey
.. |powerkey-keycode-property| replace:: linux,code

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

The table below shows the Compatible BSPs for this manual:

======================= ================ ============= ================ ===========
Compatible BSPs         BSP Release Type Yocto Version BSP Release Date BSP Status

======================= ================ ============= ================ ===========
|yocto-manifestname-91| Head                           ----/--/--       Development
|yocto-manifestname-93| Head                           ----/--/--       Development
======================= ================ ============= ================ ===========

.. include:: ../../intro.rsti

.. _imx93-head-supported-hardware:

Supported Hardware
------------------

On our web page, you can see all supported Machines with the available Article
Numbers for this release: |yocto-manifestname-91| see `download <dlpage-bsp-91_>`_,
or |yocto-manifestname-93| see `download <dlpage-bsp-93_>`_.

If you choose a specific **Machine Name** in the section **Supported Machines**,
you can see which **Article Numbers** are available under this machine and also
a short description of the hardware information. In case you only have
the **Article Number** of your hardware, you can leave the **Machine
Name** drop-down menu empty and only choose your **Article Number**. Now it
should show you the necessary **Machine Name** for your specific hardware.

.. tip::

   **Console examples in this BSP manual only focus on phyBOARD-Segin i.MX 93.
   Similar commands can also be executed for/on phyBOARD-Nash i.MX 93**

.. _imx93-head-components:
.. include:: components.rsti

.. +---------------------------------------------------------------------------+
.. Getting Started
.. +---------------------------------------------------------------------------+

.. _imx93-head-getting-started:
.. include:: /bsp/getting-started.rsti

First Start-up
--------------

*  To boot from an SD card, the |ref-bootswitch| needs to be set to the
   following position:

   .. image:: /bsp/images/dipswitch-4-1100.svg
      :scale: 400%

*  Insert the SD card
*  Connect the targets debug console with your host.
   Use |ref-debugusbconnector|.
*  Power up the board
*  Open serial/usb port with 115200 baud and 8N1 (you should see u-boot/linux
   start on the console

.. +---------------------------------------------------------------------------+
.. Building the BSP
.. +---------------------------------------------------------------------------+

.. include:: /bsp/building-bsp.rsti

.. _imx93-head-images:

*  **u-boot.bin**: Binary compiled U-boot bootloader (U-Boot). Not the final
   Bootloader image!
*  **oftree**: Default kernel device tree
*  **u-boot-spl.bin**: Secondary program loader (SPL)
*  **bl31-imx93.bin** or **bl31-imx91.bin**: ARM Trusted Firmware binary
*  **lpddr4_dmem_1d_v202201.bin, lpddr4_dmem_2d_v202201.bin,
   lpddr4_imem_1d_v202201.bin,
   lpddr4_imem_2d_v202201.bin**: DDR PHY firmware images
*  **imx-boot**: Bootloader build by imx-mkimage which includes SPL, U-Boot, ARM
   Trusted Firmware and DDR firmware. This is the final bootloader image which
   is bootable.
*  **fitImage**: Linux kernel FIT image
*  **fitImage.its**
*  **Image**: Linux kernel image
*  **Image.config**: Kernel configuration
*  **imx93-phyboard-*.dtb** or **imx91-phyboard-*.dtb**: Kernel device tree file
*  **imx93-phy\*.dtbo** or **imx91-phy\*.dtbo**: Kernel device tree overlay files
*  **phytec-\*.tar.gz**: Root file system,
   of bitbake-image that was built.

   * **phytec-qt6demo-image-phyboard-*-imx9*-*.tar.gz**: when bitbake-build
     was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-phyboard-*-imx9*-*.tar.gz**: when bitbake-build
     was processed for ``phytec-headless-image``
*  **phytec-\*.rootfs.wic.xz**: Compressed bootable SD
   card image of bitbake-image that was built. Includes bootloader, DTBs, Kernel
   and Root file system.

   * **phytec-qt6demo-image-phyboard-*-imx9*-*.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-qt6demo-image``
   * **phytec-headless-image-phyboard-*-imx9*-*.rootfs.wic.xz**: when
     bitbake-build was processed for ``phytec-headless-image``
*  **imx93-11x11-evk_m33_\*.bin**, binaries of demo applications for the
   Cortex-M33 MCU; can be manually loaded and started with U-Boot or Linux;
   are not part of builds for i.MX 91;

.. +---------------------------------------------------------------------------+
.. INSTALLING THE OS
.. +---------------------------------------------------------------------------+

Installing the OS
=================

Bootmode Switch (S3)
--------------------

.. tip::

   Hardware revision baseboard:

   *  |sbc-segin|: 1472.5
   *  |sbc-nash|: 1616.0, 1616.1, 1616.2

The |sbc| features a boot switch with four individually switchable ports to
select the |som| default bootsource.

.. _imx93-head-bootswitch:
.. include:: bootmode-switch.rsti

.. include:: ../installing-os.rsti

.. +---------------------------------------------------------------------------+
.. DEVELOPMENT
.. +---------------------------------------------------------------------------+

.. _imx93-head-development:

Development
===========

.. include:: /bsp/imx-common/development/standalone_build_preface.rsti
.. include:: /bsp/imx-common/development/standalone_build_u-boot_imxmkimage.rsti
.. include:: /bsp/imx-common/development/standalone_build_kernel_fit.rsti
.. include:: /bsp/imx-common/development/uuu.rsti
   :end-before: .. uuu-flash-spinor-marker

.. include:: /bsp/development/host_network_setup.rsti
.. include:: /bsp/imx-common/development/netboot_fit.rsti

.. include:: /bsp/imx-common/development/development_manifests.rsti

.. include:: /bsp/imx-common/development/format_sd-card.rsti

.. include:: /bsp/development/ampliphy-boot.rsti
   :end-before: .. ampliphy-boot-supported-bootscripts-marker

.. code-block::

   mmc_boot_fit
   net_boot_fit

.. include:: /bsp/development/ampliphy-boot.rsti
   :start-after: .. ampliphy-boot-supported-bootscripts-marker

For the |kit|, the default values are defined in the U-Boot devicetree
(e.g. arch/arm/dts/|dt-carrierboard|-u-boot.dtsi):

.. code-block::

   bootstd {
           bootph-verify;
           compatible = "u-boot,boot-std";

           filename-prefixes = "/", "/boot/";
           bootdev-order = "mmc0", "mmc1", "ethernet";

           script {
                   compatible = "u-boot,script";
           };
   };

The filename-prefixes property describes the paths that will be searched for
the bootscripts. In this case this is the root of the partition as well as the
boot folder. The bootdev-order property sets the default value for the
boot_targets variable. The supported bootmeths will also be named. In this case
only the script method is supported.

.. include:: /bsp/development/fitImages.rsti

.. +---------------------------------------------------------------------------+
.. DEVICE TREE
.. +---------------------------------------------------------------------------+

.. _imx93-head-device-tree:
.. include:: /bsp/device-tree.rsti

::

   imx93-phyboard-segin-peb-av-02.dtbo
   imx93-phyboard-segin-peb-av-18.dtbo
   imx93-phyboard-segin-peb-eval-01.dtbo
   imx93-phyboard-segin-peb-wlbt-05.dtbo
   imx93-phycore-npu.dtbo
   imx93-phycore-rpmsg.dtbo

Available overlays for phyboard-segin-imx91-1.conf are:

::

   imx91-phyboard-segin-peb-av-02.dtbo
   imx91-phyboard-segin-peb-av-18.dtbo
   imx91-phyboard-segin-peb-eval-01.dtbo
   imx91-phyboard-segin-peb-wlbt-05.dtbo

Available overlays for phyboard-nash-imx93-1.conf are:

::

   imx93-phyboard-nash-jtag.dtbo
   imx93-phyboard-nash-peb-av-10.dtbo
   imx93-phyboard-nash-peb-av-10-etml1010g3dra.dtbo
   imx93-phyboard-nash-peb-av-10-ph128800t006.dtbo
   imx93-phyboard-nash-peb-wlbt-07.dtbo
   imx93-phyboard-nash-pwm-fan.dtbo
   imx93-phyboard-nash-vm016.dtbo
   imx93-phyboard-nash-vm020.dtbo
   imx93-phycore-npu.dtbo
   imx93-phycore-rpmsg.dtbo

.. _imx93-head-ubootexternalenv:
.. include:: /bsp/dt-overlays-ampliphy-boot.rsti

.. +---------------------------------------------------------------------------+
.. ACCESSING PERIPHERALS
.. +---------------------------------------------------------------------------+

.. include:: /bsp/peripherals/introduction.rsti

.. include:: /bsp/imx-common/peripherals/pin-muxing.rsti

The following is an example of the pin muxing of the UART1 device in
|dt-carrierboard|.dts:

.. code-block::

   pinctrl_uart1: uart1grp {
           fsl,pins = <
                   MX93_PAD_UART1_RXD__LPUART1_RX     0x31e
                   MX93_PAD_UART1_TXD__LPUART1_TX     0x30e
           >;
   };

The first part of the string MX93_PAD_UART1_RXD__LPUART1_RX names the pad
(in this example UART1_RXD). The second part of the string (LPUART1_RX) is the
desired muxing option for this pad. The pad setting value (hex value on the
right) defines different modes of the pad, for example, if internal pull
resistors are activated or not. In this case, the internal pull up is
activated.

The device tree representation for UART1 pinmuxing:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L292`

.. _imx93-head-network:

Ethernet
--------

|sbc| provides two ethernet interfaces.

*  On |sbc-segin| we have:

   *  a 100 megabit Ethernet provided by |som|
   *  and 100 megabit Ethernet provided by phyBOARD.

*  On |sbc-nash| we have:

   *  a 100 megabit Ethernet provided by |som|
   *  and 1 gigabit Ethernet provided by phyBOARD.

.. include:: /bsp/peripherals/network.rsti

.. include:: wireless-network.rsti

.. include:: ../../peripherals/wireless-network.rsti

.. include:: /bsp/imx-common/peripherals/sd-card.rsti

DT configuration for the MMC (SD card slot) interface can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L214`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L215`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L213`

DT configuration for the eMMC interface can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L207`
* for |sbc-segin-93| or |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L214`

.. include:: /bsp/peripherals/emmc.rsti

.. include:: ../peripherals/gpios.rsti

.. include:: /bsp/peripherals/adc.rsti

On |sbc-nash| the ADC lines are accessible on X16 expansion connector:

========= ========
ADC input X16 pin
========= ========
ADC_IN0        47
ADC_IN2        49
========= ========

Additionally, there is a current sensing circuitry available on |sbc-nash|. It is
capable of measuring input current consumption of the |som| SoM @ 3.3V. The circuitry
consists of a MAX4372 current-sensing amplifier (50 V/V) with two 70 mOhm shunts
resistors in parallel configuration (effective R = 35 mOhm) connected to the ADC input
channel ADC_IN1 (Vref = 1.8V) via voltage divider with ratio of 1/2. This results
in a current scaling factor of 0.502232142 mA/LSB.

Current scaling factor is available as a sysfs parameter
``/sys/bus/iio/devices/iio:device1/in_current0_scale``.

The |som| SoM consumption can thus be measured with this simple script:

.. code-block:: bash

   #!/bin/sh
   RAW=$(cat /sys/bus/iio/devices/iio:device1/in_current0_raw)
   SCALE=$(cat /sys/bus/iio/devices/iio:device1/in_current0_scale)
   CURRENT=$(echo "$RAW * $SCALE" | bc -l)
   printf "Current: %.3f mA\n" "$CURRENT"

.. note::
   Current scaling factor calculation depends on ``CONFIG_IIO_RESCALE=y`` kernel configuration.

In our BSP we also enable config option ``CONFIG_SENSORS_IIO_HWMON=y`` which provides
hwmon interface to conveniently measure |som| SoM consumption directly via the sysfs
parameter:

.. code-block:: bash

   root@phyboard-nash-imx93-1:~# cat /sys/class/hwmon/hwmon1/curr1_input
   415

In the example output provided above, the current consumption measured was 415 mA @ 3.3V.

.. include:: ../peripherals/leds.rsti

Device tree configuration for the User I/O configuration can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin-peb-eval-01.dtso#L28`
or :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin-peb-eval-01.dtso#L28`

.. include:: /bsp/imx-common/peripherals/i2c-bus.rsti

General I²C3 bus configuration (e.g. |dt-som|.dtsi):
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L111`
or :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L104`

General I²C2 bus configuration for |dt-carrierboard|.dts:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L143`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L144`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L128`

EEPROM
------

There are two different I2C EEPROM flashes populated on |som| SoM and on the
|sbc|. For now only the one on the |som| is enabled, and it is used for board
detection.

.. include:: ../peripherals/eeprom.rsti

DT representation, e.g. in |som| file can be found in our PHYTEC git:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phycore-som.dtsi#L172`
or :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phycore-som.dtsi#L170`

.. include:: ../../peripherals/rtc.rsti

DT representation for I²C RTCs:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L164`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L165`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L138`

USB Host Controller
-------------------

The USB controller of the |soc| SoC provides a low-cost connectivity solution
for numerous consumer portable devices by providing a mechanism for data
transfer between USB devices with a line/bus speed of up to 480 Mbps (HighSpeed
'HS'). The USB subsystem has two independent USB controller cores. Both cores
are capable of acting as a USB peripheral device or a USB host, but on the |sbc|
one of them is used as a host-only port (USB-A connector).

.. include:: /bsp/peripherals/usb-host.rsti

The OTG port provides an additional pin for over-current protection, which is
not used on the |sbc|. Since it's not used, the driver part is also disabled
from within the device tree. In case this pin is used, activate this
over-current in the device tree and set the correct polarity (active high/low)
according to the device specification. For the correct setup, please refer to
the Kernel documentation under
Linux/Documentation/devicetree/bindings/usb/ci-hdrc-usb2.txt.

DT representation for USB Host:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L193`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L194`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L192`

.. include:: /bsp/peripherals/usb-otg.rsti

RS232/RS485
-----------

The |sbc-nash| i.MX 93 SoC provides one RS232/RS485 serial port.

.. warning::
   RS232 with HW flow control and RS485 are not working due to HW bug on the
   |sbc-nash| PCB revision 1616.0

.. include:: /bsp/peripherals/rs232.rsti
.. include:: /bsp/peripherals/rs485.rsti

The device tree representation for RS232 and RS485:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L185`

CAN FD
------

The |sbc| has one flexCAN interface supporting CAN FD. They are supported by the
Linux standard CAN framework which builds upon the Linux network layer. Using
this framework, the CAN interfaces behave like an ordinary Linux network device,
with some additional features special to CAN. More information can be found in
the Linux Kernel
documentation: https://www.kernel.org/doc/html/latest/networking/can.html

.. include:: /bsp/peripherals/canfd.rsti

Device Tree CAN configuration of |dt-carrierboard|.dts:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L135`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L136`
* for |sbc-nash|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L120`

Audio on |sbc-segin|
--------------------

On |sbc-segin| the TI TLV320AIC3007 audio codec is used. It uses I2S
for data transmission and I2C for codec control. The audio signals available
are:

* Stereo LINE IN,
* Stereo LINE OUT,
* Output where D-Class 1W speaker can be connected

.. include:: /bsp/peripherals/audio.rsti
   :end-before: .. audio_alsa_configuration_start_label

.. include:: /bsp/peripherals/audio.rsti
   :start-after: .. audio_playback_start_label
   :end-before: .. audio_capture_start_label

If Speaker volume it too low you can increase its volume with (values 0-3):

.. code-block:: console

   target:~$ amixer -c 0 sset Class-D 3

.. hint::

   Speaker output is only mono so when stereo track is played only left channel
   will be played by speaker.

Capture
.......

``arecord`` is a command-line tool for capturing audio streams which use Line In
as the default input source.

.. code-block:: console

   target:~$ arecord -t wav -c 2 -r 44100 -f S16_LE test.wav

.. hint::

   Since playback and capture share hardware interfaces, it is not possible to
   use different sampling rates and formats for simultaneous playback and
   capture operations.

Device Tree Audio configuration:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin.dts#L79`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin.dts#L80`

Audio on |sbc-nash|
-------------------

.. warning::

   Due to HW bug Audio is broken on |sbc-nash| PCB revision: 1616.0

To use audio with |sbc-nash| an additional adapter for the Audio/Video
connector is needed. The PEB-AV-10 (1531.1 revision) can be bought separately to
the Kit. PEB-AV-10 is populated with a TI TLV320AIC3007 audio codec. Audio
support is done via the I2S interface and controlled via I2C.

There is a 3.5mm headset jack with OMTP standard and an 8-pin header to connect
audio devices with the AV-Connector.  The 8-pin header contains a mono speaker,
headphones, and line-in signals.

.. include:: /bsp/peripherals/audio.rsti

Device Tree Audio configuration:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash-peb-av-10.dtsi#L60`

.. include:: /bsp/peripherals/video.rsti

.. include:: display.rsti

.. include:: /bsp/qt6.rsti

.. include:: /bsp/imx-common/peripherals/display.rsti

The device tree of PEB-AV-02/PEB-AV-18 can be found here:

* for |sbc-segin-91|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin-peb-av-02.dtso`
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx91-phyboard-segin-peb-av-18.dtso`
* for |sbc-segin-93|:
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin-peb-av-02.dtso`
  :linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-segin-peb-av-18.dtso`

The device tree of PEB-AV-10 for |sbc-nash| can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash-peb-av-10.dtso`

.. include:: peripherals/pm.rsti

.. include:: ../peripherals/tm.rsti

.. include:: /bsp/peripherals/watchdog.rsti

.. include:: /bsp/imx-common/peripherals/power-key.rsti

.. include:: ../peripherals/pxp.rsti

.. include:: ../peripherals/ocotp-ctrl.rsti

.. include:: /bsp/peripherals/tpm.rsti

Device tree TPM configuration can be found here:
:linux-phytec-imx:`blob/v6.12.34-2.1.0-phy9/arch/arm64/boot/dts/freescale/imx93-phyboard-nash.dts#L166`

.. include:: /bsp/peripherals/jtag.rsti
   :end-before: .. jtag-preparation-marker

Enabling JTAG Debug Interface on phyBOARD Nash
..............................................

The |soc| has a JTAG debug interface which can be used to debug software running
on the SoC. The JTAG interface is routed through the pinmux and is not enabled
by default. To enable the JTAG interface, please add this overlay configuration
to your ``overlays.txt`` file:

.. code-block::

   #conf-imx93-phyboard-nash-jtag.dtbo

.. note::
   JTAG and the MIPI CSI interface cannot be used at the same time, since they
   share the same pins. Jumper ``JP15`` switches signals between JTAG and
   MIPI CSI. It needs to be set to use JTAG.

.. include:: /bsp/peripherals/jtag.rsti
   :start-after: .. jtag-preparation-marker

.. +---------------------------------------------------------------------------+
.. i.MX 93 M33 Core
.. +---------------------------------------------------------------------------+

.. include:: ../mcu.rsti

.. +---------------------------------------------------------------------------+
.. i.MX 93 NPU
.. +---------------------------------------------------------------------------+

.. include:: /bsp/imx9/imx91-93/peripherals/npu.rsti
