from typing import List

def maximum(sequence_nums: List[int], count_pos: int) -> List[int]:
    if count_pos == 0:
        return []

    sorted_seq = sequence_nums[:]  # Make a copy to avoid mutating input
    n = len(sorted_seq)
    # Bubble sort implementation
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_seq[j + 1] < sorted_seq[j]:
                sorted_seq[j], sorted_seq[j + 1] = sorted_seq[j + 1], sorted_seq[j]

    start_index = n - count_pos

    def slice_sublist(lst: List[int], start_idx: int, end_idx: int) -> List[int]:
        if start_idx >= end_idx:
            return []
        else:
            return [lst[start_idx]] + slice_sublist(lst, start_idx + 1, end_idx)

    result_set = slice_sublist(sorted_seq, start_index, n)
    return result_set