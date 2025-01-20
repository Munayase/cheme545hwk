# Dictionary containing molecular weights of various chemicals (in g/mol).
molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}
# List of solutions required
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']


# Function to calculate the weights of solutions
def calculate_solution_weights(molecular_weights, solutions_needed):
    # Initialize an empty list to store results
    result = []
    
    # Loop through each solution in the list
    for solution in solutions_needed:
        try:
            # Split the solution into chemical formula and concentration
            chemical_formula, concentration_str = solution.split('-')
            # Convert the concentration (e.g., '0.5M') into a float value
            concentration = float(concentration_str.replace('M', ''))
        except ValueError:
            # If splitting or conversion fails, add 'unknown' to the result
            result.append('unknown')
            continue  # Skip to the next solution
        
        # Check if the chemical formula is in the molecular weights dictionary
        if chemical_formula in molecular_weights:
            # Get the molecular weight of the chemical
            molecular_weight = molecular_weights[chemical_formula]
            # Calculate the weight for 1 litre of solution
            weight = molecular_weight * concentration
            # Format the result as 'chemical-concentration-weight' and add to the list
            result.append(f"{chemical_formula}-{concentration_str}-{weight:.2f}g")
        else:
            # If the chemical is not in the dictionary, add 'unknown' to the result
            result.append('unknown')
    
    # Return the list of results
    return result

# Call the function to calculate weights and store the output
output = calculate_solution_weights(molecular_weights, solutions_needed)

# Print the output to check the results
print(output)
