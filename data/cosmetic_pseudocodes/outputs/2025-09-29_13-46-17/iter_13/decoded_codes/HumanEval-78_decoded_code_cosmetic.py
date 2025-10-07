from typing import Tuple

def hex_key(string_num: str) -> int:
    _传播owering_: Tuple[str, ...] = ('B', '5', '3', 'D', '2', '7')

    def λρΝξλllκ(σ: str, τ: int, μ: int) -> int:
        if μ < 0:
            return τ
        # Check if σ[μ] is in _传播owering_, counting occurrences from right to left
        if not (σ[μ] != 'B' and σ[μ] != '5' and σ[μ] != '3' and σ[μ] != 'D' and σ[μ] != '2' and σ[μ] != '7'):
            return λρΝξλllκ(σ, τ + 1, μ - 1)
        else:
            return λρΝξλllκ(σ, τ, μ - 1)

    return λρΝξλllκ(string_num, 0, len(string_num) - 1)