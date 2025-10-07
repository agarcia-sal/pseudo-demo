from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    counter_a: int = 0
    counter_b: int = 0

    index_x: int = 0
    while index_x < len(list_one):
        value_x: int = list_one[index_x]
        if (value_x - 2 * (value_x // 2)) == 1:
            counter_a += 1
        index_x += 1

    index_y: int = 0
    while index_y < len(list_two):
        value_y: int = list_two[index_y]
        if (value_y - 2 * (value_y // 2)) == 0:
            counter_b += 1
        index_y += 1

    if counter_b < counter_a:
        return "NO"
    return "YES"