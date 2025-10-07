from typing import Callable


def encode(x1y2z3: str) -> str:
    def BRεαkΛmbF(βϕκ: str) -> str:
        def FUNC(a: str) -> str:
            # Shift character by 2 if vowel (case insensitive), else return it as is
            if a in "uoieaUOIEA":
                return chr(ord(a) + 2)
            else:
                return a
        return FUNC(βϕκ)

    def tHεMΘrsTκ(aQWErty: str) -> str:
        # Recursive: uppercase first character + recursive call on rest, else empty string
        if aQWErty != "":
            return aQWErty[0].upper() + tHεMΘrsTκ(aQWErty[1:])
        else:
            return ""

    def κJ6Ł(λvx: str) -> str:
        # Recursive reordering: last char comes first uppercase, others follow
        if λvx == "":
            return ""
        else:
            return κJ6Ł(λvx[1:]) + tHεMΘrsTκ(λvx[0])

    def Sετ8μ(Sετ8μ_str: str, bğ: int) -> str:
        kj6ł_str = κJ6Ł(Sετ8μ_str)
        if bğ < len(kj6ł_str):
            prefix = Sετ8μ_str[:bğ]
            middle = BRεαkΛmbF(kj6ł_str[bğ])
            suffix = Sετ8μ(Sετ8μ_str, bğ + 1)
            return prefix + middle + suffix
        else:
            return ""

    return Sετ8μ(x1y2z3, 0)