def calculateRemainderBonus(number, stepSize):
    # Calculate how many full groups of stepSize fit into number
    fullGroups = number // stepSize
    
    # Calculate the remainder when number is divided by stepSize
    remainder = number % stepSize
    
    # If remainder is greater than 0, return product of remainder and (fullGroups + 1)
    if remainder > 0:
        return remainder * (fullGroups + 1)
    # Otherwise, return number itself
    else:
        return number

# Input Handling
input_line = input()  # Read a single line of input
firstNumber, secondNumber, stepSize = map(int, input_line.split())  # Split input into three integers

# Output Calculation
firstResult = calculateRemainderBonus(firstNumber, stepSize)  # Calculate result for firstNumber
secondResult = calculateRemainderBonus(secondNumber, stepSize)  # Calculate result for secondNumber

# Multiply the results and print the final result
final_result = firstResult * secondResult
print(final_result)
