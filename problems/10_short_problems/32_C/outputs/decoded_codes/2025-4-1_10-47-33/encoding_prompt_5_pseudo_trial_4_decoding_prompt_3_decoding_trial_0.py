def calculate_adjusted_product(quantity1, quantity2, size_limit):
    # Calculate how many complete sets can fit into quantity1 and the remainder
    number_of_complete_sets1, remainder1 = divmod(quantity1, size_limit)

    # Adjust quantity to account for any overflow
    if remainder1 > 0:
        adjusted_quantity1 = remainder1 * (number_of_complete_sets1 + 1)
    else:
        adjusted_quantity1 = quantity1  # No overflow, keep original quantity

    return adjusted_quantity1  # Return the adjusted value of quantity1

def main():
    # Capture user input for quantities and size limit
    number1 = int(input())
    number2 = int(input())
    limit = int(input())
    
    # Use the calculate_adjusted_product function to adjust both quantities
    adjusted_product1 = calculate_adjusted_product(number1, limit)
    adjusted_product2 = calculate_adjusted_product(number2, limit)

    # Compute the product of the adjusted quantities
    result = adjusted_product1 * adjusted_product2
    
    # Display the result
    print(result)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
