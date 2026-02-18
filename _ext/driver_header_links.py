# Copyright (c) 2026 ADBC Drivers Contributors
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

"""Sphinx extension to automatically inject header links at the top of all driver pages.

Configuration:
    driver_header_links_config (dict): Mapping of driver names to lists of link dicts.
        Each link should have a 'url' key and optional 'label' key.
        GitHub URLs are automatically detected and display a GitHub icon with an
        accessible label. Non-GitHub URLs display the label text (defaults to "Link").

Example:
    driver_header_links_config = {
        'mysql': [
            {'url': 'https://github.com/apache/arrow-adbc', 'label': 'GitHub'},
            {'url': 'https://example.com/docs', 'label': 'Documentation'},
        ],
    }
"""

from docutils import nodes
from docutils.transforms import Transform
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform

GITHUB_ICON = """<svg width="24" height="24" viewBox="0 0 98 96" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="fill: currentColor;"><path d="M41.4395 69.3848C28.8066 67.8535 19.9062 58.7617 19.9062 46.9902C19.9062 42.2051 21.6289 37.0371 24.5 33.5918C23.2559 30.4336 23.4473 23.7344 24.8828 20.959C28.7109 20.4805 33.8789 22.4902 36.9414 25.2656C40.5781 24.1172 44.4062 23.543 49.0957 23.543C53.7852 23.543 57.6133 24.1172 61.0586 25.1699C64.0254 22.4902 69.2891 20.4805 73.1172 20.959C74.457 23.543 74.6484 30.2422 73.4043 33.4961C76.4668 37.1328 78.0937 42.0137 78.0937 46.9902C78.0937 58.7617 69.1934 67.6621 56.3691 69.2891C59.623 71.3945 61.8242 75.9883 61.8242 81.252L61.8242 91.2051C61.8242 94.0762 64.2168 95.7031 67.0879 94.5547C84.4102 87.9512 98 70.6289 98 49.1914C98 22.1074 75.9883 6.69539e-07 48.9043 4.309e-07C21.8203 1.92261e-07 -1.9479e-07 22.1074 -4.3343e-07 49.1914C-6.20631e-07 70.4375 13.4941 88.0469 31.6777 94.6504C34.2617 95.6074 36.75 93.8848 36.75 91.3008L36.75 83.6445C35.4102 84.2188 33.6875 84.6016 32.1562 84.6016C25.8398 84.6016 22.1074 81.1563 19.4277 74.7441C18.375 72.1602 17.2266 70.6289 15.0254 70.3418C13.877 70.2461 13.4941 69.7676 13.4941 69.1934C13.4941 68.0449 15.4082 67.1836 17.3223 67.1836C20.0977 67.1836 22.4902 68.9063 24.9785 72.4473C26.8926 75.2227 28.9023 76.4668 31.2949 76.4668C33.6875 76.4668 35.2187 75.6055 37.4199 73.4043C39.0469 71.7773 40.291 70.3418 41.4395 69.3848Z" fill="currentColor"/></svg>"""


class InjectDriverHeaderLinks(Transform):
    """
    Transform that injects navigation links after the first header in driver pages.

    This transform only runs on documents in the 'drivers' directory and inserts
    a set of header links after the first heading (h1) element.
    The links are configured via the driver_header_links_config setting in conf.py.
    """

    default_priority = 500  # Run after the document is parsed but before other transforms

    def apply(self):
        """Inject links after the first header in driver documentation pages."""
        document = self.document
        docname = self.document.settings.env.docname

        # Only apply to pages in the drivers directory (but not the drivers index)
        if not docname.startswith('drivers/') or docname == 'drivers/index':
            return

        # Extract driver name from docname (e.g., 'drivers/mysql/index' -> 'mysql')
        driver_name = self._extract_driver_name(docname)
        if not driver_name:
            return

        # Get links configuration for this driver
        config = self.document.settings.env.config.driver_header_links_config
        links_data = config.get(driver_name, [])

        if not links_data:
            return

        # Find the first section (which contains the h1 heading)
        for section in document.findall(nodes.section):
            # Inject links after the title but at the start of the section content
            self._inject_links(section, links_data)
            break  # Only process the first section

    def _extract_driver_name(self, docname):
        """Extract the driver name from a docname like 'drivers/mysql/index'."""
        parts = docname.split('/')
        if len(parts) >= 2:
            return parts[1]
        return None

    def _inject_links(self, section, links_data):
        """Create and inject the links next to the header."""
        links_html_parts = []

        for link_data in links_data:
            url = link_data.get('url', '')
            label = link_data.get('label', 'Link')

            # TODO: If we want support for more icons, maybe tweak how this
            # works a bit to pull from a map
            if url.startswith('https://github.com/'):
                links_html_parts.append(
                    f'<a class="reference external driver-github-link" href="{url}" target="_blank" aria-label="{label}">{GITHUB_ICON}</a>'
                )
            else:
                links_html_parts.append(
                    f'<a class="reference external" href="{url}" target="_blank">{label}</a>'
                )

        links_html = ''.join(links_html_parts)
        raw_node = nodes.raw(
            '',
            f'<div class="driver-header-links">{links_html}</div>',
            format='html'
        )

        # Insert right after the title (as a sibling, not a child)
        section.insert(1, raw_node)


def setup(app: Sphinx):
    """Register the extension with Sphinx."""
    # Register the configuration value for driver header links
    app.add_config_value('driver_header_links_config', {}, 'html')

    # Register the transform
    app.add_transform(InjectDriverHeaderLinks)

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
