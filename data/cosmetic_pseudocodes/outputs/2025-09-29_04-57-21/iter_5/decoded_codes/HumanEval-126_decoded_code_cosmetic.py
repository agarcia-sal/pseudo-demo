from typing import List


def is_sorted(array_values: List[int]) -> bool:
    frequency_map = {key: 0 for key in array_values}

    def tally(index: int) -> None:
        if index > len(array_values):
            return
        frequency_map[array_values[index - 1]] += 1
        tally(index + 1)

    tally(1)

    for element in array_values:
        if frequency_map[element] > 2:
            return False

    position = 2
    while position <= len(array_values):
        if not (array_values[position - 2] <= array_values[position - 1]):
            return False
        position += 1

    return True