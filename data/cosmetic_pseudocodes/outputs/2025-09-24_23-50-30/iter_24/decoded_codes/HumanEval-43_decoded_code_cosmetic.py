from typing import List

def pairs_sum_to_zero(arr: List[int]) -> bool:
    def check_from_position(pos_x: int) -> bool:
        if pos_x >= len(arr):
            return False

        def inner_loop(pos_y: int) -> bool:
            if pos_y >= len(arr):
                return check_from_position(pos_x + 1)
            if arr[pos_x] + arr[pos_y] == 0:
                return True
            return inner_loop(pos_y + 1)

        return inner_loop(pos_x + 1)

    return check_from_position(0)