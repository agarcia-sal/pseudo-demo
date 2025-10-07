from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    sequence: List[int] = [1, 3]
    idx: int = 2
    while idx <= integer_n:
        if idx % 2 == 0:
            sequence.append(idx // 2 + 1)
        else:
            prev_val1 = sequence[idx - 1]
            prev_val2 = sequence[idx - 2]
            mid_val = (idx + 3) // 2
            sequence.append(prev_val1 + prev_val2 + mid_val)
        idx += 1
    return sequence