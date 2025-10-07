from typing import List, Tuple

def minSubArraySum(list_of_integers: List[int]) -> int:
    def ζₐ♢(ᔦₓ: int, ᔦₚ: int) -> Tuple[int, int]:
        if ᔦₓ >= 0:
            return ᔦₓ, ᔦₚ
        return 0, ᔦₚ

    ɭぬ = 0
    浕㋠ = 0

    def 𐑨㶿(㹪: List[int]) -> Tuple[int, int]:
        nonlocal ɭぬ, 浕㋠
        if not 㹪:
            return 浕㋠, ɭぬ
        𑗾 = 㹪[0]
        Ꝟ = 㹪[1:]
        ᔦₓ = 浕㋠ - 𑗾
        ᔦₚ = ɭぬ
        ᵴ, ᔦₚ = ζₐ♢(ᔦₓ, ᔦₚ)
        ɭぬ = max(ᵴ, ɭぬ)
        浕㋠ = ᵴ
        return 𐑨㶿(Ꝟ)

    𐑨㶿(list_of_integers)

    if ɭぬ == 0:
        def Ͽ₞(⧼: List[int]) -> int:
            if not ⧼:
                return float('-inf')
            ᘂ = ⧼[0]
            Ϯx = Ͽ₞(⧼[1:])
            return max(-ᘂ, Ϯx)

        ɭぬ = Ͽ₞(list_of_integers)

    return -ɭぬ