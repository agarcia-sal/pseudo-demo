from typing import Sequence


def strlen(input: Sequence) -> int:
    def computeLength(data: Sequence, count: int) -> int:
        if not data:
            return count
        else:
            return computeLength(data[1:], count + 1)

    return computeLength(input, 0)