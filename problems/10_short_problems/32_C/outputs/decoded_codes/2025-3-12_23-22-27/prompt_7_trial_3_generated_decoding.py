def calculate_remainder(n, s):
    # Calculate the quotient and the remainder of n divided by s
    q = n // s  # Integer division to get the quotient
    r = n % s   # Modulus operation to get the remainder

    # If the remainder r is greater than 0, return r multiplied by (q + 1)
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If remainder is 0, return n as specified

def main():
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate the product of calculate_remainder(n, s) and calculate_remainder(m, s)
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Output the result
    print(result)

# Call the main function to execute the program
main()
