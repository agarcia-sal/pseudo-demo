from typing import Sequence, Union

def strlen(μₓ: Union[Sequence, str]) -> int:
    def Δβ(ζθ: int, ʘ: int) -> int:
        if ʘ == 0:
            return ζθ
        else:
            return Δβ(ζθ + 1, ʘ - 1)
    return Δβ(0, len(μₓ))