# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'school-brainhack'
copyright = '2022, Brainhack school team'
author = 'Brainhack school team'
release = '2023-alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'sphinx.ext.autosectionlabel',
              'myst_parser'
             ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# tab name
html_short_title = 'BHSchool'

myst_enable_extensions = [
    "colon_fence"
]

# The logo
html_logo = 'img/logo_brainhack.png'

# icon
html_favicon = 'img/favicon.ico'
