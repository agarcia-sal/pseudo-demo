def calculate_remainder_and_quotient(input_number, divisor):
    """
    Calculate the quotient and remainder when dividing input_number by divisor.
    
    If the remainder is greater than zero, return the product of the
    remainder and one more than the quotient. Otherwise, return the 
    original input_number.
    """
    quotient, remainder = divmod(input_number, divisor)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return input_number

# Read integers n, m, and s from user input
n = int(input())
m = int(input())
s = int(input())

# Call the function for n and s, and for m and s, and multiply the results
result = calculate_remainder_and_quotient(n, s) * calculate_remainder_and_quotient(m, s)

# Output the final result
print(result)
