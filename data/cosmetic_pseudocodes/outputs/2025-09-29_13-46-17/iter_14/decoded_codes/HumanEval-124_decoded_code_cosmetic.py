from typing import List, Callable


def valid_date(date_string: str) -> bool:
    def τς₿цщξₐ(нϩ: str) -> bool:
        def ξ₰↯(℞ϡ: List[str], ʭ: Callable[[str], str], ζ₼: Callable[[str], int]) -> int:
            return ζ₼(ʭ(℞ϡ))

        def 🜏(ψ: List[str]) -> List[str]:
            if not ψ:
                return []
            return [ψ[0]] + 🜏(ψ[1:])

        def ⬣(λ҉: str) -> List[str]:
            if not λ҉:
                return []
            return ([], ⬣(λ҉[1:]))[λ҉[0] == '-'] if λ҉[0] == '-' else [λ҉[0]] + ⬣(λ҉[1:])  # Preserve splitting logic

        def ⬄(Ϲξμ: List[str], λ𝒷ψ: Callable[[str], int], Σ: Callable[[str], int]) -> List[int]:
            if not Ϲξμ:
                return []
            return [λ𝒷ψ(Ϲξμ[0])] + ⬄(Ϲξμ[1:], λ𝒷ψ, Σ)

        def 🜵(σϜ: str) -> bool:
            try:
                ϔྂ = σϜ
                ϔྂ = str(ϔྂ)
                # Split by '-' using ⬣ removing '-' characters
                parts = σϜ.split('-')
                # Convert parts to integers using ⬄
                ʜᔤ = ⬄(parts, lambda φ: int(φ), int)
                if len(ʜᔤ) != 3:
                    return False
                ϓ, Ӿ, Ӝ = ʜᔤ

                if not (1 <= ϓ <= 12):
                    return False

                def ƻϯ(Ζ: int) -> bool:
                    return Ζ == ϓ

                def ᔄ(Ϩ: int, ϕ: int) -> bool:
                    return Ϩ <= ϕ

                def ᖚ(ϸ: int, Ϸ: int) -> bool:
                    return ϸ >= Ϸ

                Ϯ = (ƻϯ(1) or ƻϯ(3) or ƻϯ(5) or ƻϯ(7) or ƻϯ(8) or ƻϯ(10) or ƻϯ(12)) and ((Ӿ < 1) or (Ӿ > 31))
                if Ϯ:
                    return False

                𝕜 = (ƻϯ(4) or ƻϯ(6) or ƻϯ(9) or ƻϯ(11)) and ((Ӿ < 1) or (Ӿ > 30))
                if 𝕜:
                    return False

                Ϛ = (ƻϯ(2)) and ((Ӿ < 1) or (Ӿ > 29))
                if Ϛ:
                    return False

                return True

            except Exception:
                return False

        return 🜵(нϩ)

    return τς₿цщξₐ(date_string)