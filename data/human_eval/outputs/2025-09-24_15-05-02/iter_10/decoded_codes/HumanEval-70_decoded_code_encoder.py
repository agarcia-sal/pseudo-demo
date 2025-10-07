from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    res = []
    switch = True
    numbers = list_of_integers.copy()
    while len(numbers) > 0:
        if switch:
            value = min(numbers)
        else:
            value = max(numbers)
        res.append(value)
        numbers.remove(value)
        switch = not switch
    return res