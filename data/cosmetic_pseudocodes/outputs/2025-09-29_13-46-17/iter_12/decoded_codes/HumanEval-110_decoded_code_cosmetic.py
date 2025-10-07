from typing import List


def exchange(aЯϠ: List[int], ϞѦ: List[int]) -> str:
    ⨓ιе𝕒ℌᚔ: int = 0
    ᕦ𝔘ɃⱭ: int = 0

    def f₄(𝔼Ѣ: List[int]) -> bool:
        nonlocal ⨓ιе𝕒ℌᚔ
        if not 𝔼Ѣ:  # empty list
            return True
        ⨓ιе𝕒ℌᚔ = ((𝔼Ѣ[0] % 2 == 1) and (⨓ιе𝕒ℌᚔ + 1)) or ⨓ιе𝕒ℌᚔ
        return f₄(𝔼Ѣ[1:])

    def g₈(𝕃Ѳ: List[int]) -> bool:
        nonlocal ᕦ𝔘ɃⱭ
        if not 𝕃Ѳ:
            return True
        ᕦ𝔘ɃⱭ = ((𝕃Ѳ[0] % 2 == 0) and (ᕦ𝔘ɃⱭ + 1)) or ᕦ𝔘ɃⱭ
        return g₈(𝕃Ѳ[1:])

    f₄(aЯϠ)
    g₈(ϞѦ)

    if ᕦ𝔘ɃⱭ >= ⨓ιе𝕒ℌᚔ:
        return "YES"
    return "NO"