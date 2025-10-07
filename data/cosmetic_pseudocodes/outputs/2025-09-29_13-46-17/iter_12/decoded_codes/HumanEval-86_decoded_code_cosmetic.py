from typing import List


def anti_shuffle(input_string: str) -> str:
    def ζ₍㉐₎(φₔ: str) -> List[str]:
        # Recursively convert string to list of characters
        return [] if φₔ == "" else [φₔ[0]] + ζ₍㉐₎(φₔ[1:])

    def 𝕣𝖊𝖛𝔼𝔯𝔰𝔼(卍_卐: List[str]) -> List[str]:
        def ǂ(ƨℸ: List[str], Ꭶ: List[str]) -> List[str]:
            return Ꭶ if ƨℸ == [] else ǂ(ƨℸ[1:], [ƨℸ[0]] + Ꭶ)
        return ǂ(卍_卐, [])

    def 𝔠𝔥𝔞𝔯_𝔰𝔬𝔯𝔱(𝕩𝕐𝕫: List[str]) -> List[str]:
        if not 𝕩𝕐𝕫:
            return []
        ℧𝔭𝔩 = 𝕩𝕐𝕫[0]
        𝔰𝔪𝔞𝔩𝔩𝔢𝔯 = [𝕒 for 𝕒 in 𝕩𝕐𝕫[1:] if 𝕒 <= ℧𝔭𝔩]
        𝔟𝔦𝔤𝔤𝔢𝔯 = [𝕒 for 𝕒 in 𝕩𝕐𝕫[1:] if 𝕒 > ℧𝔭𝔩]
        return 𝔠𝔥𝔞𝔯_𝔰𝔬𝔯𝔱(𝔰𝔪𝔞𝔩𝔩𝔢𝔯) + [℧𝔭𝔩] + 𝔠𝔥𝔞𝔯_𝔰𝔬𝔯𝔱(𝔟𝔦𝔤𝔤𝔢𝔯)

    def 𝔰𝔬𝔯𝔱𝔴𝔬𝔯𝔡(★: str) -> str:
        # Sorts characters of the word lexicographically
        return "".join(𝔠𝔥𝔞𝔯_𝔰𝔬𝔯𝔱(ζ₍㉐₎(★)))

    def 𝟝(Ϙψ: List[str]) -> List[str]:
        def Γ(ℇψ: List[str], ωκ: int, Α: List[str]) -> List[str]:
            if ωκ == len(ℇψ):
                return Α
            𝕘𝖑 = 𝔰𝔬𝔯𝔱𝔴𝔬𝔯𝔡(ℇψ[ωκ])
            return Γ(ℇψ, ωκ + 1, Α + [𝕘𝖑])

        return Γ(Ϙψ, 0, [])

    Δψϙ = input_string.split(" ")
    ηΩ = 𝟝(Δψϙ)
    Ζ𝔵𝕣 = " ".join(ηΩ)
    return Ζ𝔵𝕣