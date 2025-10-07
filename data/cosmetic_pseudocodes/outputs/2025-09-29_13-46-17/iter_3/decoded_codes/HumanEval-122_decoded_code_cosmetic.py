from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def helper(index: int, totalSum: int) -> int:
        if index == integer_k:
            return totalSum
        if len(str(array_of_integers[index])) > 2:
            return helper(index + 1, totalSum)
        return helper(index + 1, totalSum + array_of_integers[index])

    return helper(0, 0)