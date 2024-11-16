.. Download links
.. _`static-pdf-dl`: ../_static/coprocessor.pdf

.. only:: html

   Documentation in pdf format: `Download <static-pdf-dl_>`_

+------------------------+-------------------+
| coprocessor-ref-manual |                   |
+========================+===================+
| Document Title         |                   |
+------------------------+-------------------+
| Document Type          | Application Guide |
+------------------------+-------------------+
| Release Date           | XXXX/XX/XX        |
+------------------------+-------------------+
| Is Branch of           |                   |
+------------------------+-------------------+

This manual applies to all releases from kernel version x.

Introduction
============

Most modern SoCs include one of more coprocessors beside an application
processor. In most cases the application processor runs Linux, while the
coprocessor may run an RTOS. This manuals goes into detail how to utilize the
coprocessor efficiently for projects.

The manual explains generic principles and applies those principles in examples
for a specific platform and tools. It gives in introduction to OpenAMP, Zephyr
and Protocol Buffers (protobuf).

Overview of Technologies
========================

OpenAMP
-------

The `OpenAMP <http://openampproject.org>`_ Project which "seeks to standardize
the interactions between operating environments in a heterogeneous embedded
system through open source solutions for Asymmetric MultiProcessing (AMP)."
This introduction explains the main components and terms, the `OpenAMP
documentation <System Wide Considerations>`_ goes into further detail. OpenAMP
is avilable in Linux as well as in RTOS (e.g. Zephyr) and Vendor SDKs (e.g. NXP
MCUX, TI SDK, STM32Cube). The OpenAMP framework consists of several components:


Components
..........

Shared Memory
    In SoCs, where coprocessors are integrated on the same Die they typically
    communicate by exchanging data via sharing memory sections.

Interrupts
    Minimum set of one interrupt line per communicating core. This interrupt is
    often implemented in hardware blocks of the SoC, e.g. the "Messaging Unit
    (MU)" on the NXP i.MX8MP.

remoteproc
    Life Cycle Management (LCM) to manage and update the software running on
    coprocessors.

RPMsg
    Exchange of messages, api that enables Inter Processor Communications
    (IPC).

VirtIO, Virtqueue, Vring
   **VirtIO** provides a standardized framework for efficient message exchange
   between processing units using virtualization. **Virtqueue** is the abstract
   structure that manages the queues of messages and buffers for communication
   between these units. **Vring** is the specific circular buffer
   implementation used within a Virtqueue that organizes the descriptors for
   the messages being exchanged. There are ringbuffers for both directions
   (read, write). This set of infrastructure components can be used in
   combination with RPMsg to improve performance and reduce synchronization
   inbetween Cores.

RPC based on RPMsg
    TBD

RPMsg Messaging Protocol
........................

communication stack consisting of several protocol layers:

Transport Layer:
   RPMsg

MAC Layer:
   VirtIO, Virtqueue, Vring

Physical Layer:
   Shared Memory, Inter-core Interrupts e.g. via Messaging Unit (MU)


Libmetal
--------

Protocol Buffers
----------------

Zephyr
------

Mailbox
    Registers interrupt line from Messaging Unit.

Application Architectures
=========================

VirtIO
------

RPmsg + Protobuf
----------------

Use Cases
=========

Data Processing
---------------

Sensors and Real-Time
---------------------

Interface Virtualization
------------------------

Examples and Resources
======================

The Zephyr Inter-Processor Communication (IPC) Subsystem includes some `samples
<https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc.html>`_:

Resources
---------

* `NXP AN5317 - Loading code to Coprocessor <https://www.nxp.com/docs/en/application-note/AN5317.pdf>`_


OpenAMP using resource table
----------------------------

The `openamp_rsc_table
<https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp_rsc_table/README.html>`_
sample "demonstrates how to use OpenAMP with Zephyr based on a resource table.
It is designed to respond to [..]" the `rpmsg client
<https://elixir.bootlin.com/linux/latest/source/samples/rpmsg/rpmsg_client_sample.c>`_
and `rpmsg tty
<https://elixir.bootlin.com/linux/latest/source/drivers/tty/rpmsg_tty.c>`_
samples in the Linux Kernel. This sample demonstrates communication between
Zephyr (coprocessor) and Linux (application processor) using OpenAMP. It
creates the two RPMsg endpoints:

rpmsg-client-sample
   Demonstrates generic RPMsg message exchange between Zephyr and Linux.

rpmsg-tty
   A TTY service that virtualizes a serial connection at `/dev/rpmsg-tty` in
   Linux, facilitating data exchange with Zephyr over this virtualized
   interface.

Run the Sample
..............

1. Make sure the devicetree overlay ``imx8mp-phycore-rpmsg.dtbo`` is activated,
   the BSP manual for your platform explains how to activate this.

2. Restart the target and execute in U-Boot:

   .. code-block::

      u-boot=> run prepare_mcore

3. The target will now boot and you can build and flash the Zephyr application
   with:

   .. code-block:: console

      host:zephyrproject/zephyr$ west build -b phyboard_pollux/mimx8ml8/m7 samples/subsys/ipc/openamp_rsc_table/ -p
      host:zephyrproject/zephyr$ west flash

4. Zephyr should now boot with

   .. code-block:: console

      target_m7:~$ *** Booting Zephyr OS build v4.0.0-rc3-4-g65511eacf9d1 ***
                   I: Starting application threads!
                   I: OpenAMP[remote] Linux responder demo started
                   Waiting for remote to be ready

5. Load the kernel Module:

   .. code-block:: console

      target:~$ modprobe rpmsg_client_sample
      target:~$ dmesg | tail                         # Check module messages
      target:~$ modprobe -u rpmsg_client_sample      # Unload Kernel module


.. note::

   Running firmware via debug adapter or via remoteproc has an effect on
   inter-core communication.

   TODO: Verify if inter-core-communication also works via debug adapter.

.. warning::

   Remoteproc only reads firmware files from the ``/lib/firmware`` directory!
   If you try to load a binary from another location unexpected errors will
   occur!


Other Examples
--------------

The following examples exist in Zephyr, however, they are specific to SoCs that
have multiple instances of Zephyr running in the same SoC. They are partly
related to Zephyrs
`ipc_service <https://docs.zephyrproject.org/latest/services/ipc/ipc_service/ipc_service.html>`_ and not suitable for communication with Linux.

`OpenAMP Sample
<https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp/README.html#openamp>`_

   sample builds different images for two targets running Zephyr. Both targets
   setup virtqueue and virtio and communicate with each other via RPMsg. This
   sample is mainly used to evaluate SoCs with two Cortex M devices and can not
   be used with Linux.

`openamp-system-reference <https://github.com/OpenAMP/openamp-system-reference>`_

   Several samples for both platforms, Linux and Zephyr that demonstrate
   different aspects of OpenAMP.

`rpmsg_service Samples
<https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/rpmsg_service>`_

   Simplified version of the OpenAMP sample that does not use virtio and
   virqueues.


`Samples in ipc_service/ <https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc.html>`_

   Examples related to Zephyr ipc_service subsytem.

Current Problems
================

This section lists current problems that need work.

Shell not working in Zephyr for Linux SoCs
   There may be a problem with interrupts and nxp deactivated the shell for the
   imx8qm  boards. https://github.com/zephyrproject-rtos/zephyr/pull/79428


