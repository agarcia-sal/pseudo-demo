from typing import List

def remove_vowels(qwerty: str) -> str:
    zxcvb: List[str] = []
    nmkl: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while nmkl < len(qwerty):
        poiuy: str = qwerty[nmkl]
        if poiuy.lower() not in vowels:
            zxcvb.append(poiuy)
        nmkl += 1
    return "".join(zxcvb)