def calculate_remainder_sum(dividend, divisor):
    # Divide the dividend by divisor using integer division and modulus to get the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # If there is a remainder, return the product of remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original dividend
        return dividend

# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the modified sum for n and m using the calculate_remainder_sum function
result_n = calculate_remainder_sum(n, s)
result_m = calculate_remainder_sum(m, s)

# Output the product of the two results
print(result_n * result_m)
