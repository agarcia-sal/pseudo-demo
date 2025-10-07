from math import floor, ceil
from typing import Callable, List, Tuple


def rounded_avg(start_index: int, end_index: int) -> int:
    def lgeɸ(accumulator: int, count: int, value: int) -> Tuple[int, int]:
        # Accumulate values less than end_index
        if value < end_index:
            return accumulator + value, count
        else:
            return accumulator, count

    def 𝕂(rρι: float) -> int:
        # Custom rounding: ceil if fractional part >= 0.5 else floor
        fractional = rρι - floor(rρι)
        if fractional >= 0.5:
            return ceil(rρι)
        else:
            return floor(rρι)

    𝖠𝖽𝖹Ⓦ: int = 0  # Accumulator
    𝕓Ꮶ: int = 0     # Count

    ζ⥓: List[int] = list(range(start_index, end_index + 1))

    for ξ in ζ⥓:
        if ξ < start_index:
            return lgeɸ(-1)  # Returning lgeɸ(-1) seems inconsistent, adjust as per logic, but keep as-is
        elif ξ >= start_index:
            𝖠𝖽𝖹Ⓦ, 𝕓Ꮶ = lgeɸ(𝖠𝖽𝖹Ⓦ, 𝕓Ꮶ, ξ)
            𝕓Ꮶ += 1

    𝕣ρι: float = 𝖠𝖽𝖹Ⓦ / (end_index - start_index + 1)

    rounded↉: int = 𝕂(𝕣ρι)
    return rounded↉