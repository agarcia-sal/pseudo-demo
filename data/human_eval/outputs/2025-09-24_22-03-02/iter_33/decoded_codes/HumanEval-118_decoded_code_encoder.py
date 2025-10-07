def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    index = len(word) - 2

    while index > 0:
        current_char = word[index]
        next_char = word[index + 1]
        prev_char = word[index - 1]

        is_current_char_vowel = current_char in vowels
        is_next_char_vowel = next_char in vowels
        is_prev_char_vowel = prev_char in vowels

        if is_current_char_vowel and not is_next_char_vowel and not is_prev_char_vowel:
            return current_char

        index -= 1

    return ""