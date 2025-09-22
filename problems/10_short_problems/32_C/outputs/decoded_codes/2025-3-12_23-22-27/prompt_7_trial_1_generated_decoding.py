def calculate_remainder(n, s):
    # Calculate the quotient and remainder of n divided by s
    q, r = divmod(n, s)
    
    # If the remainder r is greater than 0, return r * (q + 1)
    # Otherwise, return n
    if r > 0:
        return r * (q + 1)
    else:
        return n

def main():
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    
    # Calculate the product of calculate_remainder of n and m with the divisor s
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Output the result
    print(result)

# Call the main function to execute the program
main()
