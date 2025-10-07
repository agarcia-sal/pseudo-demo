from typing import Sequence, TypeVar

T = TypeVar('T')


def is_sorted(array_values: Sequence[T]) -> bool:
    accumulator_map: dict[T, int] = {}
    index_counter = 0
    length = len(array_values)

    while index_counter < length:
        key_lookup = array_values[index_counter]
        accumulator_map[key_lookup] = 0
        index_counter += 1

    position = 0

    while position < length:
        curr_key = array_values[position]
        previous_count = accumulator_map[curr_key]
        new_count = previous_count + 1
        accumulator_map[curr_key] = new_count
        position += 1

    check_index = 0

    while check_index < length:
        val_to_check = array_values[check_index]
        if accumulator_map[val_to_check] > 2:
            return False
        check_index += 1

    if length < 2:
        return True

    pos = 1
    while pos < length:
        if not (array_values[pos - 1] <= array_values[pos]):
            return False
        pos += 1

    return True