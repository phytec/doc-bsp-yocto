Changelog:
==========
Naming scheme changed from Libra phyCORE to Libra phyFLEX
-Devicetree files like imx95-phyflex-libra-rdk.dtb
-Yocto machine (imx95-phyflex-libra-rdk-2)
-Kconfig names.

New Libra hardware revision to 1618.2, SoM 1620.3

Changes to U-Boot environment variables (ampliphy boot):
changed overlay priority so that overlays.txt no longer unconditionally overrides the
U-Boot environment variable, instead applying only when the variable
is unset to allow easier recovery from misconfigurations. Add overlaysenv
support to net_boot_fit bootscript, Simplify overlaysenv support for other
mmc bootscripts.

Changed from Ax SoC revision support to B0 SoC revision support

New Features:
-------------
- Camera support
  * VM-024 phyCAM-M
- Chromium support (chromium image)
- Introduction of ampliphy-boot
- RS232/485 support
- PWM fan support
- TPM support
- USB-C device and host mode support
- VPU support
- U-Boot USB Host support

Known Issues and Limitations:
-----------------------------
- GPU performance may be very low; As of release date, NXP is investigating
  this issue as it is present on their EVK as well. Our BSP documentation explains a workaround that
  yields better performance.
- Sporadic artifacts when capturing camera images with yavta
- Video provided with the qt6demo is decoded with CPU (due to incompatible coding with VPU) and thus
  may not play smoothly.
- network boot only works with connection on ETH1 by default. Changes to the U-Boot environment are
  necessary to boot via nfs on ETH2
