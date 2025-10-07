def remove_vowels(text) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_chars = []
    index = 0
    while index < len(text):
        s = text[index]
        s_lower = s.lower()
        is_vowel = False
        v_index = 0
        while v_index < len(vowels):
            if s_lower == vowels[v_index]:
                is_vowel = True
                break
            v_index += 1
        if not is_vowel:
            result_chars.append(s)
        index += 1
    result_string = ""
    r_index = 0
    while r_index < len(result_chars):
        result_string += result_chars[r_index]
        r_index += 1
    return result_string