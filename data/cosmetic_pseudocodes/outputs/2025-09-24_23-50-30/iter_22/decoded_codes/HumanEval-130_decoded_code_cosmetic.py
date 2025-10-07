from typing import List

def tri(integer_m: int) -> List[int]:
    if integer_m == 0:
        return [1]
    sequence: List[int] = [1, 3]
    index = 2
    while index <= integer_m:
        if (index % 2) == 0:
            v = (index // 2) + 1
        else:
            a = sequence[index - 1]
            b = sequence[index - 2]
            c = ((index + 3) // 2)
            v = a + b + c
        sequence.append(v)
        index += 1
    return sequence