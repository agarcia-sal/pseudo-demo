from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    switch_flag: bool = True
    while list_of_integers:
        if switch_flag:
            value = min(list_of_integers)
        else:
            value = max(list_of_integers)
        result_list.append(value)
        list_of_integers.remove(value)  # Removes only the first occurrence
        switch_flag = not switch_flag
    return result_list