def calculate_adjusted_product(quantity, size_limit):
    # Calculate how many complete sets fit into quantity and the remainder
    number_of_complete_sets, remainder = divmod(quantity, size_limit)

    # Adjust quantity to account for any overflow
    if remainder > 0:
        adjusted_quantity = remainder * (number_of_complete_sets + 1)
    else:
        adjusted_quantity = quantity

    return adjusted_quantity  # Return the adjusted value of quantity

def main():
    # Capture user input for quantities and size limit
    number1 = int(input())
    number2 = int(input())
    size_limit = int(input())

    # Use the calculate_adjusted_product function to adjust both quantities
    adjusted_product1 = calculate_adjusted_product(number1, size_limit)
    adjusted_product2 = calculate_adjusted_product(number2, size_limit)

    # Compute the product of the adjusted quantities
    result = adjusted_product1 * adjusted_product2

    # Display the result 
    print(result)

# Call main
main()
