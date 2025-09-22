def calculate_remainder(n, s):
    # Divide n by s using integer division to get quotient q and remainder r
    q, r = divmod(n, s)  # divmod gives us both the quotient and remainder
    
    # If the remainder r is greater than 0
    if r > 0:
        return r * (q + 1)  # Return the adjusted remainder product with quotient
    else:
        return n  # If r is 0, return n

def main():
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate the product of modified remainders from both n and m
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Output the result
    print(result)

# Call the main function to execute the program
main()
