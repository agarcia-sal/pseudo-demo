def calculate_modified_quantity(quantity, divisor):
    # Divide quantity by divisor to get total units and remainder
    total_units = quantity // divisor
    remainder = quantity % divisor
    
    # Return the required modified quantity based on the remainder
    if remainder > 0:
        return remainder * (total_units + 1)
    else:
        return quantity

# Read three integers from input
quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

# Calculate the modified quantities
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result by multiplying the modified quantities
final_result = modified_quantity_a * modified_quantity_b

# Output the final result
print(final_result)
