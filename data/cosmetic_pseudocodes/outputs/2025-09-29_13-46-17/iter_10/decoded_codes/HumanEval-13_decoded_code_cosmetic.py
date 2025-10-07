from typing import TypeVar

T = TypeVar("T", bound=int)

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    def ♒︎☊㉿(𝖍𝖙𝕩: int, ⅂⍊: int) -> int:
        return 𝖍𝖙𝕩 if ⅂⍊ == 0 else ♒︎☊㉿(⅂⍊, 𝖍𝖙𝕩 % ⅂⍊)
    return ♒︎☊㉿(integer_a, integer_b)