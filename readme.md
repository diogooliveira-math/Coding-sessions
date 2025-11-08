# Coding Sessions

This folder serves as a dumping ground for coding experiments across different programming languages.

## Table of Contents

- [Setup for Contributors](#setup-for-contributors)
- [Organization](#organization)
- [Current Projects](#current-projects)
- [Utilities](#utilities)
- [VS Code Configuration](#vs-code-configuration-vscode)
- [TODO List](#todo-list)

## Setup for Contributors

To use this repository:
1. Install Maxima from [maxima.sourceforge.net](https://maxima.sourceforge.net/).
2. The Maxima installation path is hardcoded in the VS Code tasks for simplicity. If your installation is in a different location, update the path in `.vscode/tasks.json`.
3. The `.gitignore` file excludes the `Maxima/doc/` folder to keep the repository focused on your code.

## Organization

Files are organized by day using the following naming convention:
- `day1.*` - First day experiments
- `day2.*` - Second day experiments
- `day3.*` - Third day experiments
- etc.

Each day may contain experiments in various programming languages and technologies.

## Current Projects

- **Maxima**: Symbolic computation and mathematical modeling experiments (days 1-2 completed). See [Maxima/README.md](Maxima/README.md) for details.

## Utilities

- `new_day.ps1`: A PowerShell script to create new day files in subfolders. It prompts for a folder name, finds the next available day number based on existing `day*.mac` files, and creates an empty `dayN.mac` file.

## VS Code Configuration (.vscode/)

The `.vscode/` folder contains configuration files that enhance the development experience in VS Code:

- `tasks.json`: Defines two build tasks:
  - "Run Maxima Script": Executes the current `.mac` file using Maxima in batch mode (hardcoded path: `C:\maxima-5.48.1\bin\maxima.bat`), with output displayed in a dedicated terminal panel.
  - "Create New Day File": Runs the `new_day.ps1` script to generate new day files.

- `settings.json`: Configures VS Code settings including terminal placement and defines a multi-command "runMaximaSideBySide" that splits the editor, runs the Maxima script in the right pane, and moves the terminal to the editor area.

- `keybindings.json`: Binds the key combination `Ctrl+Shift+Alt+N` to execute the "Create New Day File" task for quick access.## TODO List

# TODO list

- [ ] Enhance the "Run Maxima Script" task to automatically split the terminal panel to the right, simplifying the workflow.
    - Possible approaches:
        1. Develop a custom VS Code extension to interact with VS Code internals.
        2. Utilize an existing VS Code extension that supports terminal splitting.
