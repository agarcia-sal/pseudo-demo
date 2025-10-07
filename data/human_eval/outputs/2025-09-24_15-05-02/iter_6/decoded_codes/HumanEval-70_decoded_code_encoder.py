from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list = []
    switch = True
    numbers = list_of_integers.copy()
    while numbers:
        if switch:
            value = min(numbers)
        else:
            value = max(numbers)
        result_list.append(value)
        numbers.remove(value)
        switch = not switch
    return result_list