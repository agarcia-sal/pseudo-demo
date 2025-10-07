from typing import List, Union


def median(list_of_elements: List[Union[int, float]]) -> Union[int, float]:
    temp_map: dict[int, Union[int, float]] = {}
    for each_key in range(len(list_of_elements)):
        temp_map[each_key] = list_of_elements[each_key]

    keys_sorted = sorted(temp_map)
    sorted_sequence: List[Union[int, float]] = [temp_map[key] for key in keys_sorted]

    total_count = len(sorted_sequence)
    half_index = total_count // 2
    if total_count % 2 != 0:
        return sorted_sequence[half_index]
    return (sorted_sequence[half_index - 1] + sorted_sequence[half_index]) * 0.5