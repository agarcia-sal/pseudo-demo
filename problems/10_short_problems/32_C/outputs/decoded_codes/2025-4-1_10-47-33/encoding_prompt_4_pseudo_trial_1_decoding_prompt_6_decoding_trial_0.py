def calculate_result(n, m, s):
    # Compute the adjusted value for n based on s
    adjusted_n = compute_adjusted_value(n, s)
    
    # Compute the adjusted value for m based on s
    adjusted_m = compute_adjusted_value(m, s)
    
    # Calculate the final result by multiplying the adjusted values
    return adjusted_n * adjusted_m

def compute_adjusted_value(value, segment_size):
    # Divide value into segments and get the quotient and remainder
    quotient = value // segment_size
    remainder = value % segment_size
    
    # If there is a remainder, adjust the value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

# Input: Read three integers from standard input (n, m, and s)
n = int(input())
m = int(input())
s = int(input())

# Output: Print the result of the calculation
result = calculate_result(n, m, s)
print(result)
