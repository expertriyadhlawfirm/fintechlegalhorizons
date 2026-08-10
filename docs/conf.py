# Configuration file for raw HTML passthrough in Sphinx

project = 'My Landing Page'
copyright = '2026'
author = 'Author'

# No extensions needed
extensions = []

# Output setup
html_title = 'My Page'

# Read the Docs ke default theme ko disable karna
html_theme = 'basic'

# Aapki docs/ folder ki saari files (including index.html) ko build output mein copy karna
html_static_path = ['.']

# Default Sphinx layout templates ko override karna taake aapki index.html exact render ho
html_additional_pages = {
    'index': 'index.html'
}

# Unwanted Sphinx elements disable karna
html_show_sphinx = False
html_show_sourcelink = False
