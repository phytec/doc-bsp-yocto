.. image:: https://github.com/phytec/doc-bsp-yocto/workflows/Documentation/badge.svg
   :target: https://github.com/phytec/doc-bsp-yocto/actions/workflows/documentation.yaml

.. inclusion-marker-do-not-remove

PHYTEC Yocto BSP Documentation
==============================

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

Building the Documentation
--------------------------

Build the documentation as HTML, which is the default build target::

   tox

To produce a LaTeX generated PDF documentation, specify the target explicitly::

   tox -e py3-pdf

Open the locally built HTML pages in your webbrowser::

   xdg-open build/index.html

Contributing
------------

To propose changes, open a pull-request with your WIP branch. This WIP branch
should be pushed to this repository, without forking. It must be named after the
following scheme::

   WIP/your-github-account-name/feature-description

E.g. if your GitHub account is named ``john-smith`` and your pull-request
contains a new chapter about the SPI on the i.MX8M, then name the branch like
the following::

   WIP/john-smith/imx8m-spi-chapter

To create this branch, use ``checkout`` and specify the remote ``main`` branch
to be the base of your changes::

   git checkout -b WIP/your-github-account-name/feature-description origin/main

Push your changes regularly to the remote repository. When pushing the branch
for first time, you have to specify the upstream using ``-u``::

   git push -u origin WIP/your-github-account-name/feature-description

For subsequent commits you do not have to do this and simply use ``push`` while
being on your WIP branch::

   git push

When committing, make sure to add a sign-off using the option ``-s``::

   git commit -s
