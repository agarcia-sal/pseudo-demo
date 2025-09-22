def calculate_modified_quantity(quantity, divisor):
    total_units = quantity // divisor  # Integer division to get total units
    remainder = quantity % divisor       # Modulus operation to get remainder
    if remainder > 0:
        return remainder * (total_units + 1)
    else:
        return quantity

# Read input values
quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

# Calculate two modified quantities
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result
final_result = modified_quantity_a * modified_quantity_b

# Output the final value
print(final_result)
