def calculateRemainderBonus(number, stepSize):
    """
    Calculate the remainder bonus based on the given number and step size.
    
    Parameters:
    - number (int): The number to evaluate.
    - stepSize (int): The size of each step for grouping.
    
    Returns:
    - int: The calculated bonus or the number itself based on the remainder.
    """
    # Calculate the number of full groups of stepSize that fit into number
    fullGroups = number // stepSize
    # Calculate the remainder when number is divided by stepSize
    remainder = number % stepSize
    
    # Return the product of the remainder and (fullGroups + 1) if remainder is greater than 0
    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        return number

# Input handling
input_line = input()  # Read a single line of input
firstNumber, secondNumber, stepSize = map(int, input_line.split())

# Output calculation
firstResult = calculateRemainderBonus(firstNumber, stepSize)
secondResult = calculateRemainderBonus(secondNumber, stepSize)

# Print the final multiplied result
final_result = firstResult * secondResult
print(final_result)
