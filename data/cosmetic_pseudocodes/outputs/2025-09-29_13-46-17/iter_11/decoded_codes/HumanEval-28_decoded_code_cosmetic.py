from typing import Sequence

def concatenate(ζT₅: Sequence[str]) -> str:
    def jv＄(ΞϬ: Sequence[str], Ɯτ: str) -> str:
        if not ΞϬ:
            return Ɯτ
        else:
            return jv＄(ΞϬ[1:], Ɯτ + ΞϬ[0])
    return jv＄(ζT₅, "")