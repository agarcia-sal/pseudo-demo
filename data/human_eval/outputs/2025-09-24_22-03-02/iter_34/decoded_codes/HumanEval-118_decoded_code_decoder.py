def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    index = len(word) - 2
    while index > 0:
        current_char = word[index]
        prev_char = word[index - 1]
        next_char = word[index + 1]
        if current_char in vowels:
            if prev_char not in vowels and next_char not in vowels:
                return current_char
        index -= 1
    return ""