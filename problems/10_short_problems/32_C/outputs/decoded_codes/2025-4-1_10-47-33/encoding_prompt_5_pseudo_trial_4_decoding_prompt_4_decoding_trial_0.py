def calculate_adjusted_product(quantity, size_limit):
    """
    Calculate the adjusted product of a given quantity based on the size limit.
    
    Parameters:
    quantity (int): The quantity to adjust.
    size_limit (int): The limit for dividing the quantity.
    
    Returns:
    int: The adjusted quantity based on the size limit.
    """
    number_of_complete_sets, remainder = divmod(quantity, size_limit)
    # Calculate how many complete sets fit into quantity and the remainder.

    if remainder > 0:
        adjusted_quantity = remainder * (number_of_complete_sets + 1)
        # Adjust quantity to account for any overflow.
    else:
        adjusted_quantity = quantity
        # If no overflow, keep the original quantity.

    return adjusted_quantity  # Return the adjusted value of quantity.

def main():
    """
    Main function to read input values, calculate adjusted products, and print the result.
    """
    number1 = int(input())
    number2 = int(input())
    limit = int(input())
    # Capture user input for quantities and size limit.

    adjusted_product1 = calculate_adjusted_product(number1, limit)
    adjusted_product2 = calculate_adjusted_product(number2, limit)
    # Use the calculate_adjusted_product function to adjust both quantities.

    result = adjusted_product1 * adjusted_product2
    # Compute the product of the adjusted quantities.

    print(result)  # Display the result.

# Start the program by calling main function.
main()
