def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i + 1] not in vowels and word[i - 1] not in vowels:
                return word[i]
    return ""