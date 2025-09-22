def calculateRemainderBonus(number, stepSize):
    fullGroups = number // stepSize
    remainder = number % stepSize

    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        return number

input_data = input()
firstNumber, secondNumber, stepSize = map(int, input_data.split())

firstResult = calculateRemainderBonus(firstNumber, stepSize)
secondResult = calculateRemainderBonus(secondNumber, stepSize)

final_result = firstResult * secondResult
print(final_result)
