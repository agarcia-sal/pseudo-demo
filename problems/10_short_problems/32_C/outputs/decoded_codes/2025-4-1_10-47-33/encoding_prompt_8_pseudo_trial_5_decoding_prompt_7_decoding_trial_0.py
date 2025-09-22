def calculate_modified_value(total, divisor):
    # Calculate the quotient and remainder when total is divided by divisor
    quotient = total // divisor
    remainder = total % divisor
    
    # If there is a remainder, modify the total according to specified rules
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total  # Return the original total if there is no remainder

# Main Program
# Read three integer values from input
n = int(input())
m = int(input())
s = int(input())

# Calculate modified values based on the function
modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)

# Calculate the final result as the product of the modified values
final_result = modified_n * modified_m

# Print the final result
print(final_result)
