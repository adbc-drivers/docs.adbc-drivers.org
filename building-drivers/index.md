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

While ADBC is an open standard, few external contributors have successfully built and released ADBC drivers outside the Apache ecosystem. The purpose of the Foundry is to change that. The Foundry provides all of the resources that were previously missing for database vendors and users to easily build their own drivers.

The Foundry provides:

- A home for your drivers in our [adbc-drivers](https://github.com/adbc-drivers) GitHub organization
- Well-tested and feature complete SDKs for building drivers in a variety of languages
- Ready to run CI workflows for building, testing, and releasing drivers on all major platforms
- A powerful driver validation suite to help you test and document your drivers capabilities
- A place to host documentation for your driver (this website)

If you're interested in building a driver with the Foundry, continue reading to understand the process. If you have any questions, we encourage you to join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w) or to file an issue at [adbc-drivers/onboarding](https://github.com/adbc-drivers/onboarding).

## Repository Modes

Your code can live in a repo in the [adbc-drivers](https://github.com/adbc-drivers) organization or under your GitHub organizationn

**Internal**: If you choose to develop under [adbc-drivers](https://github.com/adbc-drivers), Foundry staff can grant your team members enough permission to operate entirely independently, including managing secrets and environments for access to external cloud resources.

**External:** If you prefer to develop your driver under your own organization, Foundry staff can create a build-only repository for your driver under adbc-drivers.org.

## Process

At a high level, here's what the process looks like to from zero to a fully released and dbc-installable drivers.

1. File an issue at [adbc-drivers/onboarding](https://github.com/adbc-drivers/onboarding). Fill in the template describing the driver you want to build or contribute.
2. Foundry staff creates a repo under adbc-drivers.org for your driver
3. Foundry staff adds templates with common workflows, CI, and validation
4. They invite members of your team and give you appropriate access
5. You develop the driver as you see fit
6. When you tag a release, Foundry staff can help coordinate making it available with [dbc](https://columnar.tech/dbc)

## Resources

### SDKs

The Foundry is focused on building drivers that can be loaded by an ADBC Driver Manager. Under this mode, drivers can be written in any language that can export a C ABI.

In pratice, most drivers are written in C/C++, Go, or Rust.

And because Go and Rust are such common choices, the Foundry provides frameworks for both languages that include helpers for common concerns such as error handling and managing result sets, testing, and more:

- Go: [driverbase-go](https://github.com/adbc-drivers/driverbase-go)
- Rust: [driverbase-rs](https://github.com/adbc-drivers/driverbase-rs/)

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

### Who owns the repo under adbc-drivers?

TODO: Talk about how we envision that the driver/author will be who owns the repo and that the Foundry will help manage it.

### After I build my driver, how does it become available with dbc?

TODO

### Who is responsible for releasing?

TODO

### Who is responsible for responding to issues?

TODO

### What's the best language for writing drivers?

TODO
