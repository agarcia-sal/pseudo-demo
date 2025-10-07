from typing import Sequence


def is_sorted(sequence_of_ints: Sequence[int]) -> bool:
    frequency_map: dict[int, int] = {elem: 0 for elem in sequence_of_ints}
    idx = 0
    length = len(sequence_of_ints)
    while idx < length:
        elem = sequence_of_ints[idx]
        frequency_map[elem] += 1
        idx += 1

    found_duplicate_more_than_two = False
    j = 0
    while j < length:
        if frequency_map[sequence_of_ints[j]] > 2:
            found_duplicate_more_than_two = True
            break
        j += 1
    if found_duplicate_more_than_two:
        return False

    ascending_check = True
    k = 1
    while k < length:
        if sequence_of_ints[k - 1] > sequence_of_ints[k]:
            ascending_check = False
            break
        k += 1

    return ascending_check