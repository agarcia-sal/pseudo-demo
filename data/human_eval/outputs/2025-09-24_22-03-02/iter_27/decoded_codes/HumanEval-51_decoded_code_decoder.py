def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    index = 0
    while index < len(text):
        s = text[index]
        lower_s = s.lower()
        is_vowel = False
        v_index = 0
        while v_index < len(vowels):
            if lower_s == vowels[v_index]:
                is_vowel = True
                break
            v_index += 1
        if is_vowel == False:
            result += s
        index += 1
    return result