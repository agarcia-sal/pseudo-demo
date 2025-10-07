from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def helper(index: int, acc: int) -> int:
        if index >= integer_k:
            return acc
        else:
            acc += array_of_integers[index] if len(str(array_of_integers[index])) <= 2 else 0
            return helper(index + 1, acc)
    return helper(0, 0)