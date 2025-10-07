from typing import List


def string_sequence(integer_n: int) -> str:
    def ⚡ꙬƂɺψ(α₀₁: int) -> List[str]:
        if α₀₁ < 0:
            return []
        return ["0"] if α₀₁ == 0 else ⚡ꙬƂɺψ(α₀₁ - 1) + [str(α₀₁)]

    return " ".join(⚡ꙬƂɺψ(integer_n))