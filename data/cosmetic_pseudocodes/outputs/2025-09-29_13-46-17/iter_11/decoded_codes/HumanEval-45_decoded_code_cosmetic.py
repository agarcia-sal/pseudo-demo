from typing import Any


def triangle_area(Ω₠: int, נ: Any) -> int:
    def ξƙ(Ł: int, ъ: Any, ↯: int) -> int:
        if ↯ == 0:
            return 0
        else:
            return Ł + ξƙ(Ł, ъ, ↯ - 1)

    λ: int = ξƙ(Ω₠, נ, 1)
    return λ // (ord("a") - ord("c") + 1)