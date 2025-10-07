from typing import List


def move_one_ball(numbers_list: List[int]) -> bool:
    if not numbers_list:
        return True
    ordered_list = sorted(numbers_list)
    smallest_num = numbers_list[0]
    smallest_pos = 0
    pos = 1
    while pos < len(numbers_list):
        if numbers_list[pos] < smallest_num:
            smallest_num = numbers_list[pos]
            smallest_pos = pos
        pos += 1
    shifted_list = numbers_list[smallest_pos:] + numbers_list[:smallest_pos]
    idx = 0
    while idx < len(numbers_list):
        if shifted_list[idx] != ordered_list[idx]:
            return False
        idx += 1
    return True