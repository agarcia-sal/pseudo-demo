def calculate_modified_quantity(quantity, divisor):
    # Calculate total units and remainder by dividing quantity by divisor
    total_units, remainder = divmod(quantity, divisor)
    
    # If there's a remainder, return the modified quantity
    if remainder > 0:
        return remainder * (total_units + 1)
    else:
        return quantity

# Read three integers from input
quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

# Calculate modified quantities
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result
final_result = modified_quantity_a * modified_quantity_b

# Output the final value
print(final_result)
