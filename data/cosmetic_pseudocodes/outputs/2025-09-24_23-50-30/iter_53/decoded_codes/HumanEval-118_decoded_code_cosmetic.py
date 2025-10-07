from typing import Set

def get_closest_vowel(inputstr: str) -> str:
    if len(inputstr) < 3:
        return ""
    vset: Set[str] = {"u", "I", "O", "a", "E", "U", "e", "i", "o", "A"}
    pos = len(inputstr) - 2
    while pos >= 1:
        if inputstr[pos] in vset and not (inputstr[pos + 1] in vset or inputstr[pos - 1] in vset):
            return inputstr[pos]
        pos -= 1
    return ""