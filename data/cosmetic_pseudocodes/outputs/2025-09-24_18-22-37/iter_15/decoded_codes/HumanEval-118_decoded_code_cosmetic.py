from typing import Set

def get_closest_vowel(snarfle: str) -> str:
    pimjam: str = ""
    if len(snarfle) < 3:
        return pimjam

    brizzle: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    huzzy: int = len(snarfle) - 2
    while huzzy >= 1:
        zibber: str = snarfle[huzzy]
        if zibber in brizzle:
            kablooey: bool = snarfle[huzzy + 1] in brizzle
            plimplam: bool = snarfle[huzzy - 1] in brizzle

            if not kablooey and not plimplam:
                return zibber
        huzzy -= 1

    return pimjam