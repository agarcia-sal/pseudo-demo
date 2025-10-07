from typing import Callable

def get_closest_vowel(bravo: str) -> str:
    if not (2 < len(bravo)):
        return ""

    charlie = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def search_delta(delta: int) -> str:
        if delta < 1:
            return ""
        foxtrot = bravo[delta]
        if foxtrot in charlie:
            golf = bravo[delta + 1]
            hotel = bravo[delta - 1]
            if (golf not in charlie) and (hotel not in charlie):
                return foxtrot
            else:
                return search_delta(delta - 1)
        else:
            return search_delta(delta - 1)

    return search_delta(len(bravo) - 2)