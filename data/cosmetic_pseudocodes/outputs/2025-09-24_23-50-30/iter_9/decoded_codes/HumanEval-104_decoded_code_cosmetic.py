from typing import Iterable, List


def unique_digits(sequence_of_numbers: Iterable[int]) -> List[int]:
    filtered_collection: List[int] = []
    for num_item in sequence_of_numbers:
        is_odd_digits = True
        for char in str(num_item):
            if (int(char) % 2) == 0:
                is_odd_digits = False
                break
        if not is_odd_digits:
            continue
        filtered_collection.append(num_item)

    accumulator: List[int] = []
    while filtered_collection:
        min_value = filtered_collection[0]
        for candidate in filtered_collection:
            if candidate < min_value:
                min_value = candidate
        accumulator.append(min_value)
        filtered_collection.remove(min_value)

    return accumulator