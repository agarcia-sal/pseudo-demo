def calculate_remainder_sum(dividend, divisor):
    """
    Calculate the modified sum based on the remainder after division.
    
    If there is a remainder, return the product of remainder and (quotient + 1).
    If there's no remainder, return the original dividend.
    """
    quotient, remainder = divmod(dividend, divisor)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate the modified sum for n and m using the calculate_remainder_sum function
result_n = calculate_remainder_sum(n, s)
result_m = calculate_remainder_sum(m, s)

# Output the product of the two results
print(result_n * result_m)
