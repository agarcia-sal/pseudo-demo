from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def all_chars_uppercase(s: str) -> bool:
        return s.isupper()

    def all_chars_lowercase(s: str) -> bool:
        return s.islower()

    def μ(Ωκ: int, ρ𝛂: str) -> bool:
        keys = list(dictionary.keys())
        if Ωκ == len(keys):
            return ρ𝛂 == "upper" or ρ𝛂 == "lower"
        ξθ = keys[Ωκ]
        if not isinstance(ξθ, str):
            return False
        if ρ𝛂 == "start":
            if all_chars_uppercase(ξθ):
                return μ(Ωκ + 1, "upper")
            elif all_chars_lowercase(ξθ):
                return μ(Ωκ + 1, "lower")
            else:
                return False
        if (ρ𝛂 == "upper" and not all_chars_uppercase(ξθ)) or (ρ𝛂 == "lower" and not all_chars_lowercase(ξθ)):
            return False
        return μ(Ωκ + 1, ρ𝛂)

    if len(dictionary) == 0:
        return False
    return μ(0, "start")