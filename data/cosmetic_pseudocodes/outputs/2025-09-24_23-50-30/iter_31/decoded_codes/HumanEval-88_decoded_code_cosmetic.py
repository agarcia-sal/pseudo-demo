from typing import List

def sort_array(input_seq: List[int]) -> List[int]:
    def helper_check(seq_len: int, seq: List[int]) -> List[int]:
        if seq_len == 0:
            return []
        edge_sum = seq[0] + seq[seq_len - 1]
        desc_flag = (edge_sum % 2 == 0)
        return sorted(seq, reverse=desc_flag)

    return helper_check(len(input_seq), input_seq)