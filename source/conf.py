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
copyright = '2025, PHYTEC Messtechnik GmbH'
author = 'PHYTEC'

# Use git describe to get the version e.g.: imx8-pd23.1.0-1-gb1830e
version = re.sub('', '', os.popen('git describe --tags').read().strip())

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
    'sphinx_substitution_extensions',
    'sphinx_sitemap',
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
    'linux-phytec-imx': ('https://github.com/phytec/linux-phytec-imx/%s', None),
    'yocto-bootenv': ('https://git.phytec.de/meta-phytec/tree/recipes-bsp/bootenv?h=%s', None)
}

extlinks_detect_hardcoded_links = True

highlight_language = 'none'

# -- Internationalization ----------------------------------------------------

# Set the default language
locale_dirs = ['locale/']
# Compact all strings into a single file, this avoids editing identical strings
# in multiple .po files.
gettext_compact = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'sphinx/static/logo-phytec.svg'
html_favicon = 'sphinx/static/favicon.ico'
html_title = 'PHYTEC BSP Documentation'
html_show_sphinx = False
html_baseurl = 'https://phytec.github.io/doc-bsp-yocto/'

# Add robots.txt so search engines can index the site
html_extra_path = ['sphinx/static/robots.txt',
                   'sphinx/static/googledd12f2e41658d61e.html']

# Link scheme
sitemap_url_scheme = "{link}"
# When adding a lang prefix, this would also affect the english version, which
# currently does not have a language prefix as it is the default. Therefore, we
# currently only support a sitemap without alternative links.
sitemap_locales = [None]

html_theme_options = {
    'logo_only': False,
    'navigation_depth': 5,
}

pages_root = "https://phytec.github.io/doc-bsp-yocto"
html_context = {
    "display_github": True,
    "github_user": "phytec",
    "github_repo": "doc-bsp-yocto",
    "github_version": "main",
    "conf_py_path": "/source/",
    # Language selector, works together with versions.html in templates
    'languages': [
        ['en', pages_root],
        ['zh_CN', pages_root + '/zh_CN']
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['sphinx/static']

# The templates directory is used to display a language selector in the sidebar.
templates_path = ['sphinx/templates']

html_css_files = [
    'css/code-block.css',
    'css/phytec-theme.css',
]

# -- Options for PDF output -------------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    'fontpkg':
    '\\usepackage{lmodern}',
    'preamble': r'''
      \usepackage{fontspec}
      \setmonofont{DejaVu Sans Mono}[Scale=0.8]
      \makeatletter
      % Redefine Header and Footer style
      \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[R]{{\py@HeaderFamily\thepage}}
        \fancyfoot[L]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyhead[L]{{\py@HeaderFamily \fontsize{9}{10.8}\selectfont \@title}}
        \fancyhead[R]{{\py@HeaderFamily \fontsize{9}{10.8}\selectfont Doc-rev.: \textit{''' + version + r'''}}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
      }
      % Redefine \chaptermark to exclude chapter number
      \renewcommand{\chaptermark}[1]{\markboth{#1}{}}
    \makeatother
    ''',
}

latex_documents = [
    (
        'bsp/imx8/imx8mp/head',
        'imx8mp-head.tex',
        'i.MX 8M Plus BSP Manual DRAFT',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/mainline-head',
        'imx8mp-mainline-head.tex',
        'i.MX 8M Plus BSP Manual DRAFT',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd24.1.0_nxp',
        'imx8mp-pd24.1.0_nxp.tex',
        'i.MX 8M Plus BSP Manual PD24.1.0 NXP',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd24.1.2',
        'imx8mp-pd24.1.2.tex',
        'i.MX 8M Plus BSP Manual PD24.1.2',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd24.1.1',
        'imx8mp-pd24.1.1.tex',
        'i.MX 8M Plus BSP Manual PD24.1.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd23.1.0',
        'imx8mp-pd23.1.0.tex',
        'i.MX 8M Plus BSP Manual PD23.1.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd22.1.2',
        'imx8mp-pd22.1.2.tex',
        'i.MX 8M Plus BSP Manual PD22.1.2',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp/pd22.1.1',
        'imx8mp-pd22.1.1.tex',
        'i.MX 8M Plus BSP Manual PD22.1.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mp-libra-fpsc/head',
        'imx8mp-libra-fpsc-head.tex',
        'Libra i.MX 8M Plus FPSC BSP Manual DRAFT',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/head',
        'imx8mm-head.tex',
        'i.MX 8M Mini BSP Manual DRAFT',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/pd25.1.0',
        'imx8mm-pd25.1.0.tex',
        'i.MX 8M Mini BSP Manual PD25.1.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/pd23.1.0',
        'imx8mm-pd23.1.0.tex',
        'i.MX 8M Mini BSP Manual PD23.1.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mm/pd22.1.1',
        'imx8mm-pd22.1.1.tex',
        'i.MX 8M Mini BSP Manual PD22.1.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/head',
        'imx8mn-head.tex',
        'i.MX 8M Mini BSP Manual DRAFT',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/pd23.1.0',
        'imx8mn-pd23.1.0.tex',
        'i.MX 8M Nano BSP Manual PD23.1.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx8/imx8mn/pd22.1.1',
        'imx8mn-pd22.1.1.tex',
        'i.MX 8M Nano BSP Manual PD22.1.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.1.0',
        'imx93-pd24.1.0.tex',
        'i.MX 93 BSP Manual PD24.1.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.1.1',
        'imx93-pd24.1.1.tex',
        'i.MX 93 BSP Manual PD24.1.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.2.0',
        'imx93-pd24.2.0.tex',
        'i.MX 93 BSP Manual PD24.2.0',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx93/pd24.2.1',
        'imx93-pd24.2.1.tex',
        'i.MX 93 BSP Manual PD24.2.1',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx95/quickstart',
        'imx95-quickstart.tex',
        'i.MX 95 Quickstart Guide',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'bsp/imx9/imx95/alpha1',
        'imx95-alpha1.tex',
        'i.MX 95 BSP Manual ALPHA1',
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
    (
        'rauc/kirkstone',
        'rauc-kirkstone.tex',
        'RAUC Update \\& Device Management Manual Kirkstone',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'rauc/mickledore',
        'rauc-mickledore.tex',
        'RAUC Update \\& Device Management Manual Mickledore',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'rauc/scarthgap',
        'rauc-scarthgap.tex',
        'RAUC Update \\& Device Management Manual Scarthgap',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
    (
        'coprocessor/coprocessor',
        'coprocessor.tex',
        'Coprocessor Application Manual',
        'PHYTEC Messtechnik GmbH',
        'manual',
        False,
    ),
]

# -- Linkcheck options ----------------------------------------------------

linkcheck_ignore = [
    "https://github.com/phytec/doc-bsp-yocto",
    "https://opencv.org/",
]

linkcheck_timeout = 60
linkcheck_workers = 10
linkcheck_anchors = False
