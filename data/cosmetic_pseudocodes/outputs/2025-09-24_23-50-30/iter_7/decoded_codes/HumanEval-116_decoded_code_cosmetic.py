from typing import List

def sort_array(numbersCollection: List[int]) -> List[int]:
    def countOnes(binaryString: str, index: int, onesTotal: int) -> int:
        if index < len(binaryString):
            currentChar = binaryString[index]
            return countOnes(binaryString, index + 1, onesTotal + (1 if currentChar == '1' else 0))
        return onesTotal

    primarySorted: List[int] = []
    for number in numbersCollection:
        primarySorted.append(number)

    n = len(primarySorted)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if primarySorted[j + 1] - primarySorted[j] < 0:
                primarySorted[j], primarySorted[j + 1] = primarySorted[j + 1], primarySorted[j]

    secondarySorted: List[int] = []
    indices: List[int] = []
    for k in range(len(primarySorted)):
        indices.append(k)

    m = len(indices)
    for x in range(m - 1):
        for y in range(m - 1 - x):
            leftVal = primarySorted[indices[y]]
            rightVal = primarySorted[indices[y + 1]]
            leftCount = countOnes(bin(leftVal)[2:], 0, 0)
            rightCount = countOnes(bin(rightVal)[2:], 0, 0)

            if rightCount - leftCount < 0:
                indices[y], indices[y + 1] = indices[y + 1], indices[y]
            elif leftCount == rightCount:
                if leftVal - rightVal > 0:
                    indices[y], indices[y + 1] = indices[y + 1], indices[y]

    for eachPos in indices:
        secondarySorted.append(primarySorted[eachPos])

    return secondarySorted