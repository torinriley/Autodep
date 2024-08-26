# AutoDep for JavaScript

AutoDep for JavaScript is a command-line tool that automatically scans your JavaScript/Node.js project for dependencies and generates a `package.json` file. This simplifies dependency management by ensuring your project’s dependencies are always listed.

## Features

- **Automatic Dependency Scanning:** Scans your project for all `require()` statements and identifies required dependencies.
- **package.json File Generation:** Generates a `package.json` file with all detected dependencies, ready for use with npm.
- **Customizable Output:** Specify the directory to scan and the output path for the generated `package.json` file.

## Installation

You can use AutoDep directly by downloading the script, or clone the repository:

```bash
git clone https://github.com/torinriley/Autodep.git
cd Autodep/javascript
