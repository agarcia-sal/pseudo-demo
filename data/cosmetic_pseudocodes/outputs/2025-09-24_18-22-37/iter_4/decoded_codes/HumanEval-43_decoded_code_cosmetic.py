from typing import List

def pairs_sum_to_zero(input_list: List[int]) -> bool:
    position_x: int = 0
    while position_x < len(input_list):
        position_y: int = position_x + 1
        while position_y < len(input_list):
            if input_list[position_x] + input_list[position_y] == 0:
                return True
            position_y += 1
        position_x += 1
    return False