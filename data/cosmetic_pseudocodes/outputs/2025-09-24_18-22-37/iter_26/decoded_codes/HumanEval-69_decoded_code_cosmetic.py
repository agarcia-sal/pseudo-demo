from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1  # Return -1 for empty input

    max_val = max(list_of_integers)
    count_array: List[int] = [0] * (max_val + 1)

    for current_element in list_of_integers:
        count_array[current_element] += 1

    result: int = -1
    for position in range(1, len(count_array)):
        occurrence = count_array[position]
        if occurrence >= position:
            result = position

    return result