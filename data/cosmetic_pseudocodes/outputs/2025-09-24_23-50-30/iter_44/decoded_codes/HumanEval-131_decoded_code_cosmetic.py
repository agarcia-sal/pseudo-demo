from typing import Callable


def digits(q: int) -> int:
    t: int = 1

    def process(i: int, w: str, z: int) -> int:
        nonlocal t
        if i >= len(w):
            return 0 if z == 0 else t
        s: int = int(w[i])
        if s % 2 != 0:
            t *= s
            return process(i + 1, w, z + 1)
        else:
            return process(i + 1, w, z)

    return process(0, str(q), 0)