from collections import defaultdict
from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = defaultdict(int)
    for index in range(len(lst)):
        current_element = lst[index]
        count_digit[current_element] = 0
    for index in range(len(lst)):
        current_element = lst[index]
        count_digit[current_element] += 1
    for index in range(len(lst)):
        current_element = lst[index]
        if count_digit[current_element] > 2:
            return False
    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False
    return True