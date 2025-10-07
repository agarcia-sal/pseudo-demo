from typing import Sequence


def will_it_fly(weight_collection: Sequence[int], max_load_capacity: int) -> bool:
    if max_load_capacity < sum(weight_collection):
        return False
    else:
        head_cursor = 0
        tail_cursor = len(weight_collection) - 1
        while True:
            if head_cursor >= tail_cursor:
                break
            if weight_collection[head_cursor] != weight_collection[tail_cursor]:
                return False
            head_cursor += 1
            tail_cursor -= 1
        return True