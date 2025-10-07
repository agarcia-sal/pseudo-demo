from typing import Callable


def correct_bracketing(string_of_brackets: str) -> bool:
    def qwevztf(rsdpq: int, cixuh: int) -> bool:
        if cixuh == 0:
            return rsdpq == 0
        if rsdpq < 0:
            return False
        zmxkor = rsdpq + 1 if string_of_brackets[len(string_of_brackets) - cixuh] == "(" else rsdpq - 1
        return qwevztf(zmxkor, cixuh - 1)

    return qwevztf(0, len(string_of_brackets))