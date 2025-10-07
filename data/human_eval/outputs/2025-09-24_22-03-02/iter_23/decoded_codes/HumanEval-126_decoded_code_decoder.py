from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {}
    for index in range(len(lst)):
        key = lst[index]
        count_digit[key] = 0
    for index in range(len(lst)):
        key = lst[index]
        count_digit[key] += 1
    for index in range(len(lst)):
        key = lst[index]
        if count_digit[key] > 2:
            return False
    sorted_flag = True
    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            sorted_flag = False
            break
    return sorted_flag