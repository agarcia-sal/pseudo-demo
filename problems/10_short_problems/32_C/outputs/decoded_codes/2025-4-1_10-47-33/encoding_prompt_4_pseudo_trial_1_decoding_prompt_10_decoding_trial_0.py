def calculate_result(n, m, s):
    """
    Compute the final result based on adjusted values of n and m.
    
    Parameters:
    n (int): The first number
    m (int): The second number
    s (int): The segment size for adjustment
    
    Returns:
    int: The computed product of the adjusted values
    """
    adjusted_n = compute_adjusted_value(n, s)
    adjusted_m = compute_adjusted_value(m, s)
    
    return adjusted_n * adjusted_m

def compute_adjusted_value(value, segment_size):
    """
    Adjusts the given value based on the segment size.
    
    Parameters:
    value (int): The numeric value to adjust
    segment_size (int): The segment size for adjustment
    
    Returns:
    int: The adjusted value
    """
    quotient, remainder = divmod(value, segment_size)  # Use divmod to get both quotient and remainder in one step

    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

def main():
    # Input: Read three integers
    n = int(input())
    m = int(input())
    s = int(input())

    # Output: Print the result of the calculation
    print(calculate_result(n, m, s))

if __name__ == "__main__":
    main()
