from typing import Tuple


def digits(x: int) -> int:
    def iterateChars(i: int, p: int, c: int) -> Tuple[int, int]:
        s = str(x)
        if i >= len(s):
            return p, c
        d = int(s[i])
        if d % 2 == 1:
            return iterateChars(i + 1, p * d, c + 1)
        else:
            return iterateChars(i + 1, p, c)

    product, count = iterateChars(0, 1, 0)
    return 0 if count == 0 else product