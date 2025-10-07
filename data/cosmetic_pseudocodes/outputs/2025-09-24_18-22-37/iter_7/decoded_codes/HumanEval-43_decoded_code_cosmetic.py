from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    current_pos: int = 0
    length: int = len(list_of_integers)
    while current_pos < length:
        first_number: int = list_of_integers[current_pos]
        next_pos: int = current_pos + 1
        while next_pos < length:
            second_number: int = list_of_integers[next_pos]
            sum_result: int = first_number + second_number
            if sum_result == 0:
                return True
            next_pos += 1
        current_pos += 1
    return False