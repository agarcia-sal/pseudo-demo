from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def sum_helper(position: int, accumulator: int) -> int:
        if position > integer_k:
            return accumulator
        element = array_of_integers[position - 1]
        if len(str(element)) <= 2:
            return sum_helper(position + 1, accumulator + element)
        return sum_helper(position + 1, accumulator)
    return sum_helper(1, 0)