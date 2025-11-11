# Lean Coding Sessions

This folder contains Lean scripts and projects for daily coding experiments and problem-solving sessions. Lean is a functional programming language and proof assistant designed for theorem proving, formal verification, and general-purpose programming.

## Setup

- Lean is managed via Elan (Lean toolchain manager). Ensure Elan is installed and `lean` is available in PATH.
- Projects use Lake (Lean's build tool). Run `lake update` to fetch dependencies, `lake build` to compile, and `lake run` to execute executables.

## Organization

Files are organized by day and project structure:

- `lakefile.toml` - Lake configuration for the project.
- `lean-toolchain` - Specifies the Lean version.
- `Main.lean` - Main executable entry point.
- `day1.lean` - Introduction to Lean: basic arithmetic, functions, recursion, and evaluation.

## Running Scripts

### Building the Project

- Open command prompt in this folder.
- Run: `lake build` to compile the project.

### Running the Executable

- Run: `lake run lean-test` to execute the main program.

### Interactive Mode

- Use VS Code with Lean extension for interactive development.
- Open `.lean` files and use `#eval` for evaluation.

## Creating New Day Files

Use the `new_day.ps1` script in the parent directory to create new day files. It prompts for the folder name (e.g., "Lean") and creates the next numbered `dayN.lean` file.

## Context for Future Sessions

This workspace is part of a broader "Coding Sessions" project for daily programming challenges. Each day focuses on different concepts or problems, using Lean for functional programming and theorem proving. Day 1 covers basics, with future days exploring more advanced features.
