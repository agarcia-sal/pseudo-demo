def calculate_remainder(total, divisor):
    # Calculate the quotient and the remainder
    quotient = total // divisor  # Using floor division to get the quotient
    remainder = total % divisor   # Using modulo to get the remainder
    
    # If there is a remainder, return it multiplied by one more than the quotient
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total  # If no remainder, return the original total

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the results based on the function we defined
result_for_n = calculate_remainder(n, s)
result_for_m = calculate_remainder(m, s)

# Multiply the results and print the final output
final_result = result_for_n * result_for_m
print(final_result)
