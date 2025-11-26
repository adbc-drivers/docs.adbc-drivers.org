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

# Amazon Redshift

:::{toctree}
:maxdepth: 1
:hidden:

v1.0.0.md
:::

[{badge-primary}`Driver Version|v1.0.0`](#driver-redshift-v1.0.0)

This driver provides access to [Amazon Redshift][redshift] (commonly referred
to as just "Redshift").

:::{note}
This project is not affiliated with Amazon.
:::

## Installation

The Redshift driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install redshfit
```

## Connecting

To connect, edit the `uri`, `redshift.cluster_type`, `redshift.workgroup_name`, and `redshift.db_name` options below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

dbapi.connect(
    driver="redshift",
    db_kwargs={
        "uri": "postgresql://localhost:5439", # for Redshift Serverless with bastion host
        #"uri": "postgresql://localhost:5440", # for Redshift Provisioned with bastion host
        #"uri": "postgresql://<cluster hostname>:<cluster port>", # for direct connection

        "redshift.cluster_type": "redshift-serverless", # for Redshift Serverless
        #"redshift.cluster_type": "redshift-iam", # for Redshift Provisioned with IAM auth
        #"redshift.cluster_type": "redshift", # for Redshift Provisioned with user/password auth

        "redshift.workgroup_name": "<WORKGROUP_NAME>", # for Redshift Serverless
        #"redshift.cluster_identifier": "<CLUSTER IDENTIFIER>", # for Redshift Provisioned

        "redshift.db_name": "sample_data_dev",
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
      <td>❌</td>
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

#### Redshift to Arrow

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
* - DOUBLE PRECISION
  - double
* - INT
  - int32
* - INTERVAL DAY TO SECOND
  - month_day_nano_interval
* - INTERVAL YEAR TO MONTH
  - month_day_nano_interval
* - NUMERIC
  - decimal128
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
* - VARBINARY
  - binary
* - VARCHAR
  - string
:::

#### Arrow to Redshift

<table class="docutils data align-default" style="width: 100%;">
  <tr>
    <th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
    <th colspan="2" style="text-align: center;">MySQL Type</th>
  </tr>
  <tr>
    <th style="text-align: center;">Bind</th>
    <th style="text-align: center;">Ingest</th>
  </tr>
  <tr>
    <td>binary</td>
<td style="text-align: center;">

⚠️
[^2]

</td>
    <td style="text-align: center;">VARBINARY</td>
  </tr>
  <tr>
    <td>bool</td>
    <td colspan="2" style="text-align: center;">BOOLEAN</td>
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
<td style="text-align: center;">

REAL ⚠️
[^1]

</td>
    <td style="text-align: center;">REAL</td>
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
    <td colspan="2" style="text-align: center;">VARCHAR</td>
  </tr>
  <tr>
    <td>time64[us]</td>
    <td style="text-align: center;">TIME</td>
    <td style="text-align: center;">

❌
[^3]

</td>
  </tr>
  <tr>
    <td>timestamp[us, tz=UTC]</td>
    <td colspan="2" style="text-align: center;">TIMESTAMP</td>
  </tr>
  <tr>
    <td>timestamp[us]</td>
    <td colspan="2" style="text-align: center;">TIMESTAMP</td>
  </tr>
</table>


## Previous Versions

To see documentation for the current and previous versions of this driver, see the following:

- [v1.0.0](./v1.0.0.md)

[^1]: precision is limited

[^2]: null bytes in bind parameters will instead end the value (e.g. [A, 0x00, B] will instead get inserted as [A])

[^3]: Redshift raises an ASSERT

[redshift]: https://aws.amazon.com/redshift/
