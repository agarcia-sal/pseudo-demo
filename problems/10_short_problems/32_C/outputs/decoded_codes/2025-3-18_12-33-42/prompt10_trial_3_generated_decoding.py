def mc(n, s):
    """Calculate a value based on the division and modulus of n by s."""
    q = n // s  # Calculate quotient of n divided by s
    r = n % s   # Calculate remainder of n divided by s

    if r > 0:
        return r * (q + 1)  # Calculate and return the modified value if remainder is greater than 0
    else:
        return n  # Return n if there is no remainder

def main():
    """Main function to read inputs and print the product of mc results."""
    # Read input values for n, m, and s
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate the results of mc for n and m
    result1 = mc(n, s)
    result2 = mc(m, s)

    # Print the product of the two results
    print(result1 * result2)

if __name__ == "__main__":
    main()
