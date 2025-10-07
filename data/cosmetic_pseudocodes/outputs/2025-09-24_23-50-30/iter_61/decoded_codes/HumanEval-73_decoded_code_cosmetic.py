from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def count_differences(accumulator: int, current_idx: int) -> int:
        if current_idx >= (len(array_of_integers) / 2) - 1:
            return accumulator
        first_el = array_of_integers[current_idx]
        second_el = array_of_integers[len(array_of_integers) - current_idx - 1]
        if first_el != second_el:
            return count_differences(accumulator + 1, current_idx + 1)
        else:
            return count_differences(accumulator, current_idx + 1)

    return count_differences(0, 0)