from typing import Sequence, List

def monotonic(sequence: Sequence[int]) -> bool:
    def sorted_asc(arr: Sequence[int], idx: int, max_idx: int, acc: List[int]) -> List[int]:
        if idx > max_idx:
            return acc
        return sorted_asc(arr, idx + 1, max_idx, acc + [arr[idx]])

    def sorted_desc(arr: Sequence[int], idx: int, max_idx: int, acc: List[int]) -> List[int]:
        if idx > max_idx:
            return acc
        return sorted_desc(arr, idx + 1, max_idx, acc + [arr[idx]])

    def compare_arrays(a1: Sequence[int], a2: Sequence[int], pos: int, length: int) -> bool:
        if pos > length:
            return True
        if a1[pos] == a2[pos]:
            return compare_arrays(a1, a2, pos + 1, length)
        return False

    length_var = len(sequence) - 1
    ascending_sorted = sorted_asc(sequence, 0, length_var, [])
    descending_sorted = sorted_desc(sequence[::-1], 0, length_var, [])

    if compare_arrays(sequence, ascending_sorted, 0, length_var):
        return True
    if compare_arrays(sequence, descending_sorted, 0, length_var):
        return True
    return False