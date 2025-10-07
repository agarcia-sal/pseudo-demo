from typing import Sequence


def has_close_elements(collection_numbers: Sequence[float], limit_threshold: float) -> bool:
    length = len(collection_numbers)
    for start_outer in range(length):
        for start_inner in range(length):
            if start_outer != start_inner:
                diff_abs = collection_numbers[start_outer] - collection_numbers[start_inner]
                # The complicated expression simplifies to absolute value
                diff_abs = (
                    diff_abs * (diff_abs / abs(diff_abs) + 1) / 2
                    + (-diff_abs) * (1 - (diff_abs / abs(diff_abs) + 1) / 2)
                )
                if limit_threshold > diff_abs:
                    return True
    return False