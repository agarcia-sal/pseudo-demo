def calculate_remainder(n, s):
    # Divide n by s to get quotient q and remainder r
    q = n // s  # Using integer division to get the quotient
    r = n % s   # Using modulo operation to get the remainder
    
    # If the remainder r is greater than 0, return r times (q + 1)
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If r is not greater than 0, return n

def main():
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate the product of calculate_remainder(n, s) and calculate_remainder(m, s)
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Output the result
    print(result)

# Call the main function to execute the program
main()
