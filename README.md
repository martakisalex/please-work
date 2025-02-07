# Shared Workflows Test

[![Build Status](https://github.com/martakisalex/shared-workflows-test/actions/workflows/ci.yml/badge.svg)](https://github.com/martakisalex/shared-workflows-test/actions)
[![WIP](https://img.shields.io/badge/status-WIP-orange)](https://github.com/martakisalex/shared-workflows-test)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/martakisalex/shared-workflows-test)](https://github.com/martakisalex/shared-workflows-test/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/martakisalex/shared-workflows-test)](https://github.com/martakisalex/shared-workflows-test/graphs/contributors)

## Overview

Welcome to **Shared Workflows Test**, a repository dedicated to testing and validating GitHub Actions workflows before they are merged into the main [shared-workflows](https://github.com/martakisalex/shared-workflows) repository. This project provides a safe sandbox with sample code and varied workflow configurations to ensure robust, reusable CI/CD pipelines.

## Table of Contents

- [Shared Workflows Test](#shared-workflows-test)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Contents](#contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Running Workflows](#running-workflows)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)
  - [Changelog](#changelog)

## Purpose

- **Test Workflows**: Validate GitHub Actions workflows to ensure they perform as expected.
- **Experimentation**: Provide a controlled environment for iterating and refining workflow configurations.
- **Ensure Compatibility**: Confirm that workflows work across different languages, frameworks, and environments.

## Contents

- **Sample Code**: Example projects spanning multiple languages and frameworks to simulate real-world scenarios.
- **GitHub Actions Workflows**: Predefined configurations to automate various CI/CD tasks.
- **Documentation**: Instructions and guidelines to help you use and test these workflows effectively.

## Getting Started

Follow these instructions to set up the repository locally and start testing workflows.

### Prerequisites

- **Git**: Ensure Git is installed on your machine. [Download Git](https://git-scm.com/)
- **GitHub Account**: Required for accessing and triggering GitHub Actions.
- **Runtime Environment**: Required if your sample code or workflows rely on a specific language runtime. (Optional)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/martakisalex/shared-workflows-test.git
   cd shared-workflows-test
   ```

2. **Configure Sample Code**

   Adjust sample projects as needed to reflect your testing scenarios.

### Running Workflows

1. **Automatic Triggers**

   - Push changes to the repository to trigger workflows automatically via GitHub Actions.

2. **Manual Triggers**

   - Some workflows are configured to be manually triggered using `workflow_dispatch`. You can start these directly from the GitHub Actions tab in your repository.

3. **Review Workflow Logs**

   - Visit the [Actions](https://github.com/martakisalex/shared-workflows-test/actions) tab on GitHub to monitor workflow runs and review detailed logs.

## Contributing

We welcome contributions to this project. Please review our [Contributing Guidelines](.github/CONTRIBUTING.md) to get started.

## Contact

For questions, suggestions, or issues, feel free to reach out:

- **Email**: [martakisalex@gmail.com](martakisalex@gmail.com)
- **GitHub Issues**: [Create an Issue](https://github.com/martakisalex/shared-workflows-test/issues)

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for a complete history of changes.
