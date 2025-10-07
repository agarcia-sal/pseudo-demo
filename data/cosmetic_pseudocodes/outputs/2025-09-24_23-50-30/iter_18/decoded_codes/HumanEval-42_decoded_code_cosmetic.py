from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    acc: List[int] = []
    i: int = 0
    while i < len(list_of_elements):
        temp: int = list_of_elements[i]
        new_val: int = temp + 1
        acc.append(new_val)
        i += 1
    return acc