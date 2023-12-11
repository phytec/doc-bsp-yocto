The purpose of this documentation is to highlight the workings and layout of the
documentation, special notes to keep in mind, and how to add content i.e. extend
this documentation project.

Getting Started
===============

Getting familiar with reStructuredText
--------------------------------------

The basis is reStructuredText for which documentation can be found `here
<https://docutils.sourceforge.io/docs/ref/rst/>`__. Concepts that are unique to
Sphinx, which are mostly extensions of the base reStructuredText language, can
be found `here
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__. For
more advanced stuff and/or project configuration have a look at `this
<https://www.sphinx-doc.org/en/master/usage/configuration.html>`__ page.

GitHub Contribution Guide
-------------------------

For anyone who notices an error, would like to suggest an improvement or add
new content to the manuals, GitHub Issues and pull requests are the way to do
it. We welcome any kind of feedback and contribution and would encourage anyone
to contribute to this documentation.

-  **pull requests**

   - To open a pull request, create a new git branch and give a short name that
     describes the purpose of the branch best. Once you have a branch, open a
     pull request and give it a name that you think describes what you want to
     do best. Please also write a description that explains in more detail what
     the changes do.

   .. code-block::
      :caption: Example

      In some sections of the Yocto Manual for kirkstone, links to external
      webpages are not working, they return 404 not found errors. I want to
      update the links to refer to the intended destinations.

   - This allows the maintainers to understand your intentions. Having the
     context in mind it is easier to evaluate the changes you introduced to the
     files. If you accidentally change something for a Yocto Manual for
     hardknott, a reviewer can then easily point out this mistake to you. When
     you are satisfied with the changes you made, or earlier if you want to get
     feedback, ask the maintainers for review.

   - Sometimes the maintainers will ask you to make some changes when they are
     not fully satisfied with your additions. This process is normal and is
     used to maintain high quality of the project. Of course you can argue
     about change requests from reviewers if you think their suggestions are
     not a good idea. After all they are also human.

   - Opening a pull request is the preferred solution for adding changes to the
     project. The section :ref:`Open a Pull Request <open-pull-request>`
     explains how to open a pull request in detail.

   .. note::

      We use GitHub Actions to validate some basic syntax conventions and
      styleguides. Make sure you fulfill the conditions, otherwise your changes
      will not be merged. See the :ref:`Conventions <contributing-conventions>`
      section for more information.

-  **Issues**

   - If you do not feel comfortable opening a pull request to add some changes
     yourself you can always create an Issue to point out the changes you would
     like to see introduced to the project. Be as precise as possible,
     maintainers will ask you to explain in more detail if they do not
     understand your description.

   - Issues are also a good place to ask questions on things you are not sure
     about. For example if you have a problem regarding the project and do not
     know a solution.


.. _contributing-conventions:

Conventions
-----------

Textwidth
.........

We use a textwidth of 80 characters. Exempt from this rule are long links and
literal blocks that display terminal output for example. If something like a
heading does not fit into 80 characters, then it is very likely difficult to
understand what the following section is about and you should think of a more
concise heading.

Indenting
.........

Use indent width is of 3 spaces. Tabs are not allowed.

Headings
........

reStructuredText allows for special characters to be used as an underline to
denote headings. See `reference manual
<https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections>`_.
For this project, headings are to be used in the following order::

   =====
   Title
   =====

   Section Title 1
   ===============

   Subsection Title 1.1
   --------------------

   Subsubsection Title 1.1.1
   .........................

   Subsubsubsection Title 1.1.1.1
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   For now the deepest nesting allowed is 4 levels.


Important Tasks When Extending the Documentation
------------------------------------------------

When creating a new documentation document e.g. for a new release, it is
important to add a tuple to the *latex_documents* variable in the *conf.py*
file. This ensures a separate pdf file is generated for the newly added release.

.. tip::
   Use `grep <https://www.man7.org/linux/man-pages/man1/grep.1.html>`__
   (`ripgrep <https://github.com/BurntSushi/ripgrep>`__) to search for the
   includes in other files.

Inserting Blanks
................

If there is a paragraph that is in the middle of some include file, but is only
used by a certain leaf file, it is possible to insert blank substitutions i.e.
skip the text for most manuals but insert the text for a specific manual.
This can be done with `.. |subname| replace:: \\`.

Example:
The i.MX 8M Plus has 2 ethernet interfaces while Mini and Nano only have one.
In the Network section, only for the Plus is some additional text inserted
specifying the second ethernet interface absent on the Mini and Nano.

Understanding the BSP Folder Structure
......................................

To get going quickly, it is important to get familiar with the folder structure
for the BSP documentation.

::

   /source
   |__ bsp
   |   |__ images
   |   |   \__ <images used by general module files>
   |   |__ imx8 (platform family directory)
   |   |   |__ images
   |   |   |   \__ <images used by platform family files>
   |   |   |__ imx8mm
   |   |   |   |__ mini.rst
   |   |   |   \__ <release>.rst
   |   |   |__ imx8mp
   |   |   |   |__ plus.rst
   |   |   |   \__ <release>.rst
   |   |   |__ <platform module files>
   |   |   |__ getting-started-imx8.rst
   |   |   \__ imx8.rst
   |   |__ getting-started.rst
   |   \__ <general module files>
   \_yocto
     |
   ....

The bsp folder is the top folder for all bsp related documentation. In this
folder are rst files containing content that spans multiple processor/soc
families. These rst files may contain images that they source from the
bsp/images folder (e.g. PHYTEC logo). The bsp folder also contains subfolders
for each platform/family. In the illustration above the imx8 family is used as
an example. Its files are located in the source/bsp/imx8/ folder. It also
contains generic content that although not applicable to other platform does
apply to multiple imx8 family SoCs. Finally, there is one directory in the
platform directory for each SoC used by PHYTEC. It contains one rst file for
each release. These so-called leaf files include all content that is needed to
put together one complete documentation for this release. These files may also
add content that is missing from all previously mentioned generic files. Also,
all variables (substitutions) are defined in those files.

Each platform directory as well as each SoC directory contains one file named
after the respective directories. These contain the toctree directives needed to
combine all individual documents so that they appear (can be navigated to) in
the final html documentation.

Quickstart for Creation of a New BSP Manual
...........................................

1. Read the previous subsections of the :ref:`Getting Started
   <contribute-getting-started>` section
2. Have a look at the template.rst file located in the source/bsp/ folder.
3. Create new (sub) directory structure in the source/bsp directory for the
   family of SoC and copy
   the template file to a fitting directory.
4. Add the newly created file/directory to the toctree via the .. toctree::
   directive

.. hint::

   Make sure to use a ==== headline in each file you added containing a toctree
   otherwise the final manual will not show up in the html toctree.

5. Fill out the substitutions in the template.
6. Add the tuple for the <release>.rst file in the conf.py file to
   latex_documents, so that a separate pdf file for your document will be built.
7. Add custom content needed for the final doc (use content from other platforms
   if applicable).

Use ``tox`` to make sure all pages get rebuilt and linked correctly.
Otherwise your newly added files in the toctree may not be displayed in the html
toc sidebar.


Design Decisions
================

Organization:

-  The "source" directory is structured so that more specific files in terms of
   documentation are locacted further down the file tree, with the <BSP>.rst
   files that include all other generic text representing the leaf nodes.
   Example:
   There is a "general info" guide regarding ESD conformity that is included in
   every BSP documentation document. To indicate this property, the file is
   located at source/bsp/
   Example:
   Some content is only applicable to the imx8 family of boards/socs. Thus, the
   file containing this content is located at /source/bsp/imx8

-  The leafs a.k.a. the "final" <BSP>.rst files include all content that is
   either located in other files or add content themselves. Additionally, they
   define all substitutions used in the final document.
   For more info on substitutions, see
   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions

-  As much content as reasonably possible is outsourced to include files. To
   this extent, some text might contain board names or other SOC/Board/SOM
   specific content. In the simple cases they can handled by textual
   replacement using the substitution functionality. When a longer passage of
   text is board specific, it needs to be removed from the "generic" file to a
   more specific file. E.g. move from bsp/ to bsp/imx8

-  For now the individual L-* documents are kept as a single continuous html
   page. This means that all content is included using the include reST
   directive and is not added by using the toctree sphinx reST directive.
   (Using toctree is more complex in terms of file structure and arguably adds
   the benefit to not have everything in one large html file, but separated
   into e.g. one per section)

-  Improve quality control for manuals. Due to the nature of contributing
   content on GitHub, at least 2 other people need to approve a pull request
   and thus approve the content being added to a manual.


Unresolved Issues
=================

*  Substitutions require the highest priority i.e. can't do **|<text>|** to
   highlight substitution text in bold for only one case.
   https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#recognition-order


.. _open-pull-request:

Open a Pull Request
===================

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
