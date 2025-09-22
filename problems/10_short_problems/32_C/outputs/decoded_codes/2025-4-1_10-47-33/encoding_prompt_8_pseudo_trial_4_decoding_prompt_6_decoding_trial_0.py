def adjust_quantity(quantity, divisor):
    # Calculate how many full groups can be formed
    full_groups = quantity // divisor
    remainder = quantity % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        # Return the adjusted quantity based on the remainder and full groups
        return remainder * (full_groups + 1)
    else:
        # No adjustment needed, return the original quantity
        return quantity

# Main program execution
input_line = input()  # Read a single line of input
n, m, s = map(int, input_line.split())  # Convert input into integers

# Get adjusted quantities
adjusted_n = adjust_quantity(n, s)
adjusted_m = adjust_quantity(m, s)

# Calculate the product of the adjusted quantities
result = adjusted_n * adjusted_m

# Output the result
print(result)
