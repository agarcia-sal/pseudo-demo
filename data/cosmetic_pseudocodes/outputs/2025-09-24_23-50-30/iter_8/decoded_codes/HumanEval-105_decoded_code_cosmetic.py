from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    alpha_map: Dict[int, str] = {
        9: "Nine",
        7: "Seven",
        3: "Three",
        6: "Six",
        2: "Two",
        8: "Eight",
        5: "Five",
        1: "One",
        4: "Four",
    }

    array = array_of_integers[:]  # copy to avoid mutating input
    descending_list: List[int] = []

    while len(array) > 0:
        max_val = array[0]
        max_index = 0
        for idx in range(1, len(array)):
            if array[idx] > max_val:
                max_val = array[idx]
                max_index = idx
        descending_list.append(max_val)
        array.pop(max_index)

    result_list: List[str] = []
    index_counter = 0
    while index_counter < len(descending_list):
        current_key = descending_list[index_counter]
        val = alpha_map.get(current_key)
        if val is not None:
            result_list.append(val)
        index_counter += 1

    return result_list