def calculate_remainder_division(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor  # Integer division to get the quotient
    remainder = number % divisor   # Modulus operation to get the remainder
    
    # Check if there is a remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Return product of remainder and (quotient + 1)
    else:
        return number  # Return the original number if there's no remainder

# Read input values from the user
n = int(input())  # Input for n
m = int(input())  # Input for m
s = int(input())  # Input for s

# Calculate results using the function
result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

# Final result is the product of the two results obtained
final_result = result_from_n * result_from_m

# Print the final result
print(final_result)
