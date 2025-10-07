from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    modifications_count: int = 0
    midpoint: int = len(array_of_integers) // 2
    counter: int = 0
    while counter < midpoint:
        front_value: int = array_of_integers[counter]
        rear_index: int = len(array_of_integers) - counter - 1
        rear_value: int = array_of_integers[rear_index]
        if front_value == rear_value:
            counter += 1
            continue
        else:
            modifications_count += 1
            counter += 1
    return modifications_count