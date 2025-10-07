from typing import Sequence

def concatenate(ι𝕏: Sequence[str]) -> str:
    def Ӝ(ʩ: Sequence[str], Ϙ: int) -> str:
        if Ϙ == 0:
            return ""
        else:
            return Ӝ(ʩ, Ϙ - 1) + ʩ[Ϙ - 1]
    return Ӝ(ι𝕏, len(ι𝕏))