# Maxima Coding Sessions

This folder contains Maxima scripts for daily coding experiments and problem-solving sessions. Maxima is a computer algebra system used for symbolic computation, mathematical modeling, and solving equations.

## Setup

- Maxima is installed at: `C:\maxima-5.48.1\bin\maxima.bat`
- To run a script, use the batch file (e.g., `run_day1.bat`) or execute directly with Maxima.

## Organization

Files are organized by day:
- `day1.mac` - Introduction to Maxima: basic arithmetic, symbolic expressions, differentiation, integration, equation solving, and function definitions.
- `day2.mac` - Comprehensive exploration of Maxima features:
  - Part 1: Budget calculations with state revenue and expenses (education, health, interest), including percentage calculations.
  - Part 2: Implementation of the "rule of three" (rule of proportion) for proportional calculations.
  - Part 3: Per capita and monthly per capita revenue calculations.
  - Part 4: Detailed explanation and examples of Maxima's assignment operators (: for variables vs := for functions).
  - Part 5: Multi-year budget analysis using lists, percentage mapping, budget differences, custom function definition, equation solving, and 2D plotting.

## Running Scripts

### Using Batch File
- For day1: Run `run_day1.bat` to execute `day1.mac` in batch mode.

### Manual Execution
- Open command prompt in this folder.
- Run: `"C:\maxima-5.48.1\bin\maxima.bat" -b day1.mac`

### Interactive Mode
- Run: `"C:\maxima-5.48.1\bin\maxima.bat"`
- Then load the script: `batch("day1.mac");`

## Creating New Day Files

Use the `new_day.ps1` script in the parent directory to create new day files. It prompts for the folder name (e.g., "Maxima") and creates the next numbered `dayN.mac` file.

## Context for Future Sessions

This workspace is part of a broader "Coding Sessions" project for daily programming challenges. Each day focuses on different concepts or problems, using Maxima for mathematical computations. Day 1 covers basics, while Day 2 appears to involve financial calculations, possibly for a budgeting problem.