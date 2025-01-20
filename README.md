# HW1 Submission for ChemE 545

This repository contains my submission for HW1 of ChemE 545. The included files are designed to address specific challenges in chemical engineering using structured and efficient Python programming practices.

## Files

### `extract_parameter.py`
This script retrieves specific process parameters from a predefined dataset. It takes three inputs:
1. **Unit name** (e.g., "reactor" or "distillation_column")
2. **Parameter name** (e.g., "temperature" or "pressure")
3. **Index** (e.g., 0, 1, 2)

The script searches for the corresponding value in a dictionary of process data and returns it in a structured format. If any of the inputs are invalid, it provides an error message.

### `calculate_solution_weights.py`
This script calculates the weight of chemical solutions based on their molar concentration and molecular weight. It uses:
- A dictionary of molecular weights for common chemicals
- A list of chemical formulas with specified concentrations

The script calculates the required weight (in grams) for 1 liter of solution. If a chemical is not found in the molecular weight dictionary, it is marked as "unknown."

### `README.md`
This document provides an overview of the repository, explains the functionality of the Python scripts, and offers step-by-step instructions on how to use them. It serves as a guide for running the scripts and understanding their outputs.

## Instructions for Use

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
2. cd HW1_Yase_Muna
3. python3 extract_parameter.py
4. python3 calculate_solution_weights.py
