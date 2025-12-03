---
# Copyright (c) 2025 Columnar Technologies Inc.  All rights reserved.
{}
---

# Microsoft SQL Server

:::{toctree}
:maxdepth: 1
:hidden:

v1.0.0.md
:::

[{badge-primary}`Driver Version|v1.0.0`](#driver-mssql-v1.0.0) {badge-success}`Tested With|Microsoft SQL Server 2022`

This driver provides access to [Microsoft SQL Server][mssql].

:::{note}
This project is not affiliated with Microsoft.
:::

## Installation

The Microsoft SQL Server driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install mssql
```

## Connecting

To connect, edit the `uri` option below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

dbapi.connect(
    driver="mssql",
    db_kwargs={
        "uri": "sqlserver://sa:Co1umn&r@localhost:1433?database=demo"
    }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

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
      <td>✅</td>
    </tr>
    <tr>
      <td>Specify target catalog</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Specify target schema</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td>✅</td>
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
      <td colspan="2">✅</td>
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
      <td colspan="2">✅</td>
    </tr>
  </tbody>
</table>

### Types

#### SQL Server to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - SQL Type
  - Arrow Type
* - BIGINT
  - int64
* - BIT
  - bool
* - DATE
  - date32[day]
* - DATETIME
  - timestamp[us, tz=UTC]
* - DATETIME2
  - timestamp[us, tz=UTC]
* - DOUBLE PRECISION
  - double
* - INT
  - int32
* - NUMERIC
  - decimal128
* - REAL
  - float
* - SMALLINT
  - int16
* - TIME
  - time64[ns] ⚠️ [^1]
* - TIME(0)
  - time32[s]
* - TIME(1)
  - time32[ms]
* - TIME(2)
  - time32[ms]
* - TIME(3)
  - time32[ms]
* - TIME(4)
  - time64[us]
* - TIME(5)
  - time64[us]
* - TIME(6)
  - time64[us]
* - TIME(7)
  - time64[ns]
* - VARBINARY
  - binary
* - VARCHAR
  - string
:::

#### Arrow to SQL Server

<table class="docutils data align-default" style="width: 100%;">
  <tr>
    <th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
    <th colspan="2" style="text-align: center;">SQL Server Type</th>
  </tr>
  <tr>
    <th style="text-align: center;">Bind</th>
    <th style="text-align: center;">Ingest</th>
  </tr>
  <tr>
    <td>binary</td>
    <td style="text-align: center;">VARBINARY</td>
    <td style="text-align: center;">VARBINARY(MAX)</td>
  </tr>
  <tr>
    <td>bool</td>
    <td style="text-align: center;">BOOLEAN</td>
    <td style="text-align: center;">BIT</td>
  </tr>
  <tr>
    <td>date32[day]</td>
    <td colspan="2" style="text-align: center;">DATE</td>
  </tr>
  <tr>
    <td>decimal128</td>
    <td colspan="2" style="text-align: center;">NUMERIC</td>
  </tr>
  <tr>
    <td>double</td>
    <td colspan="2" style="text-align: center;">DOUBLE PRECISION</td>
  </tr>
  <tr>
    <td>float</td>
    <td colspan="2" style="text-align: center;">REAL</td>
  </tr>
  <tr>
    <td>int16</td>
    <td colspan="2" style="text-align: center;">SMALLINT</td>
  </tr>
  <tr>
    <td>int32</td>
    <td colspan="2" style="text-align: center;">INT</td>
  </tr>
  <tr>
    <td>int64</td>
    <td colspan="2" style="text-align: center;">BIGINT</td>
  </tr>
  <tr>
    <td>string</td>
    <td style="text-align: center;">VARCHAR</td>
    <td style="text-align: center;">NTEXT</td>
  </tr>
  <tr>
    <td>time32[ms]</td>
    <td style="text-align: center;">TIME(1), TIME(2), TIME(3)</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^2]

</td>
  </tr>
  <tr>
    <td>time32[s]</td>
    <td style="text-align: center;">TIME(0)</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^2]

</td>
  </tr>
  <tr>
    <td>time64[ns]</td>
    <td style="text-align: center;">TIME(7)</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^3]

</td>
  </tr>
  <tr>
    <td>time64[us]</td>
    <td style="text-align: center;">TIME, TIME(4), TIME(5), TIME(6)</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^2]

</td>
  </tr>
  <tr>
    <td>timestamp[us]</td>
    <td style="text-align: center;">DATETIME</td>
    <td style="text-align: center;">n/a</td>
  </tr>
  <tr>
    <td>timestamp[us, tz=UTC]</td>
    <td style="text-align: center;">n/a</td>
    <td style="text-align: center;">DATETIME2</td>
  </tr>
</table>

## Previous Versions

To see documentation for the current and previous versions of this driver, see the following:

- [v1.0.0](./v1.0.0.md)

[^1]: while the documentation claims 7 digits of precision, the client only receives 6

[^2]: ingested as TIME(7)

[^3]: ingested as TIME(7), so full nanosecond precision is unavailable

[mssql]: https://www.microsoft.com/sql-server
