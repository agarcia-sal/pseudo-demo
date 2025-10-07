from typing import List

def minPath(matrix: List[List[int]], parameter: int) -> List[int]:
    numeral: int = len(matrix)
    threshold: int = (numeral * numeral) + 1

    counter: int = 0
    while counter < numeral:
        pivot: int = 0
        while pivot < numeral:
            valueCheck: int = matrix[counter][pivot]
            if valueCheck == 1:
                adjacentValues: List[int] = []

                if counter != 0:
                    previousRowVal: int = matrix[counter - 1][pivot]
                    adjacentValues.append(previousRowVal)

                if pivot != 0:
                    leftColVal: int = matrix[counter][pivot - 1]
                    adjacentValues.append(leftColVal)

                limitRow: int = numeral - 1
                if counter != limitRow:
                    nextRowVal: int = matrix[counter + 1][pivot]
                    adjacentValues.append(nextRowVal)

                limitCol: int = numeral - 1
                if pivot != limitCol:
                    nextColVal: int = matrix[counter][pivot + 1]
                    adjacentValues.append(nextColVal)

                # Find the minimum adjacent value
                minVal: int = adjacentValues[0]
                indexer: int = 1
                while indexer < len(adjacentValues):
                    currentComparand: int = adjacentValues[indexer]
                    if currentComparand < minVal:
                        minVal = currentComparand
                    indexer += 1

                threshold = minVal
            pivot += 1
        counter += 1

    resultSequence: List[int] = []
    positionCounter: int = 0
    while True:
        exitEarly: bool = (positionCounter == parameter)
        if exitEarly:
            break

        remainderValue: int = positionCounter % 2
        if remainderValue == 0:
            resultSequence.append(1)
        else:
            resultSequence.append(threshold)

        positionCounter += 1

    return resultSequence