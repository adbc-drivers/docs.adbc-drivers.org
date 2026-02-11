---
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
{}
---

(driver-clickhouse-v0.1.0-alpha.1)=
# ClickHouse Driver v0.1.0-alpha.1

[{badge-primary}`Driver Version|v0.1.0-alpha.1`](#driver-clickhouse-v0.1.0-alpha.1 "Permalink") {badge-success}`Tested With|ClickHouse 25.12`

This driver provides access to [ClickHouse][clickhouse], an open-source data warehouse and analytical database.  It is developed by ClickHouse, Inc.  The source code can be found at [adbc_clickhouse](https://github.com/ClickHouse/adbc_clickhouse); the ADBC Driver Foundry distributes precompiled binaries of the upstream sources for Linux, macOS, and Windows.

ClickHouse is a trademark of ClickHouse, Inc. https://clickhouse.com

## Installation

The ClickHouse driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre clickhouse
```

:::{note}
Only prerelease versions of the driver are currently available, so you must use `--pre` with dbc 0.2.0 or newer to install the driver.
:::

## Connecting

To use the driver, provide the URI of a ClickHouse database as the `uri` option.

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="clickhouse",
  db_kwargs={
      "uri": "http://localhost:8123/",
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
      <td>❌</td>
    </tr>
    <tr>
      <td>Append</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td>❌</td>
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
      <td>❌</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Get Parameter Schema</td>
      <td colspan="2">❌</td>
    </tr>
    <tr>
      <td>Get Table Schema</td>
      <td colspan="2">❌</td>
    </tr>
    <tr>
      <td>Prepared Statements</td>
      <td colspan="2">❌</td>
    </tr>
    <tr>
      <td>Transactions</td>
      <td colspan="2">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### ClickHouse to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - ClickHouse Type
  - Arrow Type
* - Boolean
  - bool
* - Date32
  - date32[day] [^1]
* - DateTime64 (no time zone)
  - timestamp[us] (with time zone) [^2] [^3]
* - DateTime64 (with time zone)
  - timestamp[us] (with time zone) [^3]
* - Decimal
  - decimal128
* - Float32
  - float
* - Float64
  - double
* - Int16
  - int16
* - Int32
  - int32
* - Int64
  - int64
* - String
  - string
* - Time
  - ❌ [^4]
:::

#### Arrow to ClickHouse

<table class="docutils data align-default" style="width: 100%;">
  <tr>
    <th rowspan="2" style="text-align: center; vertical-align: middle;">Arrrow Type</th>
    <th colspan="2" style="text-align: center;">ClickHouse Type</th>
  </tr>
  <tr>
    <th style="text-align: center;">Bind</th>
    <th style="text-align: center;">Ingest</th>
  </tr>
<tr>
  <td>binary</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>binary_view</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>bool</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>date32[day]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>decimal128</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>double</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>fixed_size_binary</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>float</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>halffloat</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(not tested)

</td>

</tr>
<tr>
  <td>int16</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>int32</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>int64</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>large_binary</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>large_string</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>string</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>string_view</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>time32[ms]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>time32[s]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>time64[ns]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>time64[us]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[ms]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[ms] (with time zone)</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[ns]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[ns] (with time zone)</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[s]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[s] (with time zone)</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[us]</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
<tr>
  <td>timestamp[us] (with time zone)</td>


<td colspan="2" style="text-align: center;">

❌

</td>

</tr>
</table>

[^1]: Date32 has limited range (1900-01-01 to 2299-12-31)

[^2]: ClickHouse datetime without timezone is interpreted in **server** timezone

[^3]: DateTime64 has limited range (1900 to 2299)

[^4]: ClickHouse Time type is not supported in Arrow format export

[clickhouse]: https://clickhouse.com/
