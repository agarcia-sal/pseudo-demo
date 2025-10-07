from typing import List

def maximum(sequence_numbers: List[int], count_k: int) -> List[int]:
    if count_k == 0:
        return []
    sorted_seq = sorted(sequence_numbers)
    length_seq = len(sorted_seq)
    start_idx = length_seq - count_k
    return sorted_seq[start_idx:length_seq]