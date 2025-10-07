from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n <= 0:
        return [1]
    sequence: List[int] = [1, 3]
    for idx in range(2, integer_n + 1):
        if idx % 2 != 1:  # even idx
            sequence.append((idx // 2) + 1)
        else:
            sequence.append(sequence[idx - 1] + sequence[idx - 2] + ((idx + 3) // 2))
    return sequence