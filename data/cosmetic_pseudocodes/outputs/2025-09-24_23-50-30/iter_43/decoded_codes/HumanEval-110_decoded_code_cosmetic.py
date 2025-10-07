from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    index_a: int = 0
    index_b: int = 0
    count_a: int = 0
    count_b: int = 0

    len_one: int = len(list_one)
    len_two: int = len(list_two)

    while index_a < len_one or index_b < len_two:
        if index_a < len_one:
            value_x: int = list_one[index_a]
            if value_x % 2 == 1:
                count_a += 1
            index_a += 1
        if index_b < len_two:
            value_y: int = list_two[index_b]
            if value_y % 2 == 0:
                count_b += 1
            index_b += 1

    flag_result: str = "YES" if count_b >= count_a else "NO"
    return flag_result