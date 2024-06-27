# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re

# -- Project information -----------------------------------------------------

project = 'PHYTEC BSP Documentation'
copyright = '2024, PHYTEC Messtechnik GmbH'
author = 'PHYTEC'

# Use git describe to get the version e.g.: imx8-pd23.1.0-1-gb1830e
release = re.sub('', '', os.popen('git describe --tags').read().strip())

# Assign to the version variable, to list the version in the html as well.
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
    'sphinx_substitution_extensions',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '*/template.rst',
]

extlinks = {
    'imx-dt': ('https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/%s', None),
    'linux-phytec': ('https://github.com/phytec/linux-phytec/%s', None),
    'yocto-bootenv': ('https://git.phytec.de/meta-phytec/tree/recipes-bsp/bootenv?h=%s', None)
}

extlinks_detect_hardcoded_links = True

highlight_language = 'none'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'sphinx/static/logo-phytec.svg'
html_favicon = 'sphinx/static/favicon.ico'
html_title = 'PHYTEC BSP Documentation'
html_show_sphinx = False

html_theme_options = {
    'logo_only': False,
    'navigation_depth': 5,
}

html_context = {
    "display_github": True,
    "github_user": "phytec",
    "github_repo": "doc-bsp-yocto",
    "github_version": "main",
    "conf_py_path": "/source/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['sphinx/static']

html_css_files = [
    'css/code-block.css',
    'css/phytec-theme.css',
]

# -- Options for PDF output -------------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    'fontpkg':
    '\\usepackage{lmodern}',
    'preamble':
    '''
      \\usepackage{fontspec}
      \\setmonofont{DejaVu Sans Mono}[Scale=0.8]
    ''',
}

latex_documents = [
    (
        'bsp/imx8/imx8mp/head',
        'imx8mp-head.tex',
        'L-1017e.Ax i.MX 8M Plus BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/mainline-head',
        'imx8mp-mainline-head.tex',
        'i.MX 8M Plus BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd24.1.1',
        'imx8mp-pd24.1.1.tex',
        'i.MX 8M Plus BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd23.1.0',
        'imx8mp-pd23.1.0.tex',
        'i.MX 8M Plus BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd22.1.1',
        'imx8mp-pd22.1.1.tex',
        'i.MX 8M Plus BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/head',
        'imx8mm-head.tex',
        'L-1002e.Ax i.MX 8M Mini BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/pd23.1.0',
        'imx8mm-pd23.1.0.tex',
        'i.MX 8M Mini BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/pd22.1.1',
        'imx8mm-pd22.1.1.tex',
        'i.MX 8M Mini BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/head',
        'imx8mn-head.tex',
        'L-1002e.Ax i.MX 8M Mini BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/pd23.1.0',
        'imx8mn-pd23.1.0.tex',
        'i.MX 8M Nano BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/pd22.1.1',
        'imx8mn-pd22.1.1.tex',
        'i.MX 8M Nano BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.1.0',
        'imx93-pd24.1.0.tex',
        'i.MX 93 BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.1.1',
        'imx93-pd24.1.1.tex',
        'i.MX 93 BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'yocto/kirkstone',
        'kirkstone.tex',
        'Yocto Reference Manual Kirkstone',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'yocto/mickledore',
        'mickledore.tex',
        'Yocto Reference Manual Mickledore',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'yocto/scarthgap',
        'scarthgap.tex',
        'Yocto Reference Manual Scarthgap',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
]

# -- Linkcheck options ----------------------------------------------------

linkcheck_ignore = ["https://github.com/phytec/doc-bsp-yocto"]

linkcheck_timeout = 60
linkcheck_workers = 10
linkcheck_anchors = False
