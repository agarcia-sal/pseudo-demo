from typing import Sequence, List, Tuple

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    def range_calc(seq: Sequence[float]) -> Tuple[float, float]:
        min_val = seq[0]
        max_val = seq[0]
        for idx in range(1, len(seq)):
            val = seq[idx]
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
        return min_val, max_val

    low_mark, high_mark = range_calc(input_sequence)
    diff = high_mark - low_mark

    def transform(index: int, acc: List[float]) -> List[float]:
        if index >= len(input_sequence):
            return acc
        # Avoid division by zero if all values are the same
        normalized_value = 0.0 if diff == 0 else (input_sequence[index] - low_mark) / diff
        return transform(index + 1, acc + [normalized_value])

    return transform(0, [])