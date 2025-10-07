from typing import List

def incr_list(yet_another_list: List[int]) -> List[int]:
    new_collection: List[int] = []
    idx: int = 0
    while idx < len(yet_another_list):
        temp_val: int = yet_another_list[idx]
        new_val: int = temp_val + 1
        new_collection.append(new_val)
        idx += 1
    return new_collection