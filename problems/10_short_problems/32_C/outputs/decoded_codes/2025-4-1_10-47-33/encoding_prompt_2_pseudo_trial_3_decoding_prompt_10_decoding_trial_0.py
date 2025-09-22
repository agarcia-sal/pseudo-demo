def mc(number, divisor):
    """
    Calculate a modified value based on the division of the number by the divisor.
    
    Parameters:
    number (int): The number to be processed.
    divisor (int): The divisor used for division.
    
    Returns:
    int: The processed value based on the condition of remainder.
    """
    quotient, remainder = divmod(number, divisor)  # Get quotient and remainder from division
    if remainder > 0:
        return remainder * (quotient + 1)  # If remainder is greater than 0, return modified value
    else:
        return number  # Return original number if remainder is 0

def main():
    """
    Main function to execute the program logic.
    """
    # Input section
    total1, total2, divisor = map(int, input().split())  # Read input and convert to integers
    
    # Processing section
    result1 = mc(total1, divisor)  # Process total1
    result2 = mc(total2, divisor)  # Process total2
    
    # Output section
    final_product = result1 * result2  # Calculate final product of results
    print(final_product)  # Print the final product

# Entry point of the program
if __name__ == "__main__":
    main()
