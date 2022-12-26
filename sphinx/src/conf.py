# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'presto-sql'
copyright = '2022, Andreas Reichel'
author = 'Andreas Reichel'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'sphinx.ext.extlinks', 'sphinx-prompt', 'sphinx_substitution_extensions', 'sphinx_issues', 'sphinx_tabs.tabs', 'pygments.sphinxext', ]

templates_path = ['_templates']
exclude_patterns = []
source_encoding = 'utf-8-sig'
pygments_style = 'friendly'
show_sphinx = False
master_doc = 'index'
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

