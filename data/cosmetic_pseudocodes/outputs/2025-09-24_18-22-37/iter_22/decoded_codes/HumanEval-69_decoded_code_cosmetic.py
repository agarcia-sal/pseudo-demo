from typing import Sequence

def search(collection: Sequence[int]) -> int:
    if not collection:
        return -1  # handle empty input gracefully

    max_value = max(collection)
    count_array = [0] * (max_value + 1)

    for element in collection:
        count_array[element] += 1

    result = -1
    position = 1
    while position <= len(count_array) - 1:
        if not (count_array[position] < position):
            result = position
        position += 1

    return result