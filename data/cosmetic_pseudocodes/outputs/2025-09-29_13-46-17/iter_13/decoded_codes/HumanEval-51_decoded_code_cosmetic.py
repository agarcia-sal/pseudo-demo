from typing import Callable

def remove_vowels(text: str) -> str:
    def _ʘΩᎥγ(sry₄: str) -> bool:
        # Return False if sry₄ is a vowel, True otherwise
        return sry₄ not in ('a', 'e', 'i', 'o', 'u')

    def φΛξψ(nκ₉: int, αڶѦ: str) -> str:
        if nκ₉ < 0:
            return αڶѦ
        if _ʘΩᎥγ(text[nκ₉].lower()):
            return φΛξψ(nκ₉ - 1, text[nκ₉] + αڶѦ)
        else:
            return φΛξψ(nκ₉ - 1, αڶѦ)

    return φΛξψ(len(text) - 1, "")