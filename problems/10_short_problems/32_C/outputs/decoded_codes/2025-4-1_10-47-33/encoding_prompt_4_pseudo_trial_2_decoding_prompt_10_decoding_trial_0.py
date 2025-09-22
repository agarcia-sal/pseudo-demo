def mc(number, size):
    """
    Calculate an adjusted value based on the division of number by size.
    
    If there is a remainder when dividing the number by size, 
    the function returns the remainder multiplied by (quotient + 1).
    Otherwise, it returns the original number.

    Parameters:
    number (int): The number to be adjusted.
    size (int): The size used for the division.

    Returns:
    int: The adjusted value.
    """
    quotient = number // size
    remainder = number % size

    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number  # Return the original number if no remainder


def main():
    """
    Main function to read input values and calculate the product of adjusted values.
    
    It reads three integer values from user input and computes 
    the product of adjusted values for the first two inputs.
    """
    # Read input values for n, m, and s
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate and print the product of adjusted values for n and m
    result = mc(n, s) * mc(m, s)
    print(result)

if __name__ == "__main__":
    main()
