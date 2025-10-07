from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def helper(bounds: int, collection: List[int], accumulator: int) -> int:
        if bounds == 0:
            return accumulator
        current, rest = collection[0], collection[1:]
        if len(str(current)) <= 2:
            return helper(bounds - 1, rest, accumulator + current)
        else:
            return helper(bounds - 1, rest, accumulator)
    return helper(integer_k, array_of_integers, 0)