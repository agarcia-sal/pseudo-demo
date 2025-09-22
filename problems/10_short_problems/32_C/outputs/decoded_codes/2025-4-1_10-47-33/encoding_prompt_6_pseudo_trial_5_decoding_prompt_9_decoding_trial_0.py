def calculate_remainder_count(number, divisor):
    # Divide the number by the divisor to get quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If the remainder is greater than zero, compute the adjusted count
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate adjusted counts for both n and m based on s
adjusted_count_for_n = calculate_remainder_count(n, s)
adjusted_count_for_m = calculate_remainder_count(m, s)

# Compute the product of the adjusted counts for n and m
result = adjusted_count_for_n * adjusted_count_for_m

# Output the final result
print(result)
