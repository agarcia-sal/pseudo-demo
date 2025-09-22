def calculate_modified_value(total, divisor):
    """
    Calculate a modified value based on the total and divisor.
    
    If there is a remainder from the division, return the product of the 
    remainder and one more than the quotient. If there is no remainder, 
    return the original total.
    
    Args:
    total (int): The number to be modified.
    divisor (int): The number by which to divide the total.
    
    Returns:
    int: The modified value.
    """
    quotient, remainder = divmod(total, divisor)  # divmod gives both quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

def main():
    """
    Main program to read input values and compute the product
    of modified values based on the given operations.
    """
    n = int(input())  # Read first integer
    m = int(input())  # Read second integer
    s = int(input())  # Read third integer

    modified_n = calculate_modified_value(n, s)  # Modify n based on s
    modified_m = calculate_modified_value(m, s)  # Modify m based on s

    final_result = modified_n * modified_m  # Calculate the final product
    print(final_result)  # Output the result

if __name__ == "__main__":
    main()  # Execute the main program


   10
   20
   3
   