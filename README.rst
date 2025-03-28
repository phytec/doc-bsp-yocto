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

   apt install latexmk texlive-xetex texlive-latex-extra texlive-lang-chinese

Building the Documentation
--------------------------

There are 3 build targets available:

- ``tox -e html``: Build the documentation as HTML for the default language
  (en). This build command builds the documentation in multi-core mode and is
  the fastest. Building the documentation in other languages does not support
  parallel processing and is significantly slower.

  In addition the html build uses sphinx-autobuild to automatically rebuild the
  documentation when a source file changes. The documentation is afterwards
  hosted on a free port on your local machine. Exit with CTRL+C.

- ``tox -e intl``: Update the internationalization index files and build the
  documentation as HTML for all languages.

- ``tox -e pdf``: Build the documentation as a PDF file for all languages.

Open the locally built HTML pages in your webbrowser in the default language::

   xdg-open build/html/index.html

Or for a translated language::

   xdg-open build/html/zh_CN/index.html

PDF files are available at::

   build/latex/<lang>/doc-bsp-yocto.pdf
