from typing import List

def smallest_change(list_x: List[int]) -> int:
    count_changes = 0
    max_pos = (len(list_x) // 2) - 1
    cursor = 0
    while cursor <= max_pos:
        if list_x[cursor] != list_x[len(list_x) - 1 - cursor]:
            count_changes += 1
            # break from switch equivalent - already done by if/else
        cursor += 1
    return count_changes