from typing import List


def tri(integer_n: int) -> List[int]:
    def recur(inner_i: int, acc: List[int]) -> List[int]:
        if inner_i > integer_n:
            return acc
        if inner_i % 2 != 1:
            next_val = (inner_i // 2) + 1
        else:
            idx1 = inner_i - 1
            idx2 = inner_i - 2
            next_val = acc[idx1] + acc[idx2] + ((inner_i + 3) // 2)
        return recur(inner_i + 1, acc + [next_val])

    if integer_n <= 0:
        return [1]
    return recur(2, [1, 3])