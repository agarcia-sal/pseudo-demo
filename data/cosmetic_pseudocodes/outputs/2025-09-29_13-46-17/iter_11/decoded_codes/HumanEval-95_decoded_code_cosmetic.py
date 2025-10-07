from typing import Any, Dict, List, Union


def check_dict_case(Ωηχ: Dict[Any, Any]) -> bool:
    def 𝜀ψ(βθ: bool, λξ: bool, ϰρ: bool, ζτ: str) -> bool:
        # Returns False if (ζτ is "upper" and βθ is False) or (ζτ is "lower" and λξ is False), else True
        if not (not ((ζτ == "upper") and (not βθ)) and not ((ζτ == "lower") and (not λξ))):
            return False
        else:
            return True

    def ςκ(νυ: int, πφ: int, ωψ: List[bool], χψ: int, ξβ: bool) -> bool:
        if not χψ:
            return ξβ
        else:
            return ςκ(νυ, πφ, ωψ, χψ - 1, ωψ[χψ - 1] and ξβ)

    def ιω(υσ: str, φγ: str, υβ: int) -> bool:
        if υβ == len(υσ):
            return True
        else:
            return ιω(υσ, φγ, υβ + 1) and (υσ[υβ] in φγ)

    def ξχ(κλ: str) -> bool:
        return ιω(κλ, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0)

    def ζρ(κλ: str) -> bool:
        return ιω(κλ, "abcdefghijklmnopqrstuvwxyz", 0)

    if len(Ωηχ.keys()) == 0:
        return False
    else:
        def Ɛτ(Σμ: int, Ζλ: List[Any], κσ: str) -> str:
            if Σμ == len(Ζλ):
                return κσ
            else:
                current_key = Ζλ[Σμ]
                if not isinstance(current_key, str):
                    return Ɛτ(Σμ + 1, Ζλ, "mixed")
                else:
                    if κσ == "start":
                        if ξχ(current_key):
                            return Ɛτ(Σμ + 1, Ζλ, "upper")
                        elif ζρ(current_key):
                            return Ɛτ(Σμ + 1, Ζλ, "lower")
                        else:
                            return "mixed"
                    elif (κσ == "upper" and not ξχ(current_key)) or (κσ == "lower" and not ζρ(current_key)):
                        return "mixed"
                    else:
                        return Ɛτ(Σμ + 1, Ζλ, κσ)

        ϕλ: List[Any] = list(Ωηχ.keys())
        μψ: str = Ɛτ(0, ϕλ, "start")

        return (μψ == "upper") or (μψ == "lower")