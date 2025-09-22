def adjust_quantity(quantity, divisor):
    # Calculate how many full groups can be made from the quantity
    full_groups = quantity // divisor
    remainder = quantity % divisor
    
    # If there is a remainder, adjust the quantity
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return quantity  # No adjustment needed

# Main program execution
input_line = input()  # Read input
n, m, s = map(int, input_line.split())  # Convert input to integers

# Adjust quantities based on the divisor
adjusted_n = adjust_quantity(n, s)
adjusted_m = adjust_quantity(m, s)

# Calculate the product of the adjusted quantities
result = adjusted_n * adjusted_m

# Print the resulting product
print(result)
