from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    ctrl: List[int] = []
    idx: int = 0
    while idx < len(list_input):
        if idx % 3 == 0:
            ctrl.append(list_input[idx])
        idx += 1

    ctrl_sorted: List[int] = []
    q: int = 0
    while q < len(ctrl):
        min_val: int = ctrl[q]
        j: int = q + 1
        while j < len(ctrl):
            if ctrl[j] < min_val:
                min_val = ctrl[j]
            j += 1
        ctrl_sorted.append(min_val)
        q += 1

    dst: int = 0
    for k in range(len(list_input)):
        if k % 3 == 0:
            list_input[k] = ctrl_sorted[dst]
            dst += 1

    return list_input