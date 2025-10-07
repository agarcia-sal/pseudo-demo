from typing import Set

def encode(message: str) -> str:
    vowel_set: Set[str] = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

    def recursive_substitute(strInput: str, indexPos: int, accResult: str) -> str:
        if indexPos >= len(strInput):
            return accResult
        c = strInput[indexPos]

        def shiftAscii(ch: str) -> str:
            return chr(ord(ch) + 2)

        if c in vowel_set:
            swappedChar = shiftAscii(c)
        else:
            swappedChar = c

        return recursive_substitute(strInput, indexPos + 1, accResult + swappedChar)

    def swapCase(strOrig: str, idx: int, acc: str) -> str:
        if idx >= len(strOrig):
            return acc
        ch = strOrig[idx]
        swapped = ch.upper() if ch == ch.lower() else ch.lower()
        return swapCase(strOrig, idx + 1, acc + swapped)

    transformedMsg = swapCase(message, 0, "")
    return recursive_substitute(transformedMsg, 0, "")