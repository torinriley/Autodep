# AutoDep

AutoDep is a command-line tool that automatically scans your Python project for dependencies and generates a `requirements.txt` file. It simplifies dependency management by ensuring your project’s requirements are always up-to-date.

## Features

- **Automatic Dependency Scanning:** AutoDep scans your project for all `import` statements and identifies the required dependencies.
- **Requirements File Generation:** It generates a `requirements.txt` file with all detected dependencies, ready to use with `pip`.
- **Customizable Output:** Specify the directory to scan and the output path for the generated `requirements.txt` file.

## Installation

Install AutoDep using pip:

```bash
pip install autodep

