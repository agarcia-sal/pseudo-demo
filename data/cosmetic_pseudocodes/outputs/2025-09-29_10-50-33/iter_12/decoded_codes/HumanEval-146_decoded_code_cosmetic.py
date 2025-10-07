from typing import List


def specialFilter(list_of_numbers: List[int]) -> int:
    accumulate = 0
    odd_digit_set = {9, 7, 5, 3, 1}

    def processIndex(index: int) -> None:
        nonlocal accumulate
        if index >= 0:
            currentVal = list_of_numbers[index]
            if currentVal > 10:
                numStr = str(currentVal)
                if int(numStr[0]) in odd_digit_set and int(numStr[-1]) in odd_digit_set:
                    accumulate += 1
            processIndex(index - 1)

    processIndex(len(list_of_numbers) - 1)
    return accumulate