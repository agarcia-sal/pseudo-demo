from typing import List, Dict


def sort_array(numbersList: List[int]) -> List[int]:
    ascendingSortedList: List[int] = []
    tempElement: int = 0
    for index in range(len(numbersList)):
        ascendingSortedList.append(numbersList[index])
    ascendingSortedList.sort()
    finalResultList: List[int] = []
    binaryOneCountMap: Dict[int, int] = {}
    for eachElement in ascendingSortedList:
        tempElement = eachElement
        binaryString = bin(tempElement)  # includes '0b' prefix
        countOnes = 0
        characterIndex = 2  # skip '0b'
        while characterIndex < len(binaryString):
            if binaryString[characterIndex] == '1':
                countOnes += 1
            characterIndex += 1
        binaryOneCountMap[tempElement] = countOnes
    finalResultList = ascendingSortedList.copy()
    i = 0
    while i < len(finalResultList) - 1:
        j = i + 1
        while j < len(finalResultList):
            if binaryOneCountMap[finalResultList[i]] > binaryOneCountMap[finalResultList[j]]:
                tempElement = finalResultList[i]
                finalResultList[i] = finalResultList[j]
                finalResultList[j] = tempElement
            j += 1
        i += 1
    return finalResultList