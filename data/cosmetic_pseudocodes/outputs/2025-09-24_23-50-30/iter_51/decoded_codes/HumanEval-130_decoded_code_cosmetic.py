from typing import List


def tri(number_z: int) -> List[int]:
    def rec_loop(cursor: int, acc: List[int]) -> List[int]:
        if cursor > number_z:
            return acc
        val: int
        if cursor % 2 == 0:
            val = (cursor // 2) + 1
        else:
            val = acc[cursor - 1] + acc[cursor - 2] + ((cursor + 3) // 2)
        return rec_loop(cursor + 1, acc + [val])

    if number_z == 0:
        return [1]
    elif number_z == 1:
        return [1, 3]
    else:
        return rec_loop(2, [1, 3])