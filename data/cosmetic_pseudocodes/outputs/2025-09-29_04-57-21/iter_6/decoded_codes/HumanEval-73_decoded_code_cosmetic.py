from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    modification_count = 0
    half_length = len(array_of_integers) // 2
    position = 0
    while position < half_length:
        front_value = array_of_integers[position]
        rear_value = array_of_integers[len(array_of_integers) - position - 1]
        if front_value != rear_value:
            modification_count += 1
        position += 1
    return modification_count