def mc(n, s):
    """
    Calculate the modified value based on the division of n by s.
    
    Parameters:
    n (int): The numerator value.
    s (int): The denominator value.

    Returns:
    int: Returns the product of the remainder and the incremented quotient if there is a remainder,
         otherwise returns n.
    """
    # Calculate the quotient and remainder from dividing n by s
    quotient, remainder = divmod(n, s)
    # If there is a remainder, return the product of remainder and incremented quotient
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

def main():
    """
    Main function to read inputs and compute the final result.
    """
    # Read inputs for n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate and output the product of mc(n, s) and mc(m, s)
    result = mc(n, s) * mc(m, s)
    print(result)

if __name__ == "__main__":
    main()
