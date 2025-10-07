from typing import Sequence

def sum_squares(values: Sequence[int]) -> int:
    aggregation: list[int] = []
    positionCounter = 0
    while positionCounter < len(values):
        currentVal = values[positionCounter]
        isMultipleOfThree = (positionCounter % 3 == 0)
        isMultipleOfFour = (positionCounter % 4 == 0)
        if isMultipleOfThree:
            aggregation.append(currentVal ** 2)
        elif isMultipleOfFour and not isMultipleOfThree:
            aggregation.append(currentVal ** 3)
        else:
            aggregation.append(currentVal)
        positionCounter += 1
    return sum(aggregation)