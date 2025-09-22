def calculate_remainder_adjusted(total, size):
    # Divide 'total' by 'size' to get quotient and remainder
    quotient = total // size
    remainder = total % size
    
    # Check if remainder is greater than zero
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjusted value for leftover
    else:
        return total  # No adjustment needed

# Read a line of input and convert it into three integers
n, m, s = map(int, input().split())

# Calculate the adjusted values for 'n' and 'm' by calling the function
adjusted_value_n = calculate_remainder_adjusted(n, s)
adjusted_value_m = calculate_remainder_adjusted(m, s)

# Print the product of 'adjusted_value_n' and 'adjusted_value_m'
print(adjusted_value_n * adjusted_value_m)
