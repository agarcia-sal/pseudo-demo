def calculate_remainder_sum(dividend, divisor):
    # Calculate quotient and remainder by integer division and modulo
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, return the product of remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If no remainder, return the original dividend

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate the modified sum for n and m using the calculate_remainder_sum function
result_n = calculate_remainder_sum(n, s)
result_m = calculate_remainder_sum(m, s)

# Output the product of the two results
print(result_n * result_m)
