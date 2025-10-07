def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    i = len(word) - 2
    while i > 0:
        if word[i] in vowels:
            if word[i + 1] not in vowels and word[i - 1] not in vowels:
                return word[i]
        i -= 1
    return ""