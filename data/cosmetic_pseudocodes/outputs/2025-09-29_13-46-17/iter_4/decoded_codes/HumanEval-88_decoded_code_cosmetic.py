from typing import List


def sort_array(sequence: List[int]) -> List[int]:
    def helper_sort(seq_inner: List[int]) -> List[int]:
        if not seq_inner:
            return []
        head_element = seq_inner[0]
        tail_element = seq_inner[-1]
        combined_sum = head_element + tail_element
        descending_flag = (combined_sum % 2 == 0)
        return sorted(seq_inner, reverse=descending_flag)

    return helper_sort(sequence)