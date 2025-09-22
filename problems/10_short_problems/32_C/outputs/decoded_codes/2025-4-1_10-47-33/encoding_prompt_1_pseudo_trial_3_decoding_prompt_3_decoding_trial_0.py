def calculate_remainder_and_adjustment(number, divisor):
    # Calculate the quotient and remainder
    quotient, remainder = divmod(number, divisor)
    
    # Adjust value based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Call the function for both n and m
result_a = calculate_remainder_and_adjustment(n, s)
result_b = calculate_remainder_and_adjustment(m, s)

# Final result calculation
final_result = result_a * result_b

# Print the final result
print(final_result)
