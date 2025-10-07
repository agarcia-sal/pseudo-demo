from typing import List, Union

def pluck(list_of_elements: List[int]) -> List[int]:
    # Equivalent to: if not (len(list_of_elements) > 0): return []
    # Simplified: if len(list_of_elements) == 0: return []
    if len(list_of_elements) == 0:
        return []

    filtered_values: List[int] = []
    position_tracker: int = 0

    # Collect even elements
    while position_tracker < len(list_of_elements):
        if list_of_elements[position_tracker] % 2 == 0:
            filtered_values.append(list_of_elements[position_tracker])
        position_tracker += 1

    if len(filtered_values) == 0:
        return []

    minimal_value = filtered_values[0]
    minimal_pos = 0
    counter_var = 1

    while counter_var < len(filtered_values):
        if filtered_values[counter_var] < minimal_value:
            minimal_value = filtered_values[counter_var]
            minimal_pos = counter_var
        counter_var += 1

    real_index_tracker = 0
    while real_index_tracker < len(list_of_elements) and list_of_elements[real_index_tracker] != minimal_value:
        real_index_tracker += 1

    return [minimal_value, real_index_tracker]