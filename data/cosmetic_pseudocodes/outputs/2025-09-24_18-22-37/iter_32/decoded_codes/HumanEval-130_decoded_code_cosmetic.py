from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    seq: List[int] = [1, 3]
    idx: int = 2

    while idx <= integer_n:
        remainder = idx % 2
        if remainder == 0:
            half = idx // 2
            seq.append(half + 1)
        else:
            pos = idx
            val1 = seq[pos - 1]
            val2 = seq[pos - 2]
            addend = (pos + 3) // 2
            value = val1 + val2 + addend
            seq.append(value)
        idx += 1

    return seq