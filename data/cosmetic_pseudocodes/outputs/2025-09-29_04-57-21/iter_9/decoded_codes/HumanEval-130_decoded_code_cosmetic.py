from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n <= 0:
        return [1]

    sequence_list: List[int] = [1, 3]
    idx: int = 2

    while idx <= integer_n:
        if idx % 2 == 0:
            sequence_list.append(idx // 2 + 1)
        else:
            a: int = sequence_list[idx - 1]
            b: int = sequence_list[idx - 2]
            c: int = (idx + 3) // 2
            sequence_list.append(a + b + c)
        idx += 1

    return sequence_list