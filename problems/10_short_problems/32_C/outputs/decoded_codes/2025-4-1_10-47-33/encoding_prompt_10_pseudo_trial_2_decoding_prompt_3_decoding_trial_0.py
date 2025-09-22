def mc(n, s):
    # Calculate quotient and remainder when n is divided by s
    q, r = divmod(n, s)  # divmod returns (quotient, remainder)
    
    # Check if there is a remainder
    if r > 0:
        return r * (q + 1)  # Return modified value if there's a remainder
    else:
        return n  # Return n if there's no remainder

# Main execution block
if __name__ == "__main__":
    # Read input from the user
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate the results using the mc function
    result1 = mc(n, s)
    result2 = mc(m, s)

    # Print the product of both results
    print(result1 * result2)
