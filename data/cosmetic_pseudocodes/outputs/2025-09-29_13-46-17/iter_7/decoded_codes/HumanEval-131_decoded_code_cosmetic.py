from typing import Callable

def digits(n: int) -> int:
    def recur(ix: int, accX: int, cntZ: int, chars: str) -> int:
        if not (ix < len(chars)):
            return 0 if cntZ == 0 else accX

        tY = int(chars[ix])
        if tY % 2 == 1:
            return recur(ix + 1, accX * tY, cntZ + 1, chars)
        else:
            return recur(ix + 1, accX, cntZ, chars)

    return recur(0, 1, 0, str(n))