def calculateAdjustedProduct(quantity1, sizeLimit):
    numberOfCompleteSets1 = quantity1 // sizeLimit  # Calculate complete sets
    remainder1 = quantity1 % sizeLimit  # Calculate the remainder

    if remainder1 > 0:
        adjustedQuantity1 = remainder1 * (numberOfCompleteSets1 + 1)  # Adjust for overflow
    else:
        adjustedQuantity1 = quantity1  # No adjustment needed if no overflow

    return adjustedQuantity1  # Return adjusted quantity

def main():
    number1 = int(input())  # Read the first quantity
    number2 = int(input())  # Read the second quantity
    limit = int(input())  # Read the size limit

    adjustedProduct1 = calculateAdjustedProduct(number1, limit)  # Adjust the first quantity
    adjustedProduct2 = calculateAdjustedProduct(number2, limit)  # Adjust the second quantity

    result = adjustedProduct1 * adjustedProduct2  # Calculate product of adjusted quantities

    print(result)  # Print the final result

main()  # Call the main function
