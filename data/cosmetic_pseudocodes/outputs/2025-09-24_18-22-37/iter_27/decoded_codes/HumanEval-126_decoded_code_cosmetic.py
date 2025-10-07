from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(array_of_values: Sequence[T]) -> bool:
    index_map: dict[T, int] = {key: 0 for key in array_of_values}
    iterator_val = 0
    length = len(array_of_values)

    while iterator_val < length:
        current_element = array_of_values[iterator_val]
        temp_count = index_map[current_element]
        updated_count = temp_count + 1
        index_map[current_element] = updated_count
        iterator_val += 1

    violation_found = False
    check_val = 0

    while check_val < length:
        candidate_key = array_of_values[check_val]
        if index_map[candidate_key] > 2:  # Checking if count > 1+1
            violation_found = True
            break
        check_val += 1

    if violation_found:
        return False
    else:
        flag_order = True
        pos_index = 1

        while pos_index < length:
            if not (array_of_values[pos_index - 1] <= array_of_values[pos_index]):
                flag_order = False
                pos_index = length
            pos_index += 1

        if flag_order:
            return True
        else:
            return False