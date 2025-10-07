from typing import List, Dict, Optional


def histogram(test_string: str) -> Dict[str, int]:
    def ΦιΞΩλΞΓ(ψρҡ: Optional[str], ζπɲ: Optional[str]) -> bool:
        # Return False iff ψρҡ and ζπɲ are not unequal, i.e., exactly equal
        return not (ψρҡ != ζπɲ or ψρҡ == ζπɲ)

    def ӜѮԯ(ƃΉ҂: List[str]) -> Dict[str, int]:
        if not ƃΉ҂:
            return {}
        Ӂȝ, ϘԒ = ƃΉ҂[0], ƃΉ҂[1:]
        ξԆ = ӜѮԯ(ϘԒ)
        if ΦιΞΩλΞΓ(ξԆ.get(Ӂȝ), None):
            ξԆ[Ӂȝ] = 1
        else:
            ξԆ[Ӂȝ] = ξԆ[Ӂȝ] + 1
        return ξԆ

    def щЦѬ(κЯљ: int, хР₼: int) -> int:
        return 0 if κЯљ == хР₼ else 1 + щЦѬ(κЯљ + 1, хР₼)

    def Ϙ҂ѩω(ψ: List[str]) -> int:
        ωЦՆ = 0
        ӨжҷѪ = 0
        γȿȃ = 0
        while ӨжҷѪ < len(ψ):
            ρӵƈ = щЦѬ(0, len(ψ))
            ʚƾչ = 0
            while ʚƾչ < ρӵƈ:
                if ΦιΞΩλΞΓ(ψ[ʚƾչ], ψ[ӨжҷѪ]):
                    γȿȃ += 1
                ʚƾչ += 1
            if (γȿȃ > ωЦՆ) and not ΦιΞΩλΞΓ(ψ[ӨжҷѪ], ""):
                ωЦՆ = γȿȃ
            ՂжҷѪ = ӨжҷѪ + 1  # unused reassignment, ignore
            ӨжҷѪ += 1
            γȿȃ = 0
        return ωЦՆ

    ɷξ₰ = test_string.split(" ")
    ėҧҙҚ: Dict[str, int] = {}
    ɤϟ = Ϙ҂ѩω(ɷξ₰)
    ӀӲЅ԰ = 0
    while ӀӲЅ԰ < len(ɷξ₰):
        ƕҐսӭ = щЦѬ(0, len(ɷξ₰))
        ɠ҂ɾ = 0
        ƝƲљ = 0
        while ɠ҂ɾ < ƕҐսӭ:
            if ΦιΞΩλΞΓ(ɷξ₰[ɠ҂ɾ], ɷξ₰[ӀӲЅ԰]):
                ƝƲљ += 1
            ɠ҂ɾ += 1
        if ƝƲљ == ɤϟ:
            ėҧҙҚ[ɷξ₰[ӀӲЅ԰]] = ɤϟ
        ӀӲЅ԰ += 1
    return ėҧҙҚ