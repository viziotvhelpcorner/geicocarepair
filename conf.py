# -- Project information -----------------------------------------------------

project = 'Geico Car Repair Guide'
author = 'Admin'
release = '1.0'
version = '1.0.0'

# -- General configuration ----------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output --------------------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- SEO & Metadata -----------------------------------------------------------

html_title = "Geico Car Repair – Complete Claims & Repair Guide"
html_short_title = "Geico Car Repair Guide"

html_theme_options = {
    'description': 'Step-by-step guide for geico car repair claims, process, coverage details, and repair tips.',
    'fixed_sidebar': True,
    'show_powered_by': False,
}

# -- Custom Meta Tags ---------------------------------------------------------

def setup(app):
    app.add_config_value('recommonmark_config', {}, True)
    app.add_css_file('custom.css')

# -- Language -----------------------------------------------------------------

language = 'en'

# -- Master document ----------------------------------------------------------

master_doc = 'index'
