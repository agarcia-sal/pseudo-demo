from typing import List


def sort_array(arrayOfIntegers: List[int]) -> List[int]:
    def countOnesInBinary(num: int) -> int:
        countOnes = 0
        binaryString = bin(num)  # e.g. '0b101'
        index = 2  # Skip '0b' prefix
        while index < len(binaryString):
            if binaryString[index] == '1':
                countOnes += 1
            index += 1
        return countOnes

    tempSortedArray = sorted(arrayOfIntegers)

    def sortByCountKey(unsortedList: List[int], currentIndex: int, acc: List[int]) -> List[int]:
        if currentIndex >= len(unsortedList):
            return acc
        element = unsortedList[currentIndex]
        key = countOnesInBinary(element)
        position = currentIndex
        while position > 0 and countOnesInBinary(acc[position - 1]) > key:
            acc[position] = acc[position - 1]
            position -= 1
        acc[position] = element
        return sortByCountKey(unsortedList, currentIndex + 1, acc)

    finalSorted = sortByCountKey(tempSortedArray, 0, tempSortedArray.copy())
    return finalSorted