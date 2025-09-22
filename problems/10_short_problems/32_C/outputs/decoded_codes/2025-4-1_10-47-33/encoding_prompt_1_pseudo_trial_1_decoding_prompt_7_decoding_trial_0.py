def calculate_remainder_division(number, divisor):
    # Calculate the quotient and remainder when dividing the number by the divisor
    quotient = number // divisor  # Integer division to get the quotient
    remainder = number % divisor   # Modulus to get the remainder

    # If there is a remainder, return remainder multiplied by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # If no remainder, simply return the number

# Read input values from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the division function for both n and m
result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

# Calculate the final result by multiplying both results
final_result = result_from_n * result_from_m

# Print the final result
print(final_result)
