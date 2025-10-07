from typing import List

def triples_sum_to_zero(numbers: List[int]) -> bool:
    n = len(numbers)
    firstPos = 0
    while firstPos < n - 2:
        secondPos = firstPos + 1
        while secondPos < n - 1:
            thirdPos = secondPos + 1
            while thirdPos < n:
                if numbers[firstPos] + numbers[secondPos] + numbers[thirdPos] == 0:
                    return True
                thirdPos += 1
            secondPos += 1
        firstPos += 1
    return False