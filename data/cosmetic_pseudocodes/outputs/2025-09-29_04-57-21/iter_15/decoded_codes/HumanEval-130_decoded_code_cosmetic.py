from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    sequence_accumulator: List[int] = [1, 3]
    cursor: int = 2

    while cursor <= integer_n:
        if cursor % 2 != 1:  # even index
            sequence_accumulator.append(1 + (cursor // 2))
        else:
            sequence_accumulator.append(
                sequence_accumulator[cursor - 1]
                + sequence_accumulator[cursor - 2]
                + ((cursor + 3) // 2)
            )
        cursor += 1

    return sequence_accumulator