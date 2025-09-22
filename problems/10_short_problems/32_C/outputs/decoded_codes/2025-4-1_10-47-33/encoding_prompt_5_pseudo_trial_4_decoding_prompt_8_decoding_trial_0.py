def calculateAdjustedProduct(quantity1, sizeLimit):
    numberOfCompleteSets1, remainder1 = divmod(quantity1, sizeLimit)
    # Calculate how many complete sets fit into quantity1 and the remainder

    if remainder1 > 0:
        adjustedQuantity1 = remainder1 * (numberOfCompleteSets1 + 1)
    else:
        adjustedQuantity1 = quantity1
    # Return the adjusted value of quantity1

    return adjustedQuantity1

def main():
    number1 = int(input())
    number2 = int(input())
    limit = int(input())
    # Capture user input for quantities and size limit
    
    adjustedProduct1 = calculateAdjustedProduct(number1, limit)
    adjustedProduct2 = calculateAdjustedProduct(number2, limit)
    # Use the calculateAdjustedProduct function to adjust both quantities

    result = adjustedProduct1 * adjustedProduct2
    # Compute the product of the adjusted quantities

    print(result)
    # Display the result 

if __name__ == "__main__":
    main()
