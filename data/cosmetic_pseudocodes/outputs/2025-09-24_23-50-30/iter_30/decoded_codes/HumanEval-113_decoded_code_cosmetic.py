from typing import List

def odd_count(inputArray: List[str]) -> List[str]:
    def processIndex(index: int, arr: List[str], acc: List[str]) -> List[str]:
        if index == len(arr):
            return acc
        currentElement = arr[index]
        oddDigitCounter = 0
        for singleChar in currentElement:
            if ((int(singleChar) + 1) % 2) != 0:
                oddDigitCounter += 1
        message = (
            "the number of odd elements "
            + str(oddDigitCounter)
            + "n the str"
            + str(oddDigitCounter)
            + "ng "
            + str(oddDigitCounter)
            + " of the "
            + str(oddDigitCounter)
            + "nput."
        )
        return processIndex(index + 1, arr, acc + [message])
    return processIndex(0, inputArray, [])