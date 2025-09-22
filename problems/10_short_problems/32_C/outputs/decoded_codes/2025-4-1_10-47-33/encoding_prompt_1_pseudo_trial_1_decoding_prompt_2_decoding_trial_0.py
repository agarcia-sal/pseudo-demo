def calculate_remainder_division(number, divisor):
    quotient = number // divisor  # Integer division to get the quotient
    remainder = number % divisor   # Modulus operation to get the remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Return product if remainder exists
    else:
        return number  # Return the number if there is no remainder

# Read input values from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the defined function
result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

# Final result calculation
FINAL_RESULT = result_from_n * result_from_m

# Print the final result
print(FINAL_RESULT)
