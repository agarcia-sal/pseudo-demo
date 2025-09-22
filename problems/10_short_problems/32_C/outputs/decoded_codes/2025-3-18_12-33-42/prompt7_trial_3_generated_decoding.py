def calculateRemainderAndMultiply(number1, divisor):
    # Calculate quotient and remainder
    quotient = number1 // divisor
    remainder = number1 % divisor
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number1  # If no remainder, just return number1

def main():
    # Read three integers from input
    totalItems1 = int(input())
    totalItems2 = int(input())
    divisor = int(input())

    # Call the function to calculate adjusted values
    result1 = calculateRemainderAndMultiply(totalItems1, divisor)
    result2 = calculateRemainderAndMultiply(totalItems2, divisor)

    # Print the product of the two adjusted results
    print(result1 * result2)

# Execute the main function
if __name__ == "__main__":
    main()
