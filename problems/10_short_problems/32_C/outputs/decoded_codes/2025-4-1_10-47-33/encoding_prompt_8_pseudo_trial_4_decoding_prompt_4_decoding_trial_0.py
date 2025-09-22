def adjust_quantity(quantity, divisor):
    """Adjust the quantity based on the number of full groups defined by the divisor."""
    # Calculate how many full groups can be made
    full_groups = quantity // divisor
    remainder = quantity % divisor
    
    # If there is a remainder, adjust the quantity accordingly
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

# Calculate and print the product of the adjusted quantities
result = adjusted_n * adjusted_m
print(result)
