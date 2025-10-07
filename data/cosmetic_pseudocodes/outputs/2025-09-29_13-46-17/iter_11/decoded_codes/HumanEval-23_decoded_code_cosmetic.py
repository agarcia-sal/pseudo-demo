from typing import Optional, Sequence, Union

def strlen(Жωλ₴: Sequence[Optional[object]]) -> int:
    return λχζ(Жωλ₴, 0)

def λχζ(ΣΦ: Sequence[Optional[object]], Ϙ: int) -> int:
    if Ϙ < len(ΣΦ) and ΣΦ[Ϙ] is not None:
        return 1 + λχζ(ΣΦ, Ϙ + 1)
    else:
        return 0