def calculate_modified_quantity(quantity, divisor):
    total_units = quantity // divisor  # Calculate number of complete groups
    remainder = quantity % divisor      # Calculate leftover part

    if remainder > 0:
        return remainder * (total_units + 1)  # Return modified quantity if remainder exists
    else:
        return quantity  # Return original quantity if no remainder

# Read input values
quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

# Calculate modified quantities using the defined function
modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

# Calculate the final result
final_result = modified_quantity_a * modified_quantity_b

# Output the final value
print(final_result)
