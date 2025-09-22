def calculate_adjusted_groups(value, group_size):
    # Divide value into groups of the specified size
    quotient = value // group_size  # Integer division to get the number of full groups
    remainder = value % group_size  # Calculate remainder
    
    # If there's a remainder, include one extra group for it
    if remainder > 0:
        return remainder * (quotient + 1)  
    else:
        return value  # If there's no remainder, return the original value

# Read input values for n, m, and s from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted group values for n and m
adjusted_n = calculate_adjusted_groups(n, s)
adjusted_m = calculate_adjusted_groups(m, s)

# Calculate the product of the two adjusted values
product = adjusted_n * adjusted_m

# Output the result of the product
print(product)
