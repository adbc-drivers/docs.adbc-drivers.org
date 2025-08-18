---
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
hide-navigation: true
hide-toc: true
---
:::::{div} .landing-box
:style: "color: #FFF; background: var(--columnar); margin-bottom: 2.5em; padding: 1em; box-shadow: 0 0 .2rem rgba(0,0,0,.1),0 .2rem .4rem rgba(0,0,0,.2);"

::::{grid}
:margin: 0
:padding: 0

:::{grid-item}
:columns: 12 12 12 12
:class: sd-fs-1 rainbow
Fast universal data connectivity.
:::

:::{grid-item}
:columns: 12 12 12 12
:class: sd-fs-4
Powered by Apache Arrow.
:::
::::
:::::

## ADBC Drivers

:::::{grid} 1 2 3 3
:margin: 4 4 0 0

::::{grid-item-card}
**Google BigQuery**
^^^
Work with [Google BigQuery](https://cloud.google.com/bigquery), a data
warehouse offered by Google Cloud.
+++
:::{button-ref} drivers/bigquery
Documentation
:::
::::

:::::

## ADBC Resources

:::::{grid} 1 2 3 3
:margin: 4 4 0 0

::::{grid-item-card}
**Apache Arrow ADBC**
^^^
Official documentation for the ADBC specification and project.
+++
:::{button-link} https://arrow.apache.org/adbc/current/index.html
Documentation {octicon}`link-external`
:::
::::

::::{grid-item-card}
**dbc**
^^^
Install and manage drivers easily with a CLI from Columnar.
+++
:::{button-link} https://columar.tech
Download {octicon}`link-external`
:::
::::

:::::

:::{toctree}
:maxdepth: 2
:hidden:

drivers/index.md
:::
