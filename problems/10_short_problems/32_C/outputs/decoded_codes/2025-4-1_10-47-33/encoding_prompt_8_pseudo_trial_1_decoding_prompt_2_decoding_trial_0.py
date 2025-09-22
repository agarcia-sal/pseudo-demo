def calculate_remainder_and_adjustment(number, divisor):
    # Calculate quotient and remainder when dividing number by divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder
    if remainder > 0:
        # Return the remainder multiplied by incremented quotient
        return remainder * (quotient + 1)
    
    # If no remainder, return the original number
    return number

# READ the input values for n, m, and s and convert them to integers
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values for n and m using the helper function
adjusted_value_for_n = calculate_remainder_and_adjustment(n, s)
adjusted_value_for_m = calculate_remainder_and_adjustment(m, s)

# Compute the final result by multiplying the adjusted values for n and m
final_result = adjusted_value_for_n * adjusted_value_for_m

# Print the final result
print(final_result)
