from typing import List


def unique_digits(listOfPositiveIntegers: List[int]) -> List[int]:
    def checkOddDigitsRecursively(numbersList: List[int], accumulator: List[int]) -> List[int]:
        if not numbersList:
            return accumulator
        currentNumber = numbersList[0]
        remainingNumbers = numbersList[1:]

        def isDigitOdd(num: int) -> bool:
            if num == 0:
                return True
            elif (num % 10) % 2 == 0:
                return False
            else:
                return isDigitOdd(num // 10)

        if not isDigitOdd(currentNumber):
            return checkOddDigitsRecursively(remainingNumbers, accumulator)
        else:
            return checkOddDigitsRecursively(remainingNumbers, accumulator + [currentNumber])

    collectedOddElements = checkOddDigitsRecursively(listOfPositiveIntegers, [])

    def insertionSort(listToSort: List[int]) -> List[int]:
        if len(listToSort) <= 1:
            return listToSort
        headElement = listToSort[0]
        tailSorted = insertionSort(listToSort[1:])

        def insertSorted(element: int, sortedList: List[int]) -> List[int]:
            if not sortedList:
                return [element]
            elif element <= sortedList[0]:
                return [element] + sortedList
            else:
                return [sortedList[0]] + insertSorted(element, sortedList[1:])

        return insertSorted(headElement, tailSorted)

    return insertionSort(collectedOddElements)