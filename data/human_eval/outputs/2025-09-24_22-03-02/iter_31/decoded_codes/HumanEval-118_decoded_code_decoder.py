def get_closest_vowel(word):
    if len(word) < 3:
        return ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    index = len(word) - 2
    while index > 0:
        current_char = word[index]
        if current_char in vowels:
            right_char = word[index + 1]
            left_char = word[index - 1]
            if right_char not in vowels and left_char not in vowels:
                return current_char
        index -= 1
    return ""