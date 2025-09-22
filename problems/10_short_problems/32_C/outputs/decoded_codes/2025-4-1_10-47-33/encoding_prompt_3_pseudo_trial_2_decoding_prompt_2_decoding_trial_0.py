def CalculateRemainderCountAndMultiply(inputValue1, divisor):
    # Calculate the quotient and remainder when inputValue1 is divided by divisor
    quotient = inputValue1 // divisor
    remainder = inputValue1 % divisor
    
    # If there is a remainder, return the product of the remainder and the next quotient value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return inputValue1  # When there is no remainder, return inputValue1

# Start Main Program
# Read three integer inputs from user
inputValue1 = int(input())
inputValue2 = int(input())
divisor = int(input())

# Calculate the results for inputValue1 and inputValue2 using the defined function
result1 = CalculateRemainderCountAndMultiply(inputValue1, divisor)
result2 = CalculateRemainderCountAndMultiply(inputValue2, divisor)

# Multiply the results and output the final result
finalResult = result1 * result2
print(finalResult)
