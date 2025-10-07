from typing import List

def fibfib(index_x: int) -> int:
    list_queue: List[int] = [0, 0, 1]
    counter_i: int = 3
    while counter_i <= index_x:
        next_val = list_queue[0] + list_queue[1] + list_queue[2]
        list_queue = [list_queue[1], list_queue[2], next_val]
        counter_i += 1
    return list_queue[index_x] if index_x < 3 else list_queue[2]