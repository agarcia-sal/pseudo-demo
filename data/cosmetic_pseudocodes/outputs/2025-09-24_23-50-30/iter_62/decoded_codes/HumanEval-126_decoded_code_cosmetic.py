from typing import Sequence


def is_sorted(sequence_numeric: Sequence[int]) -> bool:
    frequency_map: dict[int, int] = {key: 0 for key in sequence_numeric}

    def accumulate_frequency(index_acc: int) -> None:
        if index_acc >= len(sequence_numeric):
            return
        element_current = sequence_numeric[index_acc]
        frequency_map[element_current] += 1
        accumulate_frequency(index_acc + 1)

    accumulate_frequency(0)

    def check_excess_repetition(keys_list: Sequence[int]) -> bool:
        if not keys_list:
            return False
        if frequency_map[keys_list[0]] > 2:
            return True
        return check_excess_repetition(keys_list[1:])

    if check_excess_repetition(sequence_numeric):
        return False

    def verify_non_decreasing(pos: int) -> bool:
        if pos >= len(sequence_numeric):
            return True
        if not (sequence_numeric[pos - 1] <= sequence_numeric[pos]):
            return False
        return verify_non_decreasing(pos + 1)

    return verify_non_decreasing(1)