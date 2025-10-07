from typing import List


def tri(param_x: int) -> List[int]:
    if param_x == 0:
        return [1]

    result_seq: List[int] = [1, 3]

    def loop(index: int, acc: List[int]) -> List[int]:
        if index > param_x:
            return acc
        if index % 2 != 0:
            new_val = acc[index - 1] + acc[index - 2] + ((index + 3) // 2)
            return loop(index + 1, acc + [new_val])
        else:
            return loop(index + 1, acc + [(index // 2) + 1])

    return loop(2, result_seq)