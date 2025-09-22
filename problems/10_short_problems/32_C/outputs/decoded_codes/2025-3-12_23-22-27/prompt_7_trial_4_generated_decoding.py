def calculate_remainder(n, s):
    """
    Calculate the modified remainder of n divided by s.
    
    If the remainder r of n divided by s is greater than 0, return r * (q + 1),
    where q is the quotient of n divided by s. Otherwise, return n.
    """
    q, r = divmod(n, s)  # Get quotient and remainder
    if r > 0:  # Check if remainder is greater than 0
        return r * (q + 1)
    else:
        return n  # Return n if remainder is not greater than 0


def main():
    """
    Read input values, compute result using calculate_remainder,
    and print the final output.
    """
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate the product of calculate_remainder(n, s) and calculate_remainder(m, s)
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Output the result
    print(result)


# Call the main function to execute the program
main()
