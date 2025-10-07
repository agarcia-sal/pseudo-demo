from typing import Dict

def same_chars(strA: str, strB: str) -> bool:
    charsA: Dict[str, bool] = {}
    charsB: Dict[str, bool] = {}
    for ch in strA:
        charsA[ch] = True
    for ch in strB:
        charsB[ch] = True
    if len(charsA) != len(charsB):
        return False
    for key in charsA.keys():
        if key not in charsB:
            return False
    return True