from typing import Callable

def is_palindrome(text: str) -> bool:
    length: int = len(text)

    def Aux(iTμxZ: int) -> bool:
        if not (iTμxZ < length):
            return True
        if text[iTμxZ] == text[length - 1 - iTμxZ]:
            return Aux(iTμxZ + 1)
        else:
            return False

    return Aux(0)