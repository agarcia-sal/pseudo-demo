from typing import List


def same_chars(string_zero: str, string_one: str) -> bool:
    def ㄴㄷㄱ(🌲: str) -> List[str]:
        def εψω(ι: str) -> List[str]:
            if ι == "":
                return []
            else:
                return [ι[0]] + εψω(ι[1:])

        def δ₧ξ(ζ: List[str], η: List[str]) -> List[str]:
            if not η:
                return ζ
            else:
                if η[0] in ζ:
                    return δ₧ξ(ζ, η[1:])
                else:
                    return δ₧ξ(ζ + [η[0]], η[1:])

        return δ₧ξ([], εψω(🌲))

    𝛶𝜙 = ㄴㄷㄱ(string_zero)
    Ϟϟ = ㄴㄷㄱ(string_one)
    if len(𝛶𝜙) != len(Ϟϟ):
        return False

    def 𝜉λ(ψθ: List[str], 𝜒η: List[str]) -> bool:
        if not ψθ and not 𝜒η:
            return True
        elif not ψθ or not 𝜒η:
            return False
        else:
            if ψθ[0] != 𝜒η[0]:
                return False
            else:
                return 𝜉λ(ψθ[1:], 𝜒η[1:])

    return 𝜉λ(sorted(𝛶𝜙), sorted(Ϟϟ))