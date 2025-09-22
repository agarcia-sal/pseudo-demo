# Function to calculate adjusted values based on group size
def calculate_remainder_and_groups(number, group_size):
    full_groups = number // group_size  # Integer division to find full groups
    remainder = number % group_size       # Calculate the remainder
    
    # If there is any remainder, adjust the count of groups
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return number

# Read input values for n (first number), m (second number), and s (group size)
n = int(input())  # Read the first number and convert to integer
m = int(input())  # Read the second number and convert to integer
s = int(input())  # Read the group size and convert to integer

# Calculate the adjusted values for both n and m based on the group size
first_adjusted_value = calculate_remainder_and_groups(n, s)
second_adjusted_value = calculate_remainder_and_groups(m, s)

# Print the product of the two adjusted values
print(first_adjusted_value * second_adjusted_value)
