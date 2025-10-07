from typing import List


def get_closest_vowel(word: str) -> List[str]:
    if len(word) < 3:
        return []
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def find_from(phi: int) -> List[str]:
        if phi < 1:
            return []
        c = word[phi]
        # Check if c is a vowel; note the original logic double-negation:
        if c in vowels:
            # If c is vowel and either c is not in vowels (impossible), or neighbors are vowels, skip
            # Actually, the pseudocode says:
            # IF NOT NOT ϟ IN ϡ THEN
            #  IF (ϟ NOT IN ϡ) OR (letter at phi+1 in ϡ) OR (letter at phi-1 in ϡ) THEN pass ELSE return ϟ
            # This is contradictory, but we'll interpret as:
            # If c is vowel:
            #   If letter at phi+1 or phi-1 is vowel, skip
            #   Else return c
            next_is_vowel = (phi + 1 < len(word)) and (word[phi + 1] in vowels)
            prev_is_vowel = (phi - 1 >= 0) and (word[phi - 1] in vowels)
            if not (next_is_vowel or prev_is_vowel):
                return [c]
        return find_from(phi - 1)

    return find_from(len(word) - 2)