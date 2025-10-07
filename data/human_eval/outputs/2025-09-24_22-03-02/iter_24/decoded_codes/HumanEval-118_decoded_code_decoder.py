def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    index_start = len(word) - 2
    index_end = 1
    for i in range(index_start, index_end - 1, -1):
        current_char = word[i]
        if current_char in vowels:
            next_char = word[i + 1]
            prev_char = word[i - 1]
            if next_char not in vowels and prev_char not in vowels:
                return current_char
    return ""