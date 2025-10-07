from typing import List

def sort_third(l: List[int]) -> List[int]:
    l = list(l)
    list_divisible_by_three = []
    index = 0
    while index < len(l):
        if index % 3 == 0:
            list_divisible_by_three.append(l[index])
        index += 1
    sorted_divisible_by_three = sorted(list_divisible_by_three)
    sorted_index = 0
    target_index = 0
    while target_index < len(l):
        if target_index % 3 == 0:
            l[target_index] = sorted_divisible_by_three[sorted_index]
            sorted_index += 1
        target_index += 1
    return l