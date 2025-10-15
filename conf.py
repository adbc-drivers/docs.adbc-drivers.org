# Copyright (c) 2025 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx.writers.html import HTMLTranslator

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "docs.adbc-drivers.org"
copyright = "2025 ADBC Drivers Contributors"
author = "ADBC Drivers Contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_immaterial",
    "sphinx.ext.intersphinx",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "venv",
    ".venv",
    ".pixi",
    ".git",
    "generated",
    "README.md",
]
suppress_warnings = ["myst.header"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = ["custom.css"]
html_logo = "_static/adbc-drivers-logo.png"
html_static_path = ["_static"]
html_theme = "sphinx_immaterial"
html_title = "ADBC Drivers Documentation"
html_theme_options = {
    "features": [
        "content.code.copy",
    ],
    "font": {
        "text": "IBM Plex Sans",
        "code": "IBM Plex Mono",
    },
    "palette": [
        {
            "media": "(prefers-color-scheme)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "default",
            "toggle": {
                "icon": "material/theme-light-dark",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "default",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "slate",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to system preference",
            },
        },
    ],
    "social": [],
    "toc_title": "Contents",
}

# -- Options for Intersphinx -------------------------------------------------

intersphinx_mapping = {
    "arrow": ("https://arrow.apache.org/docs/", None),
    "adbc": ("https://arrow.apache.org/adbc/current/", None),
    "python": ("https://docs.python.org/3", None),
}

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = ["attrs_block", "attrs_inline", "colon_fence", "linkify"]

# -- Options for OpenGraph ---------------------------------------------------

ogp_description_length = 400
ogp_site_url = "https://docs.adbc-drivers.org"
ogp_site_name = "ADBC Drivers Documentation"
ogp_social_cards = {
    "image": "_static/opengraph-logo.png",
    "line_color": "#434343",
}

# -- Customization -----------------------------------------------------------


class ExternalLinkHtmlTranslator(HTMLTranslator):
    _external_icon = """ <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-link-external" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg>"""

    def visit_reference(self, node):
        if node.get("newtab") or not (
            node.get("target") or node.get("internal") or "refuri" not in node
        ):
            node["target"] = "_blank"
        super().visit_reference(node)

    def depart_reference(self, node):
        if node.get("target") == "_blank":
            self.body.append(self._external_icon)
        super().depart_reference(node)


def setup(app):
    app.set_translator("html", ExternalLinkHtmlTranslator)
