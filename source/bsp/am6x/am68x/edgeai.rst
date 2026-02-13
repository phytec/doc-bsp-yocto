.. |sdk-edge-ai| replace:: SDK Linux Edge AI for AM68A Documentation by TI
.. _sdk-edge-ai: https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am68a/09_02_00/exports/edgeai-docs/common/sdk_overview.html
.. |sdk-edge-ai-link| replace:: |sdk-edge-ai|_

.. |link-bsp-images| replace:: https://download.phytec.de/Software/Linux/BSP-Yocto-EdgeAI/BSP-Yocto-EdgeAI-AM68x-v0.1/
.. |am68x-pd-getting-started| replace:: :ref:`phyCORE-AM68x/TDA4x documentation <am68x-pd24.1.0-getting-started>`

Introduction
============

Welcome to the quickstart guide for the BSP-Yocto-EdgeAI-AM68x-v0.1.

This release is designed to bring the TI EdgeAI SDK onto the phyBOARD-Izar
development kit for the phyCORE-AM68x/TDA4x platform.

Setting up the EdgeAI BSP on the phyBOARD-Izar
----------------------------------------------

If you have a kit, you need the phyboard-izar-am68x-2 machine which represents
the GP silicon, whereas phyboard-izar-am68x-3 is for HS-FS silicon-based SoCs.

The prebuilt images for the phyBOARD-Izar can be downloaded from: |link-bsp-images|

Consult the |am68x-pd-getting-started| for instructions on how to flash
the image onto the SD card, set boot switches and edit the bootenv.txt if needed.

Running the Demos
-----------------

In addition to the demos included in the SDK Linux Edge AI from TI, there are
a few Gstreamer pipelines located in the rootfs using the VM-016 phyCAM-M CSI
Camera as a source.

Running the PHYTEC example pipelines
....................................

The example Gstreamer pipelines will capture using the VM016 CSI camera and
show the output on the connected LVDS display:

- run_vm016_csi0.sh
- run_vm016_isp_csi0.sh
- run_vm016_isp_csi0_keypoint_det.sh
- run_vm016_isp_csi0_object_det.sh

For example, to start one of the example pipelines, type

.. code-block:: console

      root@phyboard-izar-am68x-2:~# ./phytec_edgeai_examples/run_vm016_isp_csi0_object_det.sh

The following pipeline is supposed to be run on a Linux host PC to display an incoming
RTP stream using eth0 (so copy it there):

- receive_rtp_stream.sh

In order to switch out the default kmssink using the connected LVDS display to
a udpsink streaming the output to a connected host PC at the very end of
the Gstreamer pipeline, LOCAL_SINK needs to be replaced with REMOTE_SINK.

Running the TI GStreamer Examples
.................................

Before running one of the demos from the SDK Linux Edge AI, the SoC environment
variable has to be set:

.. code-block:: console

      root@phyboard-izar-am68x-2:~# cd /opt/edgeai-gst-apps/
      root@phyboard-izar-am68x-2:edgeai-gst-apps# . scripts/detect_soc.sh

In case the LVDS display with its 1280x800 resolution is used, the output in
the corresponding yaml configuration (here configs/face_detection.yaml) needs
to be adjusted accordingly:

.. code-block:: console

      outputs:
         output0:
            sink: kmssink
            width: 1280
            height: 800
            overlay-perf-type: graph

         [...]

      flows:
         flow0: [input1,model0,output0,[0,0,1280,720]]

Or if the output shall be a network stream to the host machine similar to what
the REMOTE_SINK option in our default is:

.. code-block:: console

         output3:
            sink: remote
            width: 1920
            height: 1080
            port: 8081
            host: 192.168.3.10
            encoding: h264
            overlay-perf-type: graph

         [...]

      flows:
         flow0: [input1,model0,output3,[320,150,1280,720]]

Then, the application can be started:

.. code-block:: console

      root@phyboard-izar-am68x-2:edgeai-gst-apps# ./apps_cpp/app_edgeai configs/face_detection.yaml
      /* or by using the Python version */
      root@phyboard-izar-am68x-2:edgeai-gst-apps# ./apps_python/app_edgeai.py configs/face_detection.yaml
      /* or by using Optiflow */
      root@phyboard-izar-am68x-2:edgeai-gst-apps# ./sources/optiflow/optiflow.py configs/face_detection.yaml

Further information can be obtained from the |am68x-pd-getting-started| and
|sdk-edge-ai-link|.
