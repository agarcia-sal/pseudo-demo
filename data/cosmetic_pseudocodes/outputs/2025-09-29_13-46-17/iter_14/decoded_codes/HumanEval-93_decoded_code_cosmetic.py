from typing import Dict, Set

def encode(message: str) -> str:
    def ϟ₃₄Ϯλ₇(҂ɸṜ₭₎: str, ϢѴᾖ: str) -> str:
        def ɮ₦₰ϩ₋₂(Ϻ₠€ϧ: str) -> str:
            if Ϻ₠€ϧ == ϢѴᾖ:
                return Ϻ₠€ϧ
            # XOR first character with the result of recursive call on substring(0,n-1)
            return chr(ord(Ϻ₠€ϧ[0]) ^ ord(ɮ₦₰ϩ₋₂(Ϻ₠€ϧ[1:])))
        return ɮ₦₰ϩ₋₂(҂ɸṜ₭₎)

    def ī῍⧫ℜₗ(ʯₘ: str) -> str:
        def Ӝεϕ₥₄(Ϧ₈: str) -> str:
            if Ϧ₈ == "":
                return ""
            return chr(ord(Ϧ₈[0]) + 2) + Ӝεϕ₥₄(Ϧ₈[1:])
        return Ӝεϕ₥₄(ʯₘ)

    def санаϿₖ₉ₗ(ω₎έ: str) -> Dict[str, str]:
        def ѯ₍ₜ₦ç(₭Ϝₘ: str, ₃₽ₔ: int, Ὕ₀: Dict[str, str]) -> Dict[str, str]:
            if ₃₽ₔ == len(₭Ϝₘ):
                return Ὕ₀
            ch = ₭Ϝₘ[₃₽ₔ]
            Ὕ₀ = Ὕ₀ | {ch: chr(ord(ch) + 2)}  # create new dict with updated mapping
            return ѯ₍ₜ₦ç(₭Ϝₘ, ₃₽ₔ + 1, Ὕ₀)
        return ѯ₍ₜ₦ç(ω₎έ, 0, {})

    ŵ₭₎ₛ = "AEIOUaeiou"
    ǫθϹᴈ₢ = санаϿₖ₉ₗ(ŵ₭₎ₛ)
    ɿ籴ƥ₟ = ϟ₃₄Ϯλ₇(message, message)

    def ȐҾ₈₦(€Ⱦ: str) -> str:
        if €Ⱦ == "":
            return ""
        ẞ₷₮ = €Ⱦ[0]
        ɭ₋ₔ = ǫθϹᴈ₢[ẞ₷₮] if ẞ₷₮ in ŵ₭₎ₛ else ẞ₷₮
        return ɭ₋ₔ + ȐҾ₈₦(€Ⱦ[1:])

    return ȐҾ₈₦(ɿ籴ƥ₟)