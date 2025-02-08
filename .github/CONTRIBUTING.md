# Contributing to Shared Workflows Test

Thank you for your interest in contributing to the **Shared Workflows Test** repository! Your contributions help improve and refine GitHub Actions workflows for better automation. By contributing, you agree to follow our **guidelines and best practices** to ensure a smooth and collaborative process.

## Table of Contents

- [Contributing to Shared Workflows Test](#contributing-to-shared-workflows-test)
  - [Table of Contents](#table-of-contents)
  - [**How to Contribute**](#how-to-contribute)
  - [**Reporting Issues**](#reporting-issues)
  - [**Submitting Pull Requests**](#submitting-pull-requests)
  - [**Branch Naming Conventions**](#branch-naming-conventions)
    - [**Rules**](#rules)
  - [Versioning and Commit Guidelines](#versioning-and-commit-guidelines)
  - [**Commit Types**](#commit-types)
  - [**Style Guidelines**](#style-guidelines)
  - [**Additional Resources**](#additional-resources)

## **How to Contribute**

There are several ways to contribute to this project:

1. **Security Reports**  
   - If you discover a security vulnerability, **do not open a public issue**.  
   - Instead, follow the responsible disclosure guidelines in [SECURITY.md](./SECURITY.md).

2. **Bug Reports**  
   - If you encounter a bug, check the [issue tracker](https://github.com/martakisalex/shared-workflows-test/issues) to see if it has already been reported.  
   - If not, open a **new issue** and provide detailed reproduction steps.

3. **Feature Requests**  
   - Have an idea for a new feature or an improvement?  
   - Open an **issue** and describe your proposal.

4. **Pull Requests**  
   - Fork the repository, make changes, and submit a pull request.
   - Ensure your changes follow the **branch naming conventions** and **commit guidelines** outlined below.

## **Reporting Issues**

Before opening an issue:

- **Check existing issues** to avoid duplicates.
- **Provide clear details**, including:
  - Steps to reproduce the problem.
  - Expected behavior vs. actual behavior.
  - Relevant logs or screenshots (if applicable).

If reporting a **security issue**, please follow the steps outlined in [SECURITY.md](./SECURITY.md).

## **Submitting Pull Requests**

Follow these steps to submit a **PR**:

1. **Fork the Repository**  
   - Click the "Fork" button on GitHub.

2. **Create a New Branch**  
   - Use a descriptive branch name following our [Branch Naming Conventions](#branch-naming-conventions):

   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Make and Commit Your Changes**  
   - Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) when writing commit messages:

   ```bash
   git commit -m "feat: add sample workflow for testing manual triggers"
   ```

4. **Push Your Branch to GitHub**
  
   ```bash
   git push origin feat/your-feature-name
   ```

5. **Open a Pull Request**  
   - Go to the **Pull Requests** tab in GitHub.
   - Select your branch and open a new PR.
   - Ensure your PR title follows the format **`<type>: <short description>`** (see [Commit Types](#commit-types)).

## **Branch Naming Conventions**

To maintain a clean Git history, use the following branch naming format:

```git
<type>/<short-description>
```

- `<type>`: Must be one of `feat`, `fix`, `hotfix`, `chore`, `docs`, `style`, `refactor`, `test`, `ci`, `perf`, `build`.
- `<short-description>`: A concise, hyphen-separated description of the change.

### **Rules**

- Use **lowercase** letters.
- Separate words in `<short-description>` with **hyphens**.
- Keep descriptions **concise but meaningful**.
- PR titles **must match the branch type** for consistency.

## Versioning and Commit Guidelines

This project follows:

- **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)** (`MAJOR.MINOR.PATCH` format).
- **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)** for structured commit messages.
- **[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)** for tracking all changes.

All notable changes to this project are documented in [CHANGELOG.md](../CHANGELOG.md).  
When contributing, ensure your changes are **clearly described** in your PR so they can be reflected in the changelog.

## **Commit Types**

| Type       | Description |
|------------|-------------|
| **feat**   | Introduces a new feature |
| **fix**    | Fixes a bug |
| **docs**   | Updates documentation (e.g., modifying README.md) |
| **style**  | Changes code formatting without affecting functionality |
| **refactor** | Code restructuring without behavior changes |
| **test**   | Adds or updates tests |
| **chore**  | Repository maintenance (e.g., updating dependencies) |
| **ci**     | Updates CI/CD configurations |
| **build**  | Changes related to the build tool or dependencies |
| **perf**   | Improves performance |
| **revert** | Reverts a previous commit |

## **Style Guidelines**

- **Coding Style:** Follow language-specific coding conventions.
- **Documentation:** Update relevant documentation for all changes.
- **Testing:** Ensure new features or fixes include **tests** where applicable.

## **Additional Resources**

- **GitHub Contribution Guide:** [Using Pull Requests](https://docs.github.com/en/github/collaborating-with-pull-requests)  
- **Issue Reporting Best Practices:** [Creating Good Issues](https://www.notion.so/github/How-to-write-good-issues-35a75823b3fd485285c2a983df3306dc)  
- **Semantic Versioning:** [Semantic Versioning 2.0.0](https://semver.org/)  
- **Conventional Commits:** [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/)  
- **Changelog Management:** [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
- **GitHub Actions Documentation:** [GitHub Actions Guide](https://docs.github.com/en/actions)  
- **GitHub Actions Best Practices:** [Best Practices for GitHub Actions](https://docs.github.com/en/actions/best-practices)  
- **Git Branching Model:** [A Successful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)

*Thank you for contributing to Shared Workflows Test! Your efforts help improve and refine our GitHub Actions workflows.*
