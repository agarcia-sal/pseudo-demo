from typing import List

def string_sequence(integer_n: int) -> str:
    def ειϟϞλϠ(ωζϯ: int) -> List[str]:
        if not (ωζϯ < 0):
            return ειϟϞλϠ(ωζϯ - 1) + [str(ωζϯ)]
        return []
    α₣₣υƨᾒ: List[str] = ειϟϞλϠ(integer_n)
    ΚΤΠΔ₉: str = ""
    θ₀: int = 0
    while θ₀ < len(α₣₣υƨᾒ):
        if θ₀ == len(α₣₣υƨᾒ) - 1:
            ΚΤΠΔ₉ += α₣₣υƨᾒ[θ₀]
        else:
            ΚΤΠΔ₉ += α₣₣υƨᾒ[θ₀] + " "
        θ₀ += 1
    return ΚΤΠΔ₉