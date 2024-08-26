# AutoDep

AutoDep is a command-line tool that automatically scans your Python project for dependencies and generates a `requirements.txt` file. It simplifies dependency management by ensuring your project’s requirements are always up-to-date.

## Features

- **Automatic Dependency Scanning:** AutoDep scans your project for all `import` statements and identifies the required dependencies.
- **Requirements File Generation:** It generates a `requirements.txt` file with all detected dependencies, ready to use with `pip`.
- **Customizable Output:** Specify the directory to scan and the output path for the generated `requirements.txt` file.


## Supported Languages

- [Python](python/README.md)
- [JavaScript](javascript/README.md)
- [Ruby](ruby/README.md)

## Getting Started
Each language version has its own setup and usage instructions. Please navigate to the directory for the language you are interested in:

- **Python:** `cd python` and follow the instructions in `python/README.md`.
- **JavaScript:** `cd javascript` and follow the instructions in `javascript/README.md`.
- **Ruby:** `cd ruby` and follow the instructions in `ruby/README.md`.

## Contributing

Contributions are welcome for new languages or improvements to existing versions. Please see the CONTRIBUTING.md file in each language directory for specific guidelines.

## Installation

Install AutoDep using pip:

```bash
pip install autodep

