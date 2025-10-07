def remove_vowels(text):
    vowels_list = ["a", "e", "i", "o", "u"]
    filtered_characters = []
    for index in range(len(text)):
        s = text[index]
        s_lower = s.lower()
        is_vowel = False
        for v_index in range(len(vowels_list)):
            vowel = vowels_list[v_index]
            if s_lower == vowel:
                is_vowel = True
                break
        if not is_vowel:
            filtered_characters.append(s)
    result_string = "".join(filtered_characters)
    return result_string