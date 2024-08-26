# AutoDep

AutoDep is a Python-based command-line tool that automatically scans your project for dependencies and generates the appropriate dependency file, such as `requirements.txt`, `package.json`, `Gemfile`, and others. AutoDep simplifies dependency management by ensuring your project’s requirements are always up-to-date, regardless of the programming language.

## Features

- **Automatic Dependency Scanning:** AutoDep scans your project for dependency declarations (e.g., `import`, `require`, `use`) and identifies the required packages or modules.
- **Multi-Language Support:** AutoDep supports multiple programming languages and generates the correct dependency file for each language.
- **Customizable Output:** Specify the directory to scan and the output path for the generated dependency file.

## Supported Languages

AutoDep currently supports the following languages:

- **Python:** Generates `requirements.txt`
- **JavaScript/Node.js:** Generates `package.json`
- **Ruby:** Generates `Gemfile`
- **PHP:** Generates `composer.json`
- **Go:** Generates `go.mod`
- **Java:** Generates `pom.xml` (for Maven) or `build.gradle` (for Gradle)

## Installation

Install AutoDep using pip:

```bash
pip install autodep

```
(coming soon)
