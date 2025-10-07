from typing import List


def tri(count: int) -> List[int]:
    if count == 0:
        return [1]
    sequence: List[int] = [1, 3]
    index = 2
    while index <= count:
        if (index % 2) == 0:
            sequence.append((index // 2) + 1)
        else:
            sequence.append(sequence[index - 1] + sequence[index - 2] + ((index + 3) // 2))
        index += 1
    return sequence