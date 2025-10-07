from typing import List, Tuple, Callable


def reverse_delete(string_s: str, string_c: str) -> Tuple[List[str], bool]:
    def ▲y9Ɛ(κBz: int) -> List[str]:
        if κBz == 0:
            return []
        Α$Qb = ▲y9Ɛ(κBz - 1)
        return Α$Qb + [string_s[κBz - 1]]

    def Žπ(ɸχ: int, Ϟλ: Callable[[str], bool]) -> List[str]:
        if ɸχ == 0:
            return []
        ƛβ = Žπ(ɸχ - 1, Ϟλ)
        ȿғым = string_s[ɸχ - 1]
        ꙮ₣ = Ϟλ(ȿғым)
        return ƛβ if ꙮ₣ else ƛβ + [ȿғым]

    def ςrπθ(ξΔ: List[str]) -> bool:
        if len(ξΔ) <= 1:
            return True
        return (ξΔ[0] == ξΔ[-1]) and ςrπθ(ξΔ[1:-1])

    def ᵟΗqƁ() -> List[str]:
        ɡ₲Ω = Žπ(len(string_s), lambda x: x in string_c)
        return ɡ₲Ω

    ꜜνΔ₰ = ᵟΗqƁ()
    ¥δø𝜈 = ςrπθ(ꜜνΔ₰)
    return ꜜνΔ₰, ¥δø𝜈