def calculateAdjustedProduct(quantity1, quantity2, sizeLimit):
    # Calculate how many complete sets fit into quantity1 and the remainder
    numberOfCompleteSets1, remainder1 = divmod(quantity1, sizeLimit)

    # Adjust quantity to account for any overflow
    if remainder1 > 0:
        adjustedQuantity1 = remainder1 * (numberOfCompleteSets1 + 1)
    else:
        adjustedQuantity1 = quantity1  # If no overflow, keep original quantity

    return adjustedQuantity1  # Return the adjusted value of quantity1


def main():
    # Capture user input for quantities and size limit
    number1 = int(input())  # First quantity
    number2 = int(input())  # Second quantity
    limit = int(input())     # Size limit

    # Use the calculateAdjustedProduct function to adjust both quantities
    adjustedProduct1 = calculateAdjustedProduct(number1, limit)
    adjustedProduct2 = calculateAdjustedProduct(number2, limit)

    # Compute the product of the adjusted quantities
    result = adjustedProduct1 * adjustedProduct2

    # Display the result
    print(result)


# Call the main function to execute the program
main()
