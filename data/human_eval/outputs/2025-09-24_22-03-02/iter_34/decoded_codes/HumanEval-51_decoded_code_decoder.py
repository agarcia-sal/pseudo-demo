def remove_vowels(text) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    index = 0
    while index < len(text):
        s = text[index]
        s_lower = s.lower()
        is_vowel = False
        vowel_index = 0
        while vowel_index < len(vowels):
            if s_lower == vowels[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if not is_vowel:
            result_characters.append(s)
        index += 1
    result_string = ''.join(result_characters)
    return result_string