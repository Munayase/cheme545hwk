unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}

# Function to fetch and format data for a specific unit operation and feature
def fetch_parameter_data(unit, feature, idx):
    """
    Fetches the value of a specified feature for a given unit operation and index.
    
    Args:
        unit (str): The unit operation (e.g., "distillation_column", "reactor").
        feature (str): The feature to retrieve (e.g., "temperature", "pressure").
        idx (int): The index of the value to retrieve.
        
    Returns:
        str: A formatted string combining the unit, feature, and value, 
             or "Invalid input" if an error occurs.
    """
    try:
        # Retrieve the feature value and format it as a string
        feature_value = str(unit_operations_data[unit][feature][idx])
        return f"{unit}_{feature}_{feature_value}"
    except (KeyError, IndexError):  # Handle cases where unit, feature, or index is invalid
        return "Invalid input"
