from typing import List

def concatenate(ΔΨλ: List[str]) -> str:
    result: str = ""
    index: int = 0

    def Λ₮() -> None:
        nonlocal index, result
        if index == len(ΔΨλ):
            return
        result += ΔΨλ[index]
        index += 1
        Λ₮()

    Λ₮()
    return result