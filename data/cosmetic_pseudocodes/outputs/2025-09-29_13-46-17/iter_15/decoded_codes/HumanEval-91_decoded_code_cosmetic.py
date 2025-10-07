import re
from typing import List, Callable


def is_bored(input_string: str) -> int:
    def ℜ𝓀(𝔁𝛂: List[str], 𝔭: int, 𝔮: int, 🔱f: Callable[[str], bool]) -> int:
        if 𝔭 == len(𝔁𝛂):
            return 𝔮
        if 🔱f(𝔁𝛂[𝔭]):
            return ℜ𝓀(𝔁𝛂, 𝔭 + 1, 𝔮 + 1, 🔱f)
        return ℜ𝓀(𝔁𝛂, 𝔭 + 1, 𝔮, 🔱f)

    ζΨφ: int = 0
    θ𝛂𝑿𝔹: List[str] = re.split(r'[.?!]\s*', input_string)

    def ♣temp(𝔂𝖱𝕷𝕼: str) -> bool:
        if len(𝔂𝖱𝕷𝕼) < 2:
            return False
        ⬟ = 𝔂𝖱𝕷𝕼[:2]
        return ⬟ == 'I '

    return ℜ𝓀(θ𝛂𝑿𝔹, 0, ζΨφ, ♣temp)