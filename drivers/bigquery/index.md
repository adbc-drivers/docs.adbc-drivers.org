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

# Google BigQuery Driver

:::{toctree}
:maxdepth: 1
:hidden:

v0.1.1.md
prerelease.md
:::

[{badge-primary}`Driver Version|v0.1.1`](#driver-bigquery-v0.1.1 "Permalink") {badge-success}`Tested With|Google BigQuery 1.72.0`

:::{note}
This project is not associated with Google.
:::

This driver provides access to [Google BigQuery][bigquery], a data warehouse
offered by Google Cloud.

## Installation

The BigQuery driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install bigquery
```

## Pre-requisites

Using the BigQuery driver requires some setup before you can connect:

1. Create a [Google Cloud account](http://console.cloud.google.com)
1. Install the [Google Cloud CLI](https://cloud.google.com/cli) (for managing credentials)
1. Authenticate with Google Cloud
    - Run `gcloud auth application-default login`
1. Create, find, or reuse a project and dataset (record these for later)

## Connecting

To connect, replace `my-gcp-project` and `my-gcp-dataset` below with the appropriate values for your situation and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="bigquery",
  db_kwargs={
      "adbc.bigquery.sql.project_id": "my-gcp-project",
      "adbc.bigquery.sql.dataset_id": "my-gcp-datase"
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
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target catalog</td>
      <td>❌</td>
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

#### SELECT (SQL to Arrow) type mapping

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - SQL Type
  - Arrow Type
* - ARRAY
  - list [^1]
* - BIGNUMERIC
  - decimal256(76, 38)
* - BOOL
  - bool
* - BOOLEAN
  - bool
* - BYTES
  - binary
* - DATE
  - date32[day]
* - DATETIME
  - timestamp[us] [^2]
* - FLOAT64
  - double
* - GEOGRAPHY
  - extension&lt;geoarrow.wkt&gt;
* - INT64
  - int64
* - INTERVAL
  - month_day_nano_interval
* - JSON
  - extension&lt;arrow.json&gt;
* - NUMERIC
  - decimal128(38, 9) [^3] [^4] [^5]
* - RANGE&lt;DATE&gt;
  - struct&lt;start: date32[day], end: date32[day]&gt;
* - RANGE&lt;DATETIME&gt;
  - struct&lt;start: timestamp[us], end: timestamp[us]&gt;
* - RANGE&lt;TIMESTAMP&gt;
  - struct&lt;start: timestamp[us, tz=UTC], end: timestamp[us, tz=UTC]&gt;
* - STRING
  - string
* - STRUCT
  - struct
* - TIME
  - time64[us]
* - TIMESTAMP
  - timestamp[us, tz=UTC] [^6]
:::

#### Bind parameter (Arrow to SQL) type mapping

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - Arrow Type
  - SQL Type
* - binary
  - BYTES
* - binary_view
  - BYTES
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - decimal128
  - NUMERIC
* - double
  - FLOAT64
* - fixed_size_binary
  - BYTES
* - int64
  - INT64
* - large_binary
  - BYTES
* - large_string
  - STRING
* - string
  - STRING
* - string_view
  - STRING
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
  - BYTES
* - binary_view
  - ❌ [^7]
* - bool
  - BOOLEAN
* - date32[day]
  - DATE
* - decimal128
  - NUMERIC
* - double
  - FLOAT64
* - fixed_size_binary
  - VARBINARY
* - float
  - FLOAT64
* - int16
  - INT64
* - int32
  - INT64
* - int64
  - INT64
* - large_binary
  - VARBINARY
* - large_string
  - VARCHAR
* - list
  - ARRAY [^8] [^9] [^10]
* - string
  - STRING
* - string_view
  - ❌ [^11]
* - struct
  - STRUCT
* - time64[us]
  - TIME
* - timestamp[us, tz=UTC]
  - TIMESTAMP
* - timestamp[us]
  - ❌ [^12]
:::

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v0.1.1](./v0.1.1.md)

[^1]: BigQuery treats NULL arrays as empty arrays in result sets, even though you can differentiate between them during query execution.  See https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_nulls for more details.

[^2]: BigQuery's datetime is a naive timestamp; use TIMESTAMP for zoned timestamps

[^3]: Negative scales are not supported

[^4]: Scale must be in [0, 9]

[^5]: The declared precision/scale is ignored in queries: it will always be decimal128(38, 9)

[^6]: BigQuery's timestamp is effectively an Instant; use DATETIME for naive timestamps

[^7]: arrow-go does not support writing binary view to Parquet

[^8]: BigQuery does not support NULL lists; it will instead return an empty list

[^9]: BigQuery does not support NULL list elements; it will instead raise an error

[^10]: See the BigQuery documentation for the [ARRAY type](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type)

[^11]: arrow-go does not support writing string view to Parquet

[^12]: This is broken on Google's side, as BigQuery doesn't properly parse Parquet types. See https://github.com/googleapis/google-cloud-python/issues/6542.

[bigquery]: https://cloud.google.com/bigquery/
