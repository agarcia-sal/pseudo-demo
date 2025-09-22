# Define the function to calculate modified quantity
def calculate_modified_quantity(quantity, divisor):
    # Calculate total units and remainder
    total_units = quantity // divisor
    remainder = quantity % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        return remainder * (total_units + 1)  # Return modified quantity if remainder exists
    else:
        return quantity  # Return original quantity if no remainder

# Read input values (three integers)
quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

# Calculate two modified quantities using the defined function
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result as the product of the two modified quantities
final_result = modified_quantity_a * modified_quantity_b

# Output the final result
print(final_result)
