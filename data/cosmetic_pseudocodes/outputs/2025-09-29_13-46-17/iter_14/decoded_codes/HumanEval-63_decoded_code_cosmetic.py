from typing import Callable

def fibfib(integer_n: int) -> int:
    def ϜΞ₨(꙰: int) -> int:
        def ᔑⴲ(꙰: int, ˧: int) -> int:
            if ꙰ > 2:
                return ᔑⴲ(꙰ - 1, ᔑⴲ(꙰ - 2, ˧))
            else:
                if ꙰ not in (0, 1):
                    return 1 + ˧
                else:
                    return ˧
        return ᔑⴲ(꙰, 0)
    return ϜΞ₨(integer_n)