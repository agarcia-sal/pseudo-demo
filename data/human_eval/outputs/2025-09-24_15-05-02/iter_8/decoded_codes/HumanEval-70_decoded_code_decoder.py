from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    sorted_list = sorted(list_of_integers)
    result_list: List[int] = []
    switch = True
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        if switch:
            result_list.append(sorted_list[left])
            left += 1
        else:
            result_list.append(sorted_list[right])
            right -= 1
        switch = not switch
    return result_list