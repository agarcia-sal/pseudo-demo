from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    def construct_seq(index: int, sequence: List[int]) -> List[int]:
        if index > integer_n:
            return sequence
        if index % 2 == 0:
            next_val = (index // 2) + 1
        else:
            next_val = sequence[index - 1] + sequence[index - 2] + ((index + 3) // 2)
        return construct_seq(index + 1, sequence + [next_val])

    return construct_seq(2, [1, 3])