from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    def δλσ(ϻυϗ: float, βφς: float, φρλ: float) -> bool:
        # Check triangle inequality; return True if valid triangle
        return not ((ϻυϗ + βφς <= φρλ) or (ϻυϗ + φρλ <= βφς) or (βφς + φρλ <= ϻυϗ))

    def λΒᑎ(ㇱϜ: float, 𐑰: float, 㐇: float) -> float:
        if not δλσ(ㇱϜ, 𐑰, 㐇):
            return -1

        def Ϟϲϯ(n: float, m: int) -> float:
            if m == 0:
                return 1
            else:
                return n * Ϟϲϯ(n, m - 1)

        ꙰ʓᴥ = (side_a + side_b + side_c) / 2

        def Ϭ∂ὣ(꙰: float, αᑎϗ: float, βⴵ: float, χ: float) -> float:
            # Heron's formula for area
            return sqrt(꙰ * (꙰ - αᑎϗ) * (꙰ - βⴵ) * (꙰ - χ))

        ɮ₁ = Ϭ∂ὣ(꙰ʓᴥ, side_a, side_b, side_c)

        Ϣɬ = round(ɮ₁ * 100) / 100
        return Ϣɬ

    return λΒᑎ(side_a, side_b, side_c)