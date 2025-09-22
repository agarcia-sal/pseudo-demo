def mc(n, s):
    """Calculate a modified count based on n and full groups of size s."""
    q, r = divmod(n, s)  # Get the quotient and remainder

    if r > 0:
        return r * (q + 1)  # Return leftover multiplied by (q + 1)
    else:
        return n  # Return n if there's no remainder

def main():
    # Read the input values for n, m, and s
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate and output the product of the results from mc for both n and m
    result = mc(n, s) * mc(m, s)
    print(result)

if __name__ == "__main__":
    main()
