import re
from typing import List

def is_bored(prop_input: str) -> int:
    seg_list: List[str] = re.split(r'[.?!]\s*', prop_input)

    def tail_calc(idx: int, acc: int) -> int:
        if idx >= len(seg_list):
            return acc
        curr_seg = seg_list[idx]
        next_acc = acc + (curr_seg[:2] == 'I ')
        return tail_calc(idx + 1, next_acc)

    return tail_calc(0, 0)