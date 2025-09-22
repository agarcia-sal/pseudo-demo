def calculate_remainder_division(number, divisor):
    # Calculate quotient and remainder using integer division and modulus
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder, return the modified result
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values n, m, and s from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the calculation function
result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

# Calculate the final result
final_result = result_from_n * result_from_m

# Print the final result
print(final_result)
