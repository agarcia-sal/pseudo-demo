def calculate_remainder_division(number, divisor):
    # Calculate the quotient and remainder using integer division and modulo
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder, return the product of the remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # If no remainder, return the original number

# Read input values from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate results for n and m using the calculate_remainder_division function
result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

# Calculate the final result by multiplying both results
final_result = result_from_n * result_from_m

# Print the final result
print(final_result)
