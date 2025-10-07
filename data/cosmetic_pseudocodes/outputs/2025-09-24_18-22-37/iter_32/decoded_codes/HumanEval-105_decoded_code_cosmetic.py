from typing import List, Dict

def by_length(input_list: List[int]) -> List[str]:
    mapping_numbers: Dict[int, str] = {
        9: "Nine",
        6: "Six",
        2: "Two",
        3: "Three",
        1: "One",
        4: "Four",
        8: "Eight",
        7: "Seven",
        5: "Five"
    }

    descending_sorted: List[int] = []
    index_tracker: int = 0
    while index_tracker < len(input_list):
        descending_sorted.append(input_list[index_tracker])
        index_tracker += 1

    position: int = 0
    while position < len(descending_sorted) - 1:
        scan: int = 0
        while scan < len(descending_sorted) - position - 1:
            # If descending_sorted[scan] >= descending_sorted[scan + 1], no swap;
            # otherwise, swap to bubble lower values upwards for descending order
            if not (descending_sorted[scan] < descending_sorted[scan + 1]):
                scan += 1
            else:
                descending_sorted[scan], descending_sorted[scan + 1] = descending_sorted[scan + 1], descending_sorted[scan]
                scan += 1
        position += 1

    result_list: List[str] = []
    iter_index: int = 0
    while iter_index < len(descending_sorted):
        current_item = descending_sorted[iter_index]
        if current_item in mapping_numbers:
            result_list.append(mapping_numbers[current_item])
        iter_index += 1

    return result_list