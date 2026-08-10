import os

project = 'Fintech Legal Horizons'
copyright = '2026'
author = 'Admin'

# Basic configuration to avoid Sphinx default templates
extensions = []
html_theme = 'basic'

# Disable unnecessary Sphinx elements
html_show_sphinx = False
html_show_sourcelink = False

# Force Sphinx to copy index.html directly
html_extra_path = ['index.html']
