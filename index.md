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

# ADBC Driver Foundry Documentation

```{include} _static/adbc-drivers-logo.svg
```

Welcome to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} driver documentation site.

Below you will find documentation for the drivers available from the Foundry, resources for learning how to use them, and more about [ADBC](https://arrow.apache.org/adbc).

To learn more about the Foundry, head back to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} website.

## Foundry Drivers

Drivers available from the ADBC Driver Foundry:

:::::{grid} 1 2 3 3
:margin: 4 4 0 0
:gutter: 3

::::{grid-item-card}
**Amazon Redshift**
^^^
Work with Amazon Redshift, a data warehouse offered by AWS. Supports both Provisioned and Serverless offerings.
+++
:::{button-ref} drivers/redshift/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**BigQuery**
^^^
Work with BigQuery, a data warehouse offered by Google Cloud.
+++
:::{button-ref} drivers/bigquery/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Databricks**
^^^
Work with Databricks, a cloud data platform.
+++
:::{button-ref} drivers/databricks/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Microsoft SQL Server**
^^^
Work with Microsoft SQL Server, a relational database system offered by Microsoft.
+++
:::{button-ref} drivers/mssql/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**MySQL**
^^^
Work with MySQL, a free and open source relational database management system.
+++
:::{button-ref} drivers/mysql/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Snowflake**
^^^
Work with Snowflake, a cloud data warehouse.
+++
:::{button-ref} drivers/snowflake/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Trino**
^^^
Work with Trino, a distributed SQL query engine.
+++
:::{button-ref} drivers/trino/index
:click-parent:
Documentation
:::
::::

:::::

## Other Drivers

Drivers available across the ADBC-verse:

:::::{grid} 1 2 3 3
:margin: 4 4 0 0
:gutter: 3

::::{grid-item-card}
:class-header: sd-card-header-with-icon

**DuckDB**
:::{image} _static/DuckDB_icon-darkmode.svg
:width: 16px
:align: center
:::
^^^

DuckDB ADBC driver from DuckDB
+++
:::{button-link} https://duckdb.org/docs/stable/clients/adbc
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon

**Flight SQL**
:::{image} _static/feather.svg
:width: 16px
:align: center
:::
^^^

Arrow Flight SQL ADBC driver from the Apache Software Foundation
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/flight_sql.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon

**PostgreSQL**
:::{image} _static/feather.svg
:width: 16px
:align: center
:::
^^^

PostgreSQL ADBC driver from the Apache Software Foundation
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/postgresql.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon

**SQLite**
:::{image} _static/feather.svg
:width: 16px
:align: center
:::
^^^

SQLite ADBC driver from the Apache Software Foundation
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/sqlite.html
:click-parent:
Documentation
:::
::::

:::::

If you'd like to see your ADBC driver listed here, please shoot an email to [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).


## ADBC Resources

:::::{grid} 1 2 3 3
:margin: 4 4 0 0

::::{grid-item-card}
**Apache Arrow ADBC**
^^^
Official documentation for the ADBC specification and project.
+++
:::{button-link} https://arrow.apache.org/adbc/current/index.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**dbc**
^^^
Install and manage drivers easily with a CLI from Columnar.
+++
:::{button-link} https://docs.columnar.tech/dbc/
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**ADBC Quickstarts**
^^^
Simple examples showing how to use ADBC with various databases, query engines, and data platforms.
+++
:::{button-link} https://github.com/columnar-tech/adbc-quickstarts
:click-parent:
Repository
:::
::::

:::::

:::{toctree}
:maxdepth: 2
:hidden:

Home <self>
drivers/index.md
Back to ADBC Driver Foundry <https://adbc-drivers.org>
:::
