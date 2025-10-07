from typing import List

def strange_sort_list(flake_array: List[int]) -> List[int]:
    spiral_queue: List[int] = []
    flip_switch: bool = True
    arr = flake_array[:]  # copy to avoid mutating input
    while arr:
        echo_val = min(arr) if flip_switch else max(arr)
        spiral_queue.append(echo_val)
        arr.remove(echo_val)
        flip_switch = not flip_switch
    return spiral_queue