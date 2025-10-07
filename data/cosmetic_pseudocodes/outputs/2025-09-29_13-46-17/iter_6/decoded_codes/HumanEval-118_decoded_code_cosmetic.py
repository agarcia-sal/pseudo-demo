from typing import Set

def get_closest_vowel(word: str) -> str:
    lenX: int = len(word)
    if lenX < 2:
        return ""

    vowel_set: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def descendPos(pos_acc: int) -> str:
        if pos_acc < 1:
            return ""
        if (word[pos_acc] in vowel_set and
            (pos_acc + 1 >= lenX or word[pos_acc + 1] not in vowel_set) and
            (pos_acc - 1 < 0 or word[pos_acc - 1] not in vowel_set)):
            return word[pos_acc]
        return descendPos(pos_acc - 1)

    return descendPos(lenX - 2)