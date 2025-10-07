from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def υɆ(ƃɍ: int, ƀкᴚ: int) -> int:
        if ƀкᴚ <= 0:
            return 1
        else:
            return (2 * υɆ(ƃɍ, ƀкᴚ - 1)) % integer_p
    return υɆ(integer_n, integer_n)