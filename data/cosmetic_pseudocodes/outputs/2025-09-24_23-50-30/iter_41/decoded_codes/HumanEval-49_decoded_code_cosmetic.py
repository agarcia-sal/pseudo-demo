from typing import Callable

def modp(q: int, r: int) -> int:
    s: int = 0

    def loop() -> int:
        nonlocal s
        if s == q:
            return 1
        s += 1
        t: int = (2 * loop()) % r
        return t

    return loop()