def calculate_remainder(n, s):
    # Divide n by s to get quotient (q) and remainder (r)
    q, r = divmod(n, s)  # divmod returns both quotient and remainder
    # If remainder r is greater than 0, return (r * (q + 1))
    # Otherwise, return n
    if r > 0:
        return r * (q + 1)
    else:
        return n

def main():
    # Read a line of input and convert it into three integers n, m, and s
    n, m, s = map(int, input().split())
    # Calculate the product of calculate_remainder(n, s) and calculate_remainder(m, s)
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    # Output the result
    print(result)

# Call the main function to execute the program
main()
