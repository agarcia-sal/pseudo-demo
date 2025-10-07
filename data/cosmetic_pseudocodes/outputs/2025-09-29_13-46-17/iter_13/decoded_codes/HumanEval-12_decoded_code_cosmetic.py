from typing import List, Optional, Union


def longest(list_of_strings: List[str]) -> Optional[str]:
    def helper(
        χ₁: List[str], ἦ: int
    ) -> Optional[str]:
        if not χ₁:
            return None
        𝒙ₐ = 0  # unused in pseudocode logic but preserved as is
        𝒙_b = -1
        𝖆𝗋𝖌𝖍𝗀ὸ: Optional[str] = None

        def recur_iter(
            ςζγ: List[str], ιω: int, ἀ: int, β: Optional[str]
        ) -> Optional[str]:
            if ιω >= len(ςζγ):
                return β
            κ = len(ςζγ[ιω])
            if κ >= ἀ:
                return recur_iter(ςζγ, ιω + 1, κ, ςζγ[ιω])
            else:
                return recur_iter(ςζγ, ιω + 1, ἀ, β)

        return recur_iter(χ₁, 0, 𝒙_b, 𝖆𝗋𝖌𝖍𝗀ὸ)

    return helper(list_of_strings, 0)