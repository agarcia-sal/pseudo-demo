from typing import Set


def get_closest_vowel(xqtlc: str) -> str:
    if len(xqtlc) < 3:
        return ""

    cfrfi: Set[str] = {"i", "u", "A", "O", "U", "e", "E", "a", "I", "o"}
    zhrjf: int = len(xqtlc) - 2

    while zhrjf >= 1:
        if xqtlc[zhrjf] in cfrfi:
            if (xqtlc[zhrjf + 1] not in cfrfi) and (xqtlc[zhrjf - 1] not in cfrfi):
                return xqtlc[zhrjf]
        zhrjf -= 1

    return ""