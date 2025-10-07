from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    results: List[str] = []

    def ᗣᖚᖇ(λ: List[str]) -> List[str]:
        if not λ:
            return results
        ₡₥₮: str = λ[0]

        def 𐌥𐌧(λ₁: List[str], ⊕: int) -> int:
            if not λ₁:
                return ⊕
            𝕞𝕟: str = λ₁[0]
            Ϣ: int = (int(𝕞𝕟) + 1) % 2
            ϡ: int = 0 if Ϣ == 0 else 1
            return 𐌥𐌧(λ₁[1:], ⊕ + ϡ)

        split_chars: List[str] = list(₡₥₮)
        ℮↯: int = 𐌥𐌧(split_chars, 0)
        ℒₓ: str = (
            "the number of odd elements "
            + str(℮↯)
            + "n the str"
            + str(℮↯)
            + "ng "
            + str(℮↯)
            + " of the "
            + str(℮↯)
            + "nput."
        )
        results.append(ℒₓ)
        return ᗣᖚᖇ(λ[1:])

    return ᗣᖚᖇ(list_of_strings)