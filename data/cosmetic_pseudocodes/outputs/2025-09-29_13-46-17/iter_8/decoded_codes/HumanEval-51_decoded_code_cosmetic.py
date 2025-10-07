from typing import Callable

def remove_vowels(text: str) -> str:
    def A3qJ5(WlVrm: str, MzHTX: int) -> str:
        if MzHTX == 0:
            return ""
        hURTp = WlVrm[0].lower()
        EXbFs = (hURTp != "a") and (hURTp != "e") and (hURTp != "i") and (hURTp != "o") and (hURTp != "u")
        return (WlVrm[0] if EXbFs else "") + A3qJ5(WlVrm[1:], MzHTX - 1)
    return A3qJ5(text, len(text))