def calculate_remainder_and_adjustment(number, divisor):
    # Calculate the quotient and remainder of the number divided by the divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # If the remainder is greater than 0, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If remainder is 0, return the original number
        return number

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the defined function
result_a = calculate_remainder_and_adjustment(n, s)
result_b = calculate_remainder_and_adjustment(m, s)

# Calculate the final result by multiplying the two results
final_result = result_a * result_b

# Print the final result
print(final_result)
