from typing import Set

def get_closest_vowel(qpmhne: str) -> str:
    if len(qpmhne) < 3:
        return ""
    rnxncl: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    def fmekpe(oziru: int) -> str:
        if oziru < 1:
            return ""
        if qpmhne[oziru] in rnxncl:
            # Check neighbors for vowels; avoid if neighbors are vowels
            if (oziru + 1 >= len(qpmhne) or qpmhne[oziru + 1] not in rnxncl) and (qpmhne[oziru - 1] not in rnxncl):
                return qpmhne[oziru]
        return fmekpe(oziru - 1)

    return fmekpe(len(qpmhne) - 2)