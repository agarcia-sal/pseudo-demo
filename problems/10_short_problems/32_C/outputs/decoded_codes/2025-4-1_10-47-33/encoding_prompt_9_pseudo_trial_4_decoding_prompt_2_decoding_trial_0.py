# Define Function for Group Calculation
def calculate_groups(total_items, group_size):
    quotient = total_items // group_size  # Divide totalItems by groupSize to find how many complete groups can be formed
    remainder = total_items % group_size   # Find the remainder of totalItems divided by groupSize
    if remainder != 0:                     # If there is a remainder
        return remainder * (quotient + 1)  # Return remainder multiplied by (quotient + 1)
    else:
        return total_items                  # Otherwise, return totalItems

# Input Data
totalA = int(input())  # Read first integer for n
totalB = int(input())  # Read second integer for m
group_size = int(input())  # Read third integer for s

# Compute Group Values
valueA = calculate_groups(totalA, group_size)  # Calculate value for totalA
valueB = calculate_groups(totalB, group_size)  # Calculate value for totalB

# Calculate and Print Result
result = valueA * valueB  # Multiply the values obtained from totalA and totalB
print(result)  # Output the resulting product
