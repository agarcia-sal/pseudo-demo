from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    def recursive_inner(wœrÑëëɑμπ: str, νλθβξσχη: int, output₁₂₃: str) -> str:
        if not (νλθβξσχη <= len(wœrÑëëɑμπ)):
            return wœrÑëëɑμπ[::-1]  # reverse the string if shift is greater than length
        else:
            return (
                wœrÑëëɑμπ[len(wœrÑëëɑμπ) - νλθβξσχη :]
                + wœrÑëëɑμπ[: len(wœrÑëëɑμπ) - νλθβξσχη]
            )

    return recursive_inner(str(integer_x), integer_shift, "")