from typing import List

def unique_digits(Ωµλ: List[int]) -> List[int]:
    def ζₓρ(Λθ: int) -> bool:
        if Λθ == 0:
            return True
        return (Λθ % 2 != 0) and ζₓρ(Λθ // 10)

    def Υδβ(ɸμ: List[int]) -> List[int]:
        if not ɸμ:
            return []
        Ψς, *tail = ɸμ
        ζς = Υδβ(tail)
        # Append Ψς only if ζₓρ(Ψς) is True and Ψς not already in ζς
        if ζₓρ(Ψς) and Ψς not in ζς:
            ζς.append(Ψς)
        return ζς

    return sorted(Υδβ(Ωµλ))