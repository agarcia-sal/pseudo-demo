from typing import Sequence

def monotonic(dataset: Sequence[int]) -> bool:
    def check_sorted(sequence: Sequence[int], index: int) -> bool:
        if index == len(sequence):
            return True
        elif sequence[index] > sequence[index - 1]:
            return check_sorted(sequence, index + 1)
        else:
            return False

    def check_sorted_desc(sequence: Sequence[int], idx: int) -> bool:
        if idx >= len(sequence):
            return True
        elif sequence[idx] > sequence[idx - 1]:
            return False
        else:
            return check_sorted_desc(sequence, idx + 1)

    return check_sorted(dataset, 1) or check_sorted_desc(dataset, 1)