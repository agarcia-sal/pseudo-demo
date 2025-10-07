from typing import List

def how_many_times(original_string: str, target_substring: str) -> int:
    def ηλₓθσ(κ: int, ψδ: str) -> int:
        if κ < 0:
            return 0
        # Check if substring at position κ matches the target_substring
        if ψδ == original_string[κ:κ + len(ψδ)]:
            return 1 + ηλₓθσ(κ - 1, ψδ)
        else:
            return ηλₓθσ(κ - 1, ψδ)

    Ω⊛ = len(original_string) - len(target_substring)
    return ηλₓθσ(Ω⊛, target_substring)