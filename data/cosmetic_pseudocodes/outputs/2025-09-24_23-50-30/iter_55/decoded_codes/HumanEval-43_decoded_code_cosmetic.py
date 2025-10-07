from typing import List


def pairs_sum_to_zero(array_integers: List[int]) -> bool:
    def check_pairs_recursion(current_x: int, total_length: int) -> bool:
        if current_x == total_length:
            return False

        def check_inner_pairs(current_y: int) -> bool:
            if current_y == total_length:
                return check_pairs_recursion(current_x + 1, total_length)
            if array_integers[current_x] + array_integers[current_y] == 0:
                return True
            return check_inner_pairs(current_y + 1)

        return check_inner_pairs(current_x + 1)

    return check_pairs_recursion(0, len(array_integers))