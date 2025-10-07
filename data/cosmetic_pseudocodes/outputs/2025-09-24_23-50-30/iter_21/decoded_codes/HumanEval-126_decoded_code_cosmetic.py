from typing import Sequence


def is_sorted(sequence_numbers: Sequence[int]) -> bool:
    map_frequency: dict[int, int] = {}
    for element_index in range(len(sequence_numbers)):
        key_value = sequence_numbers[element_index]
        if key_value not in map_frequency:
            map_frequency[key_value] = 0
        map_frequency[key_value] += 1

    iterator_index = 0
    while iterator_index < len(sequence_numbers):
        if map_frequency[sequence_numbers[iterator_index]] > 2:
            return False
        iterator_index += 1

    def check_sorted_rec(position: int) -> bool:
        if position >= len(sequence_numbers):
            return True
        elif sequence_numbers[position - 1] <= sequence_numbers[position]:
            return check_sorted_rec(position + 1)
        else:
            return False

    return check_sorted_rec(1)