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

# Trino Driver

:::{toctree}
:maxdepth: 1
:hidden:

versions.md
:::

{badge-primary}`Driver Version|v0.1.0` {badge-success}`Tested With|Trino 4nn`

This driver provides access to [Trino][trino], a free and
open source distributed SQL query engine.

## Installation

The Trino driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install trino

```

## Connecting

To use the driver, provide a Trino connection string as the `uri` option. The driver supports URI format and DSN-style connection strings, but URIs are recommended.

```python
from adbc_driver_manager import dbapi

dbapi.connect(
  driver="trino",
  db_kwargs={
      "uri": "http://user@localhost:8080?catalog=tcph&schema=tiny"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

## Connection String Format

```
trino://[user[:password]@]host[:port][/catalog[/schema]][?attribute1=value1&attribute2=value2...]
```

Components:
- Scheme: trino:// (required)
- User: Optional (for authentication)
- Password: Optional (for authentication, requires user)
- Host: Required (no default)
- Port: Optional (defaults to 8080 for HTTP, 8443 for HTTPS)
- Catalog: Optional (Trino catalog name)
- Schema: Optional (schema within catalog)
- Query params: Trino connection attributes

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`. If you include a zone ID in an IPv6 address, the `%` character used as the separator must be replaced with `%25`.
:::

### HTTPS/SSL Configuration

HTTP Basic authentication is only supported on encrypted connections over HTTPS.

By default, connections use HTTPS. To connect using HTTP, add `SSL=false` as a query parameter:

- `trino://localhost:8080/catalog?SSL=false` → Uses HTTP on port 8080
- `trino://localhost/catalog?SSL=false` → Uses HTTP on default port 8080
- `trino://localhost:8443/catalog?SSL=true` → Uses HTTPS on port 8443
- `trino://localhost:8080/catalog` → Uses HTTPS on port 8080
- `trino://localhost/catalog` → Uses HTTPS on default port 8443

See [Trino JDBC Documentation](https://trino.io/docs/current/client/jdbc.html#parameter-reference) for complete parameter reference and [Trino Concepts](https://trino.io/docs/current/overview/concepts.html#catalog) for more information.

Examples:
- trino://localhost:8080/hive/default
- trino://user:pass@trino.example.com:8080/postgresql/public
- trino://trino.example.com/hive/sales?SSL=true
- trino://user@localhost:8443/memory/default?SSL=true&source=myapp

The driver also supports the Trino DSN format (see [Go Trino Client documentation](https://github.com/trinodb/trino-go-client?tab=readme-ov-file#dsn-data-source-name)), but URIs are recommended.

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
  - bool
* - DATE
  - date32[day]
* - DECIMAL
  - fixed_size_binary
* - DOUBLE PRECISION
  - double
* - INT
  - int32
* - INTERVAL DAY TO SECOND
  - month_day_nano_interval
* - INTERVAL YEAR TO MONTH
  - month_day_nano_interval
* - IPADDRESS
  - string
* - REAL
  - float
* - SMALLINT
  - int16
* - TIME
  - time64[us]
* - TIMESTAMP
  - timestamp[us]
* - TIMESTAMP WITH TIME ZONE
  - timestamp[us, tz=UTC]
* - UUID
  - extension&lt;arrow.uuid&gt;
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
* - binary_view
  - VARBINARY
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - decimal128
  - DECIMAL
* - double
  - DOUBLE PRECISION
* - extension&lt;arrow.uuid&gt;
  - UUID
* - fixed_size_binary
  - VARBINARY
* - float
  - REAL
* - int16
  - SMALLINT
* - int32
  - INT
* - int64
  - BIGINT
* - large_binary
  - VARBINARY
* - large_string
  - VARCHAR
* - string
  - IPADDRESS
* - string
  - VARCHAR
* - string_view
  - VARCHAR
* - time64[us]
  - TIME
* - timestamp[us, tz=UTC]
  - TIMESTAMP WITH TIME ZONE
* - timestamp[us]
  - TIMESTAMP
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
* - binary_view
  - VARBINARY
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - double
  - DOUBLE PRECISION
* - fixed_size_binary
  - NUMERIC
* - fixed_size_binary
  - VARBINARY
* - float
  - REAL
* - int16
  - SMALLINT
* - int32
  - INT
* - int64
  - BIGINT
* - large_binary
  - VARBINARY
* - large_string
  - VARCHAR
* - string
  - VARCHAR
* - string_view
  - VARCHAR
* - time64[us]
  - TIME
* - timestamp[us, tz=UTC]
  - TIMESTAMP WITH TIME ZONE
* - timestamp[us]
  - TIMESTAMP
:::



[trino]: https://trino.io/

## Versions Tested



This driver was tested on the following versions of Trino:

- Trino 478
