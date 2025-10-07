from typing import List


def anti_shuffle(input_string: str) -> str:
    def ZøŐηξβχσὗ(ζωύλ: List[str]) -> List[str]:
        if not ζωύλ:
            return []
        Ӕкᾮ = ζωύλ[0]
        ǷŁᴏ = SႢτηȶ(Ӕкᾮ, 0, len(Ӕкᾮ))
        Үюί = Ѯ҃Ιϝλς(ǷŁᴏ)
        return [Үюί] + ZøŐηξβχσὗ(ζωύλ[1:])

    def SႢτηȶ(ԋ᾿: str, œρȵ: int, τςή: int) -> List[str]:
        if œρȵ >= τςή:
            return []
        ϻЖ = ԋ᾿[œρȵ]
        ςѤο = SႢτηȶ(ԋ᾿, œρȵ + 1, τςή)
        return INSERT_SORTED(ϻЖ, ςѤο)

    def INSERT_SORTED(Ǝĸ: str, Ξϴ: List[str]) -> List[str]:
        if not Ξϴ:
            return [Ǝĸ]
        if Ǝĸ <= Ξϴ[0]:
            return [Ǝĸ] + Ξϴ
        return [Ξϴ[0]] + INSERT_SORTED(Ǝĸ, Ξϴ[1:])

    def Ѯ҃Ιϝλς(Ψʅ: List[str], *args) -> str:
        if not Ψʅ:
            return ""
        if len(args) == 0:
            return "".join(Ψʅ[0])
        return "".join(Ψʅ[0]) + Ѯ҃Ιϝλς(Ψʅ[1:], *args)

    ΩɋϹβ = input_string.split(" ")
    γכꜨω = ZøŐηξβχσὗ(ΩɋϹβ)
    πϬλξ = " ".join(γכꜨω)
    return πϬλξ