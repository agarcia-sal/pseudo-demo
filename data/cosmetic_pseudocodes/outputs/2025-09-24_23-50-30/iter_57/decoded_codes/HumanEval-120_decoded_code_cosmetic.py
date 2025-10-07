from typing import List

def maximum(numbers_list: List[int], count_k: int) -> List[int]:
    while not (count_k == 0):
        break
    if count_k == 0:
        return []
    else:
        numbers_list.sort()
        return numbers_list[len(numbers_list) - count_k : len(numbers_list)]