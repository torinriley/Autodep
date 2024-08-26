# AutoDep for Python

AutoDep for Python is a command-line tool that automatically scans your Python project for dependencies and generates a `requirements.txt` file. This simplifies dependency management by ensuring your project’s requirements are always up-to-date.

## Features

- **Automatic Dependency Scanning:** Scans your project for all `import` statements and identifies required dependencies.
- **Requirements File Generation:** Generates a `requirements.txt` file with all detected dependencies, ready for use with `pip`.
- **Customizable Output:** Specify the directory to scan and the output path for the generated `requirements.txt` file.

## Installation

Install AutoDep using pip:

```bash
pip install autodep
