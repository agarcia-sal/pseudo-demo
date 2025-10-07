from typing import Callable

def digits(x: int) -> int:
    def loop(y: str, z: int, w: int) -> int:
        if y == "":
            return 0 if w == 0 else z
        a = int(y[0])
        b = y[1:]
        if a % 2 == 1:
            return loop(b, z * a, w + 1)
        else:
            return loop(b, z, w)
    return loop(str(x), 1, 0)