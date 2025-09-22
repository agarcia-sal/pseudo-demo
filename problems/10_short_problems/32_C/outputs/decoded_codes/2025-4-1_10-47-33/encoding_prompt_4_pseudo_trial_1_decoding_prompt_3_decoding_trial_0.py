def calculate_result(n, m, s):
    """
    Compute the product of adjusted values of n and m based on segment size s.

    Parameters:
    n (int): First integer to adjust
    m (int): Second integer to adjust
    s (int): Segment size for adjustment

    Returns:
    int: The product of the adjusted values
    """
    adjusted_n = compute_adjusted_value(n, s)
    adjusted_m = compute_adjusted_value(m, s)
    
    return adjusted_n * adjusted_m

def compute_adjusted_value(value, segment_size):
    """
    Adjust the input value based on the segment size.

    The adjustment is based on the quotient and remainder of the division of
    value by segment_size. If there is a remainder, it multiplies the
    remainder by the next integer.

    Parameters:
    value (int): The value to adjust
    segment_size (int): The size of each segment

    Returns:
    int: The adjusted value
    """
    quotient, remainder = divmod(value, segment_size)

    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

# Input: Read three integers from standard input (n, m, and s)
n = int(input())
m = int(input())
s = int(input())

# Output: Print the result of the calculation
print(calculate_result(n, m, s))
