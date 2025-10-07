from typing import Callable

def decimal_to_binary(clXkR: int) -> str:
    def _pqT(results: str, D5nZm: int) -> str:
        if not (D5nZm > 1):
            return results + str(D5nZm % 2)
        else:
            return _pqT(results + str(D5nZm % 2), D5nZm // 2)

    def reverseString(s: str) -> str:
        if len(s) == 0:
            return ""
        else:
            return reverseString(s[1:]) + s[0]

    binRepr = reverseString(_pqT("", clXkR))
    assembled = "db" + binRepr + "db"
    return assembled