def calculate_modified_value(total, divisor):
    # Calculate quotient and remainder of the division
    quotient, remainder = divmod(total, divisor)
    
    # If there is a remainder, modify the total based on it
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Main program execution
# Read three integer values from input
n = int(input())
m = int(input())
s = int(input())

# Calculate modified values
modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)

# Calculate the final result as the product of modified_n and modified_m
final_result = modified_n * modified_m

# Print the final result
print(final_result)
