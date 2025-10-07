from typing import List, Sequence

def strange_sort_list(input_seq: List[int]) -> List[int]:
    output_seq: List[int] = []
    toggle_switch: bool = False

    while len(input_seq) > 0:
        if not toggle_switch:
            chosen_val = min(input_seq)
        else:
            chosen_val = max(input_seq)

        output_seq.append(chosen_val)

        for idx in range(len(input_seq)):
            if input_seq[idx] == chosen_val:
                input_seq.pop(idx)
                break

        toggle_switch = not toggle_switch

    return output_seq