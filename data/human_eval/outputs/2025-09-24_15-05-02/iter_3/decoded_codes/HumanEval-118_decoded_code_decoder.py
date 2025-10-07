def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    # Iterate from second last character down to second character
    for index in range(len(word) - 2, 0, -1):
        if word[index] in vowels:
            if word[index + 1] not in vowels and word[index - 1] not in vowels:
                return word[index]

    return ""