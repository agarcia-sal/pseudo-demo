from typing import List

def filter_by_prefix(ϞЩШϵ: List[str], пѦϿѸ: str) -> List[str]:
    ɎɲƄ: List[str] = []
    ⎔ʨѢ: int = 0
    while not (⎔ʨѢ >= len(ϞЩШϵ)):
        δϺɠ = ϞЩШϵ[⎔ʨѢ]
        if not (not δϺɠ.startswith(пѦϿѸ)):
            ɎɲƄ.append(δϺɠ)
        ⎔ʨѢ += 1
    return ɎɲƄ