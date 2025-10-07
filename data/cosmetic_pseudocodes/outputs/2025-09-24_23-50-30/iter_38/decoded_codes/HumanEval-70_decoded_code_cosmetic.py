from typing import List

def strange_sort_list(sequence_of_nums: List[int]) -> List[int]:
    outcome_seq: List[int] = []
    toggle_indicator: bool = True
    seq_copy = sequence_of_nums.copy()
    while seq_copy:
        if toggle_indicator:
            val = min(seq_copy)
        else:
            val = max(seq_copy)
        outcome_seq.append(val)
        seq_copy.remove(val)
        toggle_indicator = not toggle_indicator
    return outcome_seq