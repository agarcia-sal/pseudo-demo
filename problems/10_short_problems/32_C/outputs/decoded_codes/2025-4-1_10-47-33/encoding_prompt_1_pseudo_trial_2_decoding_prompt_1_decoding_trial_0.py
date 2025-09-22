def calculateRemainderBonus(number, stepSize):
    fullGroups = number // stepSize
    remainder = number % stepSize
    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        return number

# Input handling
input_line = input()
firstNumber, secondNumber, stepSize = map(int, input_line.split())

# Output calculation
firstResult = calculateRemainderBonus(firstNumber, stepSize)
secondResult = calculateRemainderBonus(secondNumber, stepSize)
final_result = firstResult * secondResult

print(final_result)
