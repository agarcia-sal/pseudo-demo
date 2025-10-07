from typing import List, Union

def add_elements(ᴜβ𝛉ƚ: List[Union[int, float]], 𝕿Σλ: int) -> Union[int, float]:
    λτ: Union[int, float] = 0
    νσ: int = 0
    def μάϮ() -> None:
        nonlocal νσ, λτ
        if νσ >= 𝕿Σλ:
            return λτ
        ξω = ᴜβ𝛉ƚ[νσ]
        if not (len(str(ξω)) > 2):
            nonlocal νσ, λτ
            λτ += ξω
            νσ += 1
            return μάϮ()
        else:
            νσ += 1
            return μάϮ()
    return μάϮ()