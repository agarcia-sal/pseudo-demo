def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    index = 0
    while index < len(text):
        current_char = text[index]
        lower_char = current_char.lower()
        is_vowel = False
        vowel_index = 0
        while vowel_index < len(vowels):
            if lower_char == vowels[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if not is_vowel:
            result += current_char
        index += 1
    return result