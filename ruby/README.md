# AutoDep for Ruby

AutoDep for Ruby is a command-line tool that automatically scans your Ruby project for dependencies and generates a `Gemfile`. This simplifies dependency management by ensuring your project’s required gems are always listed.

## Features

- **Automatic Dependency Scanning:** Scans your project for all `require` statements and identifies required gems.
- **Gemfile Generation:** Generates a `Gemfile` with all detected dependencies, ready for use with Bundler.
- **Customizable Output:** Specify the directory to scan and the output path for the generated `Gemfile`.

## Installation

You can use AutoDep directly by downloading the script, or clone the repository:

```bash
git clone https://github.com/yourusername/autodep.git
cd autodep/ruby
