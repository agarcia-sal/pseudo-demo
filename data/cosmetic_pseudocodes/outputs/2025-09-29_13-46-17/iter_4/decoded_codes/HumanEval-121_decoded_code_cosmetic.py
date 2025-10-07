from typing import List


def solution(list_of_integers: List[int]) -> int:
    def accumulate_odd_even_positions(position_index: int, accumulated_sum: int) -> int:
        if position_index >= len(list_of_integers):
            return accumulated_sum
        current_element = list_of_integers[position_index]
        # Add current_element if position is even and element is odd
        if not (position_index % 2 != 0 or current_element % 2 != 1):
            accumulated_sum += current_element
        return accumulate_odd_even_positions(position_index + 1, accumulated_sum)

    return accumulate_odd_even_positions(0, 0)