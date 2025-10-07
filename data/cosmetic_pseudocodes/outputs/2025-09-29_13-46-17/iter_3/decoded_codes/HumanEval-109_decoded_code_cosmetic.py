from typing import List


def move_one_ball(integer_list: List[int]) -> bool:
    if not len(integer_list) > 0:
        return True

    sorted_list = sorted(integer_list)
    min_element = min(integer_list)
    min_pos = integer_list.index(min_element)
    n = len(integer_list)

    def check_match(current_pos: int) -> bool:
        if current_pos == n:
            return True
        rotated_index = (min_pos + current_pos) % n
        if sorted_list[current_pos] != integer_list[rotated_index]:
            return False
        return check_match(current_pos + 1)

    return check_match(0)