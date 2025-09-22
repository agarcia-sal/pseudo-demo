def calculate_remainder_and_adjust_count(dividend, divisor):
    # Calculate the quotient and remainder when dividend is divided by divisor
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, adjust the count
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If no remainder, return the original dividend

# Read inputs for the first value (n), second value (m), and divisor value (s)
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted counts for n and m using the function
adjusted_count_for_n = calculate_remainder_and_adjust_count(n, s)
adjusted_count_for_m = calculate_remainder_and_adjust_count(m, s)

# Calculate and print the product of adjusted counts for n and m
print(adjusted_count_for_n * adjusted_count_for_m)
