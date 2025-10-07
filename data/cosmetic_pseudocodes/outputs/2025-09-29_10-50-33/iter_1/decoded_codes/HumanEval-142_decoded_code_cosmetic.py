from typing import List

def sum_squares(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0
    length: int = len(list_of_integers)
    while position < length:
        current_value: int = list_of_integers[position]
        if position % 3 == 0:
            total_sum += current_value ** 2
        elif position % 4 == 0 and position % 3 != 0:
            total_sum += current_value ** 3
        else:
            total_sum += current_value
        position += 1
    return total_sum