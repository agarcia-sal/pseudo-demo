from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_list: List[int] = sorted(array_of_integers)

    def comparator(x: int, y: int) -> int:
        x_count = bin(x).count('1')
        y_count = bin(y).count('1')
        if x_count < y_count:
            return -1
        if x_count > y_count:
            return 1
        return 0

    from functools import cmp_to_key
    final_sorted_array: List[int] = sorted(temp_list, key=cmp_to_key(comparator))
    return final_sorted_array