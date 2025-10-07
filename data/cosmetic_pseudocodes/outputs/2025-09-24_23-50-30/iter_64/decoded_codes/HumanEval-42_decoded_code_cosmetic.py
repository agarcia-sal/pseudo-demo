from typing import List

def incr_list(aggregate: List[int]) -> List[int]:
    result: List[int] = []
    index_counter: int = 0
    while index_counter < len(aggregate):
        current_val: int = aggregate[index_counter]
        result.append(current_val + (0 + 1))
        index_counter += 1
    return result