def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    length_text = len(text)
    index = 0
    while index < length_text:
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
            result += s
        index += 1
    return result