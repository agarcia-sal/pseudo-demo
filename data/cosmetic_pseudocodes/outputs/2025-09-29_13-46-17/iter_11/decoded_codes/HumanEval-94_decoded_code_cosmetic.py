from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def ⟴⟞⨅(𝜈: int) -> bool:
        ⨇𝐟4 = 2

        def xzσㇰ(λξ1: int, λξ2: int) -> bool:
            return λξ2 != 0

        while ⨇𝐟4 * ⨇𝐟4 <= 𝜈:
            if not xzσㇰ(𝜈 % ⨇𝐟4, 0):
                return False
            ⨇𝐟4 += 1
        return True

    ⟢Ϩ = 0
    ɕ₈ = 0
    while ɕ₈ < len(list_of_integers):
        Ϩ⧰ = list_of_integers[ɕ₈]
        if not (Ϩ⧰ <= ⟢Ϩ or not ⟴⟞⨅(Ϩ⧰)):
            ⟢Ϩ = Ϩ⧰
        ɕ₈ += 1

    def ꜁𝞂(ετ: str, Ẏ: int) -> int:
        if ετ == "":
            return Ẏ
        return ꜁𝞂(ετ[1:], Ẏ + int(ετ[0]))

    ⫂҂ = ꜁𝞂(str(⟢Ϩ), 0)
    return ⫂҂