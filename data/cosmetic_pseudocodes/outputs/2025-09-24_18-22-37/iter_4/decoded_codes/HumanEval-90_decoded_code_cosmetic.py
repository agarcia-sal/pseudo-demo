from typing import List, Optional

def next_smallest(input_numbers: List[int]) -> Optional[int]:
    temp_set = set()
    for item in input_numbers:
        temp_set.add(item)

    ordered_unique = []
    for element in temp_set:
        ordered_unique.append(element)

    index = 0
    while index < len(ordered_unique) - 1:
        current_min = ordered_unique[index]
        min_pos = index
        j = index + 1
        while j < len(ordered_unique):
            if ordered_unique[j] < current_min:
                current_min = ordered_unique[j]
                min_pos = j
            j += 1
        if min_pos != index:
            ordered_unique[index], ordered_unique[min_pos] = ordered_unique[min_pos], ordered_unique[index]
        index += 1

    if len(ordered_unique) <= 1:
        return None
    else:
        return ordered_unique[1]