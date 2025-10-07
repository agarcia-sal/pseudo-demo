def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for index in range(len(text)):
        s = text[index]
        lower_s = s.lower()
        is_vowel = False
        for v_index in range(len(vowels)):
            if lower_s == vowels[v_index]:
                is_vowel = True
                break
        if not is_vowel:
            result += s
    return result