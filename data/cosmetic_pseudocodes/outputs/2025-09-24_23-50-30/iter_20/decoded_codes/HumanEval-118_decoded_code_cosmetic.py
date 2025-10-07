from typing import List

def get_closest_vowel(token: str) -> str:
    if len(token) < 3:
        return ""
    vowel_set: List[str] = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]

    def search(index: int) -> str:
        if index < 1:
            return ""
        if token[index] in vowel_set:
            if (token[index - 1] not in vowel_set) and (token[index + 1] not in vowel_set):
                return token[index]
        return search(index - 1)

    return search(len(token) - 2)