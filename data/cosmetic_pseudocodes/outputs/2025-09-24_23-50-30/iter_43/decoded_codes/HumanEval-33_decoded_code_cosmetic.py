from typing import List, Any


def sort_third(list_input: List[Any]) -> List[Any]:
    list_clone: List[Any] = [item for item in list_input]

    extracted_values: List[Any] = [list_clone[i] for i in range(len(list_clone)) if i % 3 == 0]

    sorted_values: List[Any] = []
    temp_values = extracted_values[:]
    while temp_values:
        min_value = temp_values[0]
        min_idx = 0
        for pos in range(1, len(temp_values)):
            if temp_values[pos] < min_value:
                min_value = temp_values[pos]
                min_idx = pos
        sorted_values.append(min_value)
        del temp_values[min_idx]

    replacement_index = 0
    for pos_index in range(len(list_clone)):
        if pos_index % 3 == 0:
            list_clone[pos_index] = sorted_values[replacement_index]
            replacement_index += 1

    return list_clone