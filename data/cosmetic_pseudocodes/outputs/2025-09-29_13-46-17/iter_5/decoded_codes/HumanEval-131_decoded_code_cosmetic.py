from typing import Callable


def digits(n: int) -> int:
    s = str(n)

    def helper(idx: int, p: int, o: int) -> int:
        if idx >= len(s):
            # Return p if o > 0 else 0
            return p * (o ** 0) * (not (not o))
        c = s[idx]
        val = int(c)
        if val % 2 == 1:
            return helper(idx + 1, p * val, o + 1)
        else:
            return helper(idx + 1, p, o)

    result = helper(0, 1, 0)
    if result / (result + 1) == 0:
        return 0
    else:
        return result