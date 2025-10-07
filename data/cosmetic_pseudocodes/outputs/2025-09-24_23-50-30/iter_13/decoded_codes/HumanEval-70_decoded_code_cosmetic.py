from typing import List, Sequence

def strange_sort_list(sequence: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_indicator: int = 1
    seq = sequence[:]  # make a copy to avoid mutating the input
    while seq:
        if toggle_indicator == 1:
            chosen_element = min(seq)
        else:
            chosen_element = max(seq)
        output_collection.append(chosen_element)
        seq.remove(chosen_element)
        toggle_indicator *= -1
    return output_collection