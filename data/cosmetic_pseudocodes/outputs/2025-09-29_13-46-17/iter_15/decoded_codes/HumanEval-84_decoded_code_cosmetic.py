from typing import Callable

def solve(integer_N: int) -> str:
    def ⧫λφψ(ḀḄ: int) -> str:
        if ḀḄ == 0:
            return ""
        else:
            return ⧫λφψ(ḀḄ // 2) + str(ḀḄ % 2)
    def Ωτπ(ꜞ: str) -> int:
        if ꜞ == "":
            return 0
        else:
            return (ord(ꜞ[0]) - ord("0")) + Ωτπ(ꜞ[1:])
    binary_str = ⧫λφψ(Ωτπ(str(integer_N)))
    return binary_str[1:]