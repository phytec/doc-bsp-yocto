PHYTEC Yocto BSP Documentation
==============================

We welcome contributions to this documentation! Before making any changes,
please read the `Contribution Guide
<https://github.com/phytec/doc-bsp-yocto/blob/main/CONTRIBUTING.rst>`_.

Getting the Source Code
-----------------------

Clone the Git repository::

   git clone git@github.com:phytec/doc-bsp-yocto.git

Change your current working directory to the just cloned source code::

   cd doc-bsp-yocto/

This documentation depends on Python `tox <https://tox.wiki/en/latest/>`_ for
building. It is recommended to install it in a virtualenv with pip. All required
dependencies are specified in ``requirements/``::

   python3 -m venv env
   source env/bin/activate
   pip3 install -r requirements/setup.txt

Make also sure that your system has following tools installed
(example for debian based systems)::

   apt install latexmk texlive-xetex

Building the Documentation
--------------------------

Build the documentation as HTML, which is the default build target::

   tox

To produce a LaTeX generated PDF documentation, specify the target explicitly::

   tox -e py3-pdf

Open the locally built HTML pages in your webbrowser::

   xdg-open build/html/index.html
