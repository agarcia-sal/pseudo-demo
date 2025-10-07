def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for index in range(len(text)):
        current_char = text[index]
        lower_char = current_char.lower()
        is_vowel = False
        for vowel_index in range(len(vowels)):
            if lower_char == vowels[vowel_index]:
                is_vowel = True
                break
        if not is_vowel:
            result += current_char
    return result