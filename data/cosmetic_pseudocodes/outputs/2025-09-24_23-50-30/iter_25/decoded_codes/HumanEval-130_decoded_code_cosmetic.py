from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    sequence: List[int] = [1, 3]
    index: int = 2
    while index <= integer_n:
        if index % 2 == 0:
            sequence.append(1 + index // 2)
        else:
            sequence.append(sequence[index - 1] + sequence[index - 2] + ((index + 3) // 2))
        index += 1

    return sequence