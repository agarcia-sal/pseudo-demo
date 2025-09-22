def mc(n, s):
    """
    Calculate the result based on the given number n and divisor s.
    
    :param n: The number to be divided
    :param s: The divisor
    :return: The calculated result based on quotient and remainder
    """
    quotient = n // s  # Calculate the quotient
    remainder = n % s  # Calculate the remainder

    if remainder > 0:
        return remainder * (quotient + 1)  # Return product if remainder is positive
    else:
        return n  # Return n if remainder is zero

def main():
    # Read input and split into three integers
    n, m, s = map(int, input().split())

    # Calculate the result using the mc function
    result = mc(n, s) * mc(m, s)

    # Print the final result
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()


Input:
10 5 3

Output:
15
