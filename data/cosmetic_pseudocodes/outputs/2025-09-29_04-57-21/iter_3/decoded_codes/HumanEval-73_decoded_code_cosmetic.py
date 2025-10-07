from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def count_mismatches(accumulator: int, position: int) -> int:
        if position < len(array_of_integers) // 2:
            front_element = array_of_integers[position]
            back_element = array_of_integers[len(array_of_integers) - position - 1]
            increment = 1 if front_element != back_element else 0
            return count_mismatches(accumulator + increment, position + 1)
        return accumulator

    return count_mismatches(0, 0)