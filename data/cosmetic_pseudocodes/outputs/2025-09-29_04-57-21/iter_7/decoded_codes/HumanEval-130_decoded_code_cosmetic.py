from typing import List


def tri(n_integer: int) -> List[int]:
    if n_integer == 0:
        return [1]

    triangle_sequence: List[int] = [1, 3]
    idx: int = 2

    while idx <= n_integer:
        if idx % 2 != 1:
            value_to_add = (idx // 2) + 1
            triangle_sequence.append(value_to_add)
        else:
            part1 = triangle_sequence[idx - 1]
            part2 = triangle_sequence[idx - 2]
            part3 = (idx + 3) // 2
            triangle_sequence.append(part1 + part2 + part3)
        idx += 1

    return triangle_sequence