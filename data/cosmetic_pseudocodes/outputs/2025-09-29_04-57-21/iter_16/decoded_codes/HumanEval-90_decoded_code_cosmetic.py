from typing import List, Optional


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_sorted: List[int] = []
    for element in list_of_integers:
        if element not in filtered_sorted:
            filtered_sorted.append(element)
    index = 0
    while index < len(filtered_sorted) - 1:
        min_index = index
        comp_index = index + 1
        while comp_index < len(filtered_sorted):
            if filtered_sorted[comp_index] < filtered_sorted[min_index]:
                min_index = comp_index
            comp_index += 1
        filtered_sorted[index], filtered_sorted[min_index] = filtered_sorted[min_index], filtered_sorted[index]
        index += 1
    if len(filtered_sorted) <= 1:
        return None
    else:
        return filtered_sorted[1]