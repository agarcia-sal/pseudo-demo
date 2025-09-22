def calculate_modified_value(total, divisor):
    # Calculate quotient and remainder when total is divided by divisor
    quotient = total // divisor
    remainder = total % divisor
    
    # If there is a remainder, return modified total
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Main program
# Read three integer values from input
n = int(input())
m = int(input())
s = int(input())

# Calculate modified values for n and m using the divisor s
modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)

# Calculate the final result as the product of modified_n and modified_m
final_result = modified_n * modified_m

# Print the final result
print(final_result)
