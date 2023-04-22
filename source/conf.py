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
import sys

# -- Project information -----------------------------------------------------

project = 'PHYTEC BSP Documentation'
copyright = '2023, PHYTEC Messtechnik GmbH'
author = 'PHYTEC'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '*/template.rst',
]

extlinks = {'imx-dt': ('https://git.phytec.de/linux-imx/tree/arch/arm64/boot/dts/freescale/%s',
                       None)}
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
    'fontpkg': '\\usepackage{lmodern}'
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
        'bsp/imx8/imx8mm/head',
        'imx8mm-head.tex',
        'L-1002e.Ax i.MX 8M Mini BSP Manual',
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
        'bsp/am57x/pd20.1.1',
        'am57x-pd20.1.1.tex',
        'L-xxxxx.Ax AM57x BSP Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
]

# -- Linkcheck options ----------------------------------------------------

linkcheck_ignore = [
    "https://github.com/phytec/doc-bsp-yocto"
]

linkcheck_timeout = 30
linkcheck_workers = 10
linkcheck_anchors = False
