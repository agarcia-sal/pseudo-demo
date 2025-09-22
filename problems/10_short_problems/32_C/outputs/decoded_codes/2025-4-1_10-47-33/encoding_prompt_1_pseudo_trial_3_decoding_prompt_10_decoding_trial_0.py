def calculate_remainder_and_adjustment(number, divisor):
    """Calculate the remainder and adjust the quotient accordingly."""
    quotient, remainder = divmod(number, divisor)  # divmod returns quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number


# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the results for n and m with divisor s
result_a = calculate_remainder_and_adjustment(n, s)
result_b = calculate_remainder_and_adjustment(m, s)

# Final result is the product of the two results
final_result = result_a * result_b

# Print the final result
print(final_result)
