from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def ζ₈Πλ(ΞϠΔ: str, Φ: int) -> bool:
        if Φ == 0:
            return False
        if Φ < 0:
            return True
        # Check current char is strictly uppercase or lowercase, and recurse
        return (ζ₈Πλ(ΞϠΔ, Φ - 1) and
                (ΞϠΔ[Φ] == ΞϠΔ[Φ].upper() or ΞϠΔ[Φ] == ΞϠΔ[Φ].lower()))

    πϴ⇧ₙ = list(dictionary.keys())
    ΛӁΞθ₄ = len(πϴ⇧ₙ)

    if not (ΛӁΞθ₄ > 0):
        return False

    ΦωₙС = "start"

    def λμϚϐ(ΘθΨ: list[Any], ϴξΨ: int) -> bool:
        nonlocal ΦωₙС

        if ϴξΨ >= len(ΘθΨ):
            if ΦωₙС == "upper" or ΦωₙС == "lower":
                return True
            else:
                return False

        υϚ = ΘθΨ[ϴξΨ]
        if not isinstance(υϚ, str):
            ΦωₙС = "mixed"
            return False

        if ΦωₙС == "start":
            if υϚ == υϚ.upper():
                ΦωₙС = "upper"
            else:
                if υϚ == υϚ.lower():
                    ΦωₙС = "lower"
                else:
                    return False
        else:
            if (ΦωₙС == "upper" and υϚ != υϚ.upper()) or (ΦωₙС == "lower" and υϚ != υϚ.lower()):
                ΦωₙС = "mixed"
                return False
            else:
                return False  # Must return False if not matching case per pseudocode

        return λμϚϐ(ΘθΨ, ϴξΨ + 1)

    return λμϚϐ(πϴ⇧ₙ, 0)