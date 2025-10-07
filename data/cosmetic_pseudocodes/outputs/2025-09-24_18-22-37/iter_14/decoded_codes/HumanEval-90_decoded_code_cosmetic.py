from typing import Optional, Sequence


def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    distinct_sorted_sequence = sorted(set(sequence_of_numbers))
    len_ds = len(distinct_sorted_sequence)

    if len_ds < 2:
        return None
    else:
        result_val = distinct_sorted_sequence[1]
        return result_val