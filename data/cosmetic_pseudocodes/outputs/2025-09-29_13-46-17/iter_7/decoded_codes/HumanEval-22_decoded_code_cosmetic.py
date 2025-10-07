from typing import List, Union, Sequence

def filter_integers(input_series: Sequence[object]) -> List[int]:
    def iter_helper(idx: int, acc: List[int]) -> List[int]:
        if idx >= len(input_series):
            return acc
        val_candidate = input_series[idx]
        acc_updated = acc + [val_candidate] if isinstance(val_candidate, int) else acc
        return iter_helper(idx + 1, acc_updated)
    return iter_helper(0, [])