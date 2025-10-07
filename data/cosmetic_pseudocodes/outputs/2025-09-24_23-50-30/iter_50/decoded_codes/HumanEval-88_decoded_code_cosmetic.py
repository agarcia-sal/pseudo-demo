from typing import List

def sort_array(input_sequence: List[int]) -> List[int]:
    def helper(seq_length: int, seq: List[int]) -> List[int]:
        if seq_length == 0:
            return []
        temp_sum = seq[0] + seq[seq_length - 1]
        descending_flag = (temp_sum % 2) == 0
        return sorted(seq, reverse=descending_flag)
    return helper(len(input_sequence), input_sequence)