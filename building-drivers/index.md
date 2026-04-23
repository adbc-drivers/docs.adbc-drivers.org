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

# Building Drivers

While ADBC is an open standard, few external contributors have successfully built and released ADBC drivers outside the Apache ecosystem. The purpose of the foundry is to change that. The foundry provides all of the resources that were previously missing for database vendors and users to easily build their own drivers.

The Foundry provides:

- A home for your drivers in our adbc-drivers org
- Well-tested and feature complete SDKs for building drivers in a variety of languages
- Ready to run CI workflows for building, testing, and releasing drivers
- An advanced validation suite to help you test and document your drivers capabilities

If you're interested in building a driver, continue reading to understand the process of building a driver with the Foundry. If you have any questions, we encourage you to join the Columnar Community Slack.

## Process

At a high level, here's what the process looks like to from zero to a fully released and dbc-installable drivers.

1. Contact us (tell how)
2. Foundry staff creates a repo under adbc-drivers.org for your driver
3. Foundry staff creates a template repo with common workflows, CI, and validation
4. They invite members of your team and give you appropriate access
5. You develop the driver
6. Profit

## Resources

Outline...
Questions people have:

- Implementation Language
- CI
- Testing / Validation
- Building for all platforms
- Distribution
- Licensing

### SDKs

TODO: Talk about driverbases and implementation language.

### Testing

TODO: Unit testing and validation are used together to test drivers and validation is used to document drivers accurately.

### Validation

TODO: Talk about validation suite, how we bootstrap it, how you run it, what it is doing.

### CI

TODO: Talk about the CI workflows and generate.toml

### Licensing

TODO: Talk about licensing considerations.

## FAQ

### Why not under apache/arrow-adbc?

TODO: Talk about this
