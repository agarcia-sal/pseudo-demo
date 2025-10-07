from typing import Sequence, List, Union


def pluck(sequence_of_elements: Sequence[int]) -> List[int]:
    if not sequence_of_elements:
        return []
    filtered_collection = [item for item in sequence_of_elements if item % 2 == 0]
    if not filtered_collection:
        return []
    min_value = filtered_collection[0]
    for index_var in range(1, len(filtered_collection)):
        if filtered_collection[index_var] < min_value:
            min_value = filtered_collection[index_var]
    position_var = 0
    while position_var < len(sequence_of_elements) and sequence_of_elements[position_var] != min_value:
        position_var += 1
    return [min_value, position_var]