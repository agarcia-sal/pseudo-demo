def calculate_remainder_sum(dividend, divisor):
    """
    Calculate the modified sum based on the remainder of division.
    
    Parameters:
        dividend (int): The number to be divided.
        divisor (int): The number by which to divide the dividend.
        
    Returns:
        int: The product of remainder and (quotient + 1) if there is a remainder,
             or the original dividend if there is no remainder.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    # Read input values
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate the modified sum for n and m using the calculate_remainder_sum function
    result_n = calculate_remainder_sum(n, s)
    result_m = calculate_remainder_sum(m, s)

    # Output the product of the two results
    print(result_n * result_m)

if __name__ == "__main__":
    main()
