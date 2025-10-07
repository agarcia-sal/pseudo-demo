from typing import Sequence, List, Union


def median(input_sequence: Sequence[Union[int, float]]) -> float:
    def perform_sort(unsorted_seq: List[Union[int, float]], sorted_acc: List[Union[int, float]]) -> List[Union[int, float]]:
        if not unsorted_seq:
            return sorted_acc
        min_val = unsorted_seq[0]
        rest_vals: List[Union[int, float]] = []
        for item in unsorted_seq:
            if item < min_val:
                rest_vals.append(min_val)
                min_val = item
            else:
                rest_vals.append(item)
        return perform_sort(rest_vals, sorted_acc + [min_val])

    ordered_sequence = perform_sort(list(input_sequence), [])
    seq_length = len(ordered_sequence)
    mid_index = (seq_length // 2) - (1 if seq_length % 2 == 0 else 0)

    if seq_length % 2 != 0:
        return float(ordered_sequence[mid_index + 1])
    else:
        first_elem = ordered_sequence[mid_index]
        second_elem = ordered_sequence[mid_index + 1]
        return (first_elem + second_elem) / 2.0