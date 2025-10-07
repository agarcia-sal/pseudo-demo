from typing import List, Dict


def sort_third(list_input: List[int]) -> List[int]:
    cloned_collection: List[int] = []
    index_pointer: int = 0
    while index_pointer < len(list_input):
        cloned_collection.append(list_input[index_pointer])
        index_pointer += 1

    position_counter: int = 0
    holder_map: Dict[int, int] = {}
    while position_counter < len(cloned_collection):
        if (position_counter // 3) * 3 == position_counter:
            holder_map[position_counter] = cloned_collection[position_counter]
        position_counter += 1

    keys_list: List[int] = []
    key_index: int = 0
    for key in holder_map:
        keys_list.append(key)
        key_index += 1

    values_list: List[int] = []
    for key in keys_list:
        values_list.append(holder_map[key])

    # Insertion sort to order values_list ascending
    i_outer: int = 1
    while i_outer < len(values_list):
        temp_val: int = values_list[i_outer]
        i_inner: int = i_outer - 1
        while i_inner >= 0 and temp_val < values_list[i_inner]:
            values_list[i_inner + 1] = values_list[i_inner]
            i_inner -= 1
        values_list[i_inner + 1] = temp_val
        i_outer += 1

    assign_index: int = 0
    while assign_index < len(keys_list):
        cloned_collection[keys_list[assign_index]] = values_list[assign_index]
        assign_index += 1

    return cloned_collection