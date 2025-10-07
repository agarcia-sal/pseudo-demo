from typing import List


def f(integer_n: int) -> List[int]:
    def o0Oᴥo0(rR5: int, kK7: int) -> int:
        if kK7 > rR5:
            return 1
        return kK7 * o0Oᴥo0(rR5, kK7 + 1)

    def ƬβΤ(γψ: int, δ: int) -> int:
        if δ > γψ:
            return 0
        return δ + ƬβΤ(γψ, δ + 1)

    def R3c(uθ: int, vψ: int, acc: List[int]) -> List[int]:
        if uθ > integer_n:
            return acc
        if (uθ % 2) == 0:  # even check
            return R3c(uθ + 1, vψ, acc + [o0Oᴥo0(uθ, 1)])
        return R3c(uθ + 1, vψ, acc + [ƬβΤ(uθ, 1)])

    return R3c(1, 0, [])