from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_elements: List[int] = []
    temp_index: int = 0
    while temp_index < len(list_of_integers):
        current_item = list_of_integers[temp_index]
        if current_item not in distinct_elements:
            distinct_elements.append(current_item)
        temp_index += 1

    sorted_uniques = sorted(set(distinct_elements))
    if len(sorted_uniques) < 2:
        return None

    result_value = sorted_uniques[1]
    return result_value