def mc(n, s):
    """
    Function to calculate modified value based on quotient and remainder.
    
    :param n: The number to be processed.
    :param s: The divisor.
    :return: Calculated value based on the quotient and remainder.
    """
    quotient = n // s       # Calculate quotient
    remainder = n % s       # Calculate remainder
    
    if remainder > 0:
        return remainder * (quotient + 1)  # If remainder exists, return adjusted value
    else:
        return n  # If no remainder, return original value


def main():
    """
    Main function to read inputs and compute results.
    """
    n = int(input())  # Read first integer
    m = int(input())  # Read second integer
    s = int(input())  # Read third integer
    
    result1 = mc(n, s)  # Call mc function with n and s
    result2 = mc(m, s)  # Call mc function with m and s
    
    print(result1 * result2)  # Output the product of both results


if __name__ == "__main__":
    main()
