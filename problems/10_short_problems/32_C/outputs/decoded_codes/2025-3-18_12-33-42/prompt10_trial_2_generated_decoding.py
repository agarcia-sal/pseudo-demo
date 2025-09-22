def mc(n, s):
    """
    Calculate a modified value based on the integer division of n by s.

    Parameters:
    n (int): The first number.
    s (int): The second number (must not be zero).

    Returns:
    int: Modified value based on the division or the original n if conditions are not met.
    """
    if s == 0:
        raise ValueError("s must not be zero.")
    
    # Integer division and remainder
    q = n // s
    r = n % s
    
    if r > 0:
        return r * (q + 1)
    else:
        return n


def main():
    # Read input values from the user
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate results using mc function
    result1 = mc(n, s)
    result2 = mc(m, s)

    # Print the product of the two results
    print(result1 * result2)


# Execute the main program
if __name__ == "__main__":
    main()
