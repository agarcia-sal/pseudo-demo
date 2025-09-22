def calculateRemainderBonus(number, stepSize):
    fullGroups = number // stepSize  # Calculate how many full groups fit into number
    remainder = number % stepSize     # Calculate the remainder
    if remainder > 0:                 # Check if remainder is greater than 0
        return remainder * (fullGroups + 1)  # Return the bonus
    else:
        return number                 # Return number itself if remainder is 0

# Input Handling
input_data = input()  # Read a single line of input
firstNumber, secondNumber, stepSize = map(int, input_data.split())  # Split and convert to integers

# Output Calculation
firstResult = calculateRemainderBonus(firstNumber, stepSize)  # Call function for firstNumber
secondResult = calculateRemainderBonus(secondNumber, stepSize)  # Call function for secondNumber
finalResult = firstResult * secondResult  # Multiply the results
print(finalResult)  # Output the final result
