PHYTEC Yocto BSP Documentation
==============================

.. inclusion-marker-do-not-remove

How-to use this documentation
#############################

This documentation includes a quick start guide for our BSPs together with a complete
development documentation of our products.

The documentation is bundle with your release. To read it, you have three
options:

1. github pages
2. render locally with your BSP
3. Standalone installation

Standalone Installation
#######################

- The packets virtualenv and tox must be installed on your distribution::

        apt install virtualenv tox

- Clone the repository locally::

        git clone git@github.com:phytec/doc-bsp-yocto.git
        cd doc-bsp-yocto

- Create a virtualenv::

        virtualenv -p python3 venv
        . venv/bin/activate

- Install all dependencies::

        pip install -r requirements.txt

You can leave the virtualenv by running ``deactivate`` in the bash. Do not
forget to source the virtualenv again next time you want to use it.


Support questions
*****************

Don't hesitate to contact support@phytec.de


Discussion and Submitting patches
*********************************

- You can push a branch and open a pull-request for a change.
- Add a signed-off-by to your commits. Use ``git commit -s ...`` when commiting
  changes.

Start coding
------------

-   Create a branch to identify the issue you would like to work on. We're only
    working on main with tags. Therefore, branch off of the "main" branch::

        git checkout -b WIP/your-github-name/your-branch-name origin/main

- Using your favorite editor, make your changes, `committing as you go`_.
- Push your commits to GitHub and `create a pull request`_ by using::

        git push --set-upstream origin WIP/your-github-name/your-branch-name

.. _committing as you go: https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
.. _create a pull request: https://help.github.com/en/articles/creating-a-pull-request

Build the Documentation
#######################

Build the documentation and generate a PDF document.

.. code-block:: text

   make latexpdf

- On Ubuntu 20.04 you need to install some latex packages, e.g.::

        apt install texlive texlive-latex-extra latexmk

Build the documentation and generate html format.

.. code-block:: text

   make html

- On Ubuntu 20.04 you might need to expand the PATH in the enviroment::

        PATH=$PATH:~/.local/bin

Open ``docs/build/html/index.html`` in your browser to view the docs.

.. code-block:: text

   firefox build/html/index.html

Read more about `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

Build with tox
**************

Build the documentation as html and pdf::

    tox -e py3-doc
