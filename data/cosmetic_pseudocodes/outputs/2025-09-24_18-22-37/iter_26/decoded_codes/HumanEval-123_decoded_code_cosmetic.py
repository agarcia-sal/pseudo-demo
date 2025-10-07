from typing import List

def get_odd_collatz(p: int) -> List[int]:
    seq: List[int]
    temp_val: int
    mod_check: int

    if p % 2 == 0:
        seq = []
    else:
        seq = [p]

    while p > 1:
        mod_check = p % 2
        if mod_check == 0:
            temp_val = p // 2
            p = temp_val
        else:
            temp_val = (p * 3) + 1
            p = temp_val
        if p % 2 == 1:
            temp_val = p
            seq.append(int(temp_val))

    ordered_seq: List[int] = sorted(seq)
    return ordered_seq