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

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "docs.adbc-drivers.org"
copyright = "2025, ADBC Drivers Contributors"
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

html_static_path = ["_static"]
html_theme = "sphinx_immaterial"
html_title = "ADBC Driver Foundry Driver Documentation"
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
