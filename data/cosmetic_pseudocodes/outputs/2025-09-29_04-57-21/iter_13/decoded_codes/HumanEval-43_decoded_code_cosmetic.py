from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_from(current_pos: int) -> bool:
        if current_pos >= len(list_of_integers) - 1:
            return False

        current_val = list_of_integers[current_pos]

        def scan_next(next_pos: int) -> bool:
            if next_pos >= len(list_of_integers):
                return check_from(current_pos + 1)
            if list_of_integers[next_pos] + current_val == 0:
                return True
            return scan_next(next_pos + 1)

        return scan_next(current_pos + 1)

    return check_from(0)