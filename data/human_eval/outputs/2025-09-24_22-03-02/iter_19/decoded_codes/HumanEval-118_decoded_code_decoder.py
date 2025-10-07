from typing import List

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    index = len(word) - 2
    while index > 0:
        if word[index] in vowels:
            if word[index + 1] not in vowels and word[index - 1] not in vowels:
                return word[index]
        index -= 1
    return ""