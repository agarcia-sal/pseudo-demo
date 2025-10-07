def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_list = [""]
    for index in range(len(text)):
        s = text[index]
        s_lower = s.lower()
        is_vowel = False
        for v_index in range(len(vowels)):
            if s_lower == vowels[v_index]:
                is_vowel = True
        if not is_vowel:
            result_list.append(s)
    result_string = ""
    for r_index in range(len(result_list)):
        result_string = result_string + result_list[r_index]
    return result_string