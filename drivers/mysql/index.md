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
{}
---

# MySQL

:::{toctree}
:maxdepth: 1

v0.1.0.md
:::

Driver Version {bdg-ref-primary}`v0.1.0 <driver-mysql-v0.1.0>` ({ref}`permalink to this version <driver-mysql-v0.1.0>`)
<br/>Tested With MySQL: {bdg-secondary}`9.4`

This driver provides access to [MySQL][mysql]{target="_blank"}, a free and
open-source relational database management system.

## Installation & Quickstart

The driver can be installed with `dbc`.

To use the driver, provide the MySQL DSN as the `url` option.

## Feature & Type Support

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 50%;">
  </colgroup>
  <thead>
    <tr>
      <th>Feature</th>
      <th colspan="2">Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">Bulk Ingestion</td>
      <td>Create</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Append</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Temporary Table</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target catalog</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target schema</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="4">Catalog (GetObjects)</td>
      <td>depth=catalogs</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Get Parameter Schema</td>
      <td colspan="2">❌</td>
    </tr>
    <tr>
      <td>Get Table Schema</td>
      <td colspan="2">✅</td>
    </tr>
    <tr>
      <td>Prepared Statements</td>
      <td colspan="2">✅</td>
    </tr>
    <tr>
      <td>Transactions</td>
      <td colspan="2">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### SELECT (SQL to Arrow) type mapping

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - SQL Type
  - Arrow Type
* - BIGINT
  - int64
* - BOOLEAN
  - int64, int8 ⚠️ [^1]
* - DATE
  - date32[day]
* - DATETIME
  - timestamp[us]
* - DOUBLE PRECISION
  - double
* - INT
  - int32
* - NUMERIC
  - decimal64(10, 2)
* - REAL
  - ❌
* - SMALLINT
  - int16
* - TIME
  - time64[us]
* - TIMESTAMP
  - timestamp[us]
* - VARBINARY
  - binary
* - VARCHAR
  - string
:::

#### Bind parameter (Arrow to SQL) type mapping

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - Arrow Type
  - SQL Type
* - binary
  - VARBINARY
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - decimal128
  - DECIMAL
* - double
  - DOUBLE PRECISION
* - float
  - ❌
* - int16
  - SMALLINT
* - int32
  - INT
* - int64
  - BIGINT
* - string
  - VARCHAR
* - time64[us]
  - TIME
* - timestamp[us, tz=UTC]
  - TIMESTAMP
* - timestamp[us]
  - DATETIME
:::

#### Bulk ingest (Arrow to SQL) type mapping

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - Arrow Type
  - SQL Type
* - binary
  - VARBINARY
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - decimal128
  - NUMERIC
* - double
  - DOUBLE PRECISION
* - int16
  - SMALLINT
* - int32
  - INT
* - int64
  - BIGINT
* - string
  - VARCHAR
* - time64[us]
  - TIME
* - timestamp[us, tz=UTC]
  - TIMESTAMP
* - timestamp[us]
  - DATETIME
:::

[^1]: Return type is inconsistent depending on how the query was written

[mysql]: https://www.mysql.com/
