def calculate_adjusted_product(quantity, size_limit):
    # Calculate the number of complete sets and the remainder
    number_of_complete_sets, remainder = divmod(quantity, size_limit)

    # Adjust the original quantity based on the remainder
    if remainder > 0:
        adjusted_quantity = remainder * (number_of_complete_sets + 1)
    else:
        adjusted_quantity = quantity

    return adjusted_quantity

def main():
    # Read input for two quantities and the size limit
    number1 = int(input())
    number2 = int(input())
    limit = int(input())

    # Calculate the adjusted quantities using the adjustment function
    adjusted_product1 = calculate_adjusted_product(number1, limit)
    adjusted_product2 = calculate_adjusted_product(number2, limit)

    # Compute the final product of the adjusted quantities
    result = adjusted_product1 * adjusted_product2

    # Print the computed result
    print(result)

# Call the main function to execute the program
main()
