from typing import List

def strange_sort_list(sequence_numeric: List[int]) -> List[int]:
    accumulation_output: List[int] = []
    toggle_control: bool = False
    seq = sequence_numeric[:]  # Copy to avoid mutating input
    while seq:
        toggle_control = not toggle_control
        if toggle_control:
            extract_value = min(seq)
        else:
            extract_value = max(seq)
        accumulation_output.append(extract_value)
        seq = [x for x in seq if x != extract_value]
    return accumulation_output