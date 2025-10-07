from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    tally_map: dict[int, int] = {}

    def accumulate_counts(seq: List[int], idx: int) -> None:
        if idx >= len(seq):
            return
        element = seq[idx]
        tally_map[element] = tally_map.get(element, 0) + 1
        accumulate_counts(seq, idx + 1)

    accumulate_counts(list_of_numbers, 0)

    for key in tally_map:
        if tally_map[key] > 2:
            return False

    position = 1
    while position < len(list_of_numbers):
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            return False
        position += 1

    return True