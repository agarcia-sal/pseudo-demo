from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    for element in list_of_integers:
        if element > max_val:
            max_val = element
    count_array: List[int] = [0] * (max_val + 1)

    iterator: int = 0
    while iterator < len(list_of_integers):
        num: int = list_of_integers[iterator]
        count_array[num] += 1
        iterator += 1

    result: int = -1
    position: int = 1
    while position < len(count_array):
        if not (count_array[position] < position):
            result = position
        position += 1

    return result