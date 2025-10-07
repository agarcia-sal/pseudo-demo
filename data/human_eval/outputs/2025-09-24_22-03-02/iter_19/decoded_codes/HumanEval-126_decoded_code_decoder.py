from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {}
    for index in range(len(lst)):
        element = lst[index]
        if element not in count_digit:
            count_digit[element] = 0
    for index in range(len(lst)):
        element = lst[index]
        count_digit[element] += 1
    for index in range(len(lst)):
        element = lst[index]
        if count_digit[element] > 2:
            return False
    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False
    return True