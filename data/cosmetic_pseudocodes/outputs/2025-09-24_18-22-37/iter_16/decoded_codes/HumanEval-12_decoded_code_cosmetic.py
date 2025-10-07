from typing import List, Optional

def longest(mnemonicArray: List[str]) -> Optional[str]:
    if mnemonicArray:
        lenMax: int = 0
        idx: int = 0
        while idx < len(mnemonicArray):
            currentLen = len(mnemonicArray[idx])
            if currentLen > lenMax:
                lenMax = currentLen
            idx += 1

        pos: int = 0
        while pos < len(mnemonicArray):
            if len(mnemonicArray[pos]) == lenMax:
                return mnemonicArray[pos]
            pos += 1
    else:
        return None