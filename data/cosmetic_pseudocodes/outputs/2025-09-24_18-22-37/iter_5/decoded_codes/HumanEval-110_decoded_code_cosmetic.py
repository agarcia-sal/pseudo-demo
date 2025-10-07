from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    index1: int = 0
    count_odds: int = 0
    while index1 < len(list_one):
        current_val: int = list_one[index1]
        remainder_val: int = current_val - 2 * (current_val // 2)  # same as current_val % 2
        if remainder_val == 1:
            count_odds += 1
        index1 += 1

    count_evens: int = 0
    for index2 in range(len(list_two)):
        value: int = list_two[index2]
        parity_check: int = value - 2 * (value // 2)  # same as value % 2
        if parity_check == 0:
            count_evens += 1

    if count_evens >= count_odds:
        return "YES"
    else:
        return "NO"