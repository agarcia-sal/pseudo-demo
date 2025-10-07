from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    counter_a = 0
    counter_b = 0
    index_x = 0
    while index_x < len(list_one):
        current_val = list_one[index_x]
        remainder_val = current_val % 2
        if remainder_val == 1:
            counter_a += 1
        index_x += 1

    index_y = 0
    while index_y < len(list_two):
        current_val_2 = list_two[index_y]
        remainder_val_2 = current_val_2 % 2
        if remainder_val_2 == 0:
            counter_b += 1
        index_y += 1

    if counter_b >= counter_a:
        return "YES"
    else:
        return "NO"