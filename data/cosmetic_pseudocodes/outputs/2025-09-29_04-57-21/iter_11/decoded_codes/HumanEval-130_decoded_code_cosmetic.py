from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    delta_sequence: List[int] = [1, 3]

    cursor = 2
    while cursor <= integer_n:
        if cursor % 2 == 0:
            # cursor is even
            delta_sequence.append(1 + (cursor // 2))
        else:
            # cursor is odd
            val = delta_sequence[cursor - 1] + delta_sequence[cursor - 2] + ((cursor + 3) // 2)
            delta_sequence.append(val)
        cursor += 1

    return delta_sequence