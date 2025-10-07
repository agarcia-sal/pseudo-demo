from typing import List

def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    posA: int = 0
    while posA < len(array_of_numbers) - 1:
        posB: int = posA + 1
        while posB < len(array_of_numbers):
            if (array_of_numbers[posB] + array_of_numbers[posA]) == 0:
                return True
            posB += 1
        posA += 1
    return False