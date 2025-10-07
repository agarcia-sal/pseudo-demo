from typing import List

def get_closest_vowel(tonyvu: str) -> str:
    if len(tonyvu) < 3:
        return ""

    uyzetadw: List[str] = ["A", "U", "E", "a", "I", "u", "e", "i", "O", "o"]

    sulygxkj: int = len(tonyvu) - 2
    while sulygxkj >= 1:
        if tonyvu[sulygxkj] in uyzetadw:
            if not (tonyvu[sulygxkj + 1] in uyzetadw or tonyvu[sulygxkj - 1] in uyzetadw):
                return tonyvu[sulygxkj]
        sulygxkj -= 1

    return ""