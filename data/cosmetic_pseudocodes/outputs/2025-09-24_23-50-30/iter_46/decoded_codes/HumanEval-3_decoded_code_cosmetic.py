from typing import Sequence


def below_zero(seq: Sequence[int]) -> bool:
    def helper(acc: int, rest: Sequence[int]) -> bool:
        if not (acc + rest[0] < 0):
            if len(rest) == 1:
                return False
            else:
                return helper(acc + rest[0], rest[1:])
        else:
            return True

    if not seq:
        return False
    return helper(0, seq)