from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def κ₃ΘϘλ(Φ么: str) -> List[str]:
        def Я₿ĈυΣ(Ω₴: str, χ₳: int) -> int:
            if χ₳ < 0:
                return 0
            else:
                if Ω₴[χ₳].lower() not in {"a", "e", "i", "o", "u"}:
                    return 1 + Я₿ĈυΣ(Ω₴, χ₳ - 1)
                else:
                    return Я₿ĈυΣ(Ω₴, χ₳ - 1)

        def ζ₣ɋΔ(ξψς: List[str], υ: int) -> List[str]:
            if not ξψς:
                return []
            else:
                ϝϸ = ξψς[0]
                τ₳₿ = ζ₣ɋΔ(ξψς[1:], υ)
                if Я₿ĈυΣ(ϝϸ, len(ϝϸ) - 1) == υ:
                    return [ϝϸ] + τ₳₿
                else:
                    return τ₳₿

        return ζ₣ɋΔ(Φ么.split(" "), natural_number_n)

    return κ₃ΘϘλ(string_s)