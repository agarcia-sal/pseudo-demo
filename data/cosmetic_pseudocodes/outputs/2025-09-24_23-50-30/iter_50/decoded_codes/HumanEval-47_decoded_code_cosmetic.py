from typing import List, TypeVar, Union

T = TypeVar('T', int, float)  # Elements can be int or float


def median(list_of_elements: List[T]) -> Union[T, float]:
    def sortElements(seq_in: List[T], seq_out: List[T]) -> None:
        seq_out.clear()
        for item in seq_in:
            inserted = False
            for i, val in enumerate(seq_out):
                if item <= val:
                    seq_out.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                seq_out.append(item)

    def getLength(lst: List[T], acc: int, result: List[int]) -> None:
        # Use a list of one int to simulate pass-by-reference for integers
        if acc == len(lst):
            result[0] = acc
        else:
            getLength(lst, acc + 1, result)

    def isOdd(num: int, result: List[bool]) -> None:
        result[0] = (num % 2) != 0

    sortedList: List[T] = []
    sortElements(list_of_elements, sortedList)

    lenVal_holder: List[int] = [0]
    getLength(sortedList, 0, lenVal_holder)
    lenVal = lenVal_holder[0]

    oddFlag_holder: List[bool] = [False]
    isOdd(lenVal, oddFlag_holder)
    oddFlag = oddFlag_holder[0]

    halfIndex = (lenVal - (lenVal % 2)) // 2

    if oddFlag:
        return sortedList[halfIndex]
    else:
        elemA = sortedList[halfIndex - 1]
        elemB = sortedList[halfIndex]
        medianVal = (elemA + elemB) / 2.0
        return medianVal