# Lean Projects

This folder contains prototype Lean projects developed as part of the Coding Sessions initiative. These are experimental or learning-oriented projects that demonstrate various concepts in Lean 4, including theorem proving, functional programming, and project organization.

## Overview

The projects in this folder may utilize utilities, shared libraries, or code snippets from elsewhere in the workspace, such as the main `Lean/` folder (e.g., documentation or common definitions). Each project is self-contained with its own build configuration but can reference external resources as needed.

## Lean Project Structure Basics

A basic Lean project follows a standard structure managed by the Lake build tool. Here's an overview, with special focus on configuring the first project (`Knowledge_base`):

### Essential Files

- **`lean-toolchain`**: A plain text file specifying the Lean version. For `Knowledge_base`, it's set to `leanprover/lean4:stable` to use the latest stable release. This ensures consistency across environments via Elan.

- **`lakefile.toml`**: The main configuration file in TOML format. It defines:
  - `name`: Project identifier (e.g., "knowledge-base").
  - `version`: Semantic version (e.g., "0.1.0").
  - `[[lean_lib]]`: Defines a library target, with `name` and `root` (entry file, e.g., "Main").
  - `[[lean_exe]]`: Defines an executable target, with `name`, `root`, and optionally `supportInterpreter` for IO support.
  - Dependencies: Use `[[require]]` for external packages.

  For `Knowledge_base`, the `lakefile.toml` includes both a library (`KnowledgeBase`) and executable (`knowledge-base`) rooted at `Main.lean`, allowing it to be built as a library or run as a program.

- **`Main.lean`**: The primary source file, often containing the `main` function for executables or key definitions for libraries. In `Knowledge_base`, it includes a simple hello message and IO output.

### Optional Directories

- **`src/`**: For organizing additional source files beyond `Main.lean`.
- **`test/`**: For test suites, typically using Lean's testing framework.
- **`docs/`**: For project-specific documentation or notes.

### Configuring Your First Project

To set up a new Lean project (like `Knowledge_base`):

1. Create the project directory.
2. Add `lean-toolchain` with your desired Lean version (e.g., `leanprover/lean4:stable`).
3. Create `lakefile.toml` with basic metadata and targets. Start simple: define a name, version, and one `[[lean_lib]]` or `[[lean_exe]]`.
4. Add `Main.lean` with initial code (e.g., a `main` function for executables).
5. Run `lake update` to initialize dependencies.
6. Run `lake build` to compile.
7. For executables, run `lake run <exe-name>` to execute.

Ensure Elan is installed for toolchain management. Refer to the `Lean/README.md` for general Lean setup in this workspace.

## Projects in This Folder

- **`Knowledge_base`**: A foundational project for storing definitions, theorems, and examples. Serves as a reference and demonstrates basic project setup.

Add new projects by creating subdirectories with the above structure. Each should have its own README.md for specifics.
