def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ''
    vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    index = len(word) - 2
    while index > 0:
        current_char = word[index]
        next_char = word[index + 1]
        prev_char = word[index - 1]

        current_char_in_vowels = current_char in vowels
        if current_char_in_vowels:
            next_char_in_vowels = next_char in vowels
            prev_char_in_vowels = prev_char in vowels
            if not next_char_in_vowels and not prev_char_in_vowels:
                return current_char
        index -= 1
    return ''