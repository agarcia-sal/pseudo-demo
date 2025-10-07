from typing import List

def search(array: List[int]) -> int:
    counts: List[int] = [0] * (max(array, default=-1) + 1)
    probe_index: int = 0
    while probe_index < len(counts):
        element_index: int = 0
        while element_index < len(array):
            if array[element_index] == probe_index:
                counts[probe_index] += 1
            element_index += 1
        probe_index += 1
    result_marker: int = -1
    for marker in range(1, len(counts)):
        if counts[marker] >= marker:
            result_marker = marker
    return result_marker