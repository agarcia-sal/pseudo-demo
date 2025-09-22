def calculate_modified_quantity(quantity, divisor):
    # Calculate the total number of complete groups and the remainder
    total_units = quantity // divisor  # Integer division to get total units
    remainder = quantity % divisor  # Remainder after division
    
    # Check if there is a remainder
    if remainder > 0:
        # Return the product of the remainder and one more than total units
        return remainder * (total_units + 1)
    else:
        # If there is no remainder, return the original quantity
        return quantity

# Read input values from the user
quantity_a = int(input())  # First input value
quantity_b = int(input())  # Second input value
divisor = int(input())      # Third input value (divisor)

# Calculate the modified quantities using the function
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result as the product of the two modified quantities
final_result = modified_quantity_a * modified_quantity_b

# Output the final value
print(final_result)
