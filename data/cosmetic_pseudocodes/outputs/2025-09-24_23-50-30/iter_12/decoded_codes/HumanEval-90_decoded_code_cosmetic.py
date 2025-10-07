from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_set: set[int] = set()
    for each_element in list_of_integers:
        filtered_set.add(each_element)

    sorted_array: List[int] = []
    for element_in_set in filtered_set:
        sorted_array.append(element_in_set)
    sorted_array.sort()

    length_of_sorted: int = 0
    for _ in sorted_array:
        length_of_sorted += 1

    if not (length_of_sorted >= 2):
        return None

    return sorted_array[1]