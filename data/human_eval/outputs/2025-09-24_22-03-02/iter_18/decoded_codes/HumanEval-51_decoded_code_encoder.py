def remove_vowels(text):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    index = 0
    while index < len(text):
        s = text[index]
        lower_s = s.lower()
        contains_vowel = False
        vowel_index = 0
        while vowel_index < len(vowels):
            if lower_s == vowels[vowel_index]:
                contains_vowel = True
                break
            vowel_index += 1
        if not contains_vowel:
            result += s
        index += 1
    return result