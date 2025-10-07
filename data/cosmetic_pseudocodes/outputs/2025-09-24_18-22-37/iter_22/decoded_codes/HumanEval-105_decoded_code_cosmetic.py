from typing import List

def by_length(values_list: List[int]) -> List[str]:
    num_names_map = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }

    # Make a copy of values_list to temp_sorted
    temp_sorted: List[int] = []
    index_counter = 0
    while index_counter < len(values_list):
        temp_sorted.append(values_list[index_counter])
        index_counter += 1

    # Sort temp_sorted in descending order by repeatedly selecting max
    descending_sorted: List[int] = []
    while temp_sorted:
        max_val = temp_sorted[0]
        pos = 0
        i = 1
        while i < len(temp_sorted):
            if temp_sorted[i] > max_val:
                max_val = temp_sorted[i]
                pos = i
            i += 1
        descending_sorted.append(max_val)
        temp_sorted.pop(pos)

    # Build result_list from descending_sorted filtering to keys in 1-9
    result_list: List[str] = []
    cursor = 0
    while cursor < len(descending_sorted):
        current_val = descending_sorted[cursor]
        if current_val in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            lookup_key = current_val
            name_found = ""
            if lookup_key in num_names_map:
                name_found = num_names_map[lookup_key]
                result_list.append(name_found)
        cursor += 1

    return result_list