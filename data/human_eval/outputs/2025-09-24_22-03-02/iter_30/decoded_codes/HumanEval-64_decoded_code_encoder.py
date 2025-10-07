def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    length_s = len(s)
    index = 0
    while index < length_s:
        c = s[index]
        found_vowel = False
        v_index = 0
        vowels_length = len(vowels)
        while v_index < vowels_length and not found_vowel:
            if c == vowels[v_index]:
                found_vowel = True
            v_index += 1
        if found_vowel:
            n_vowels += 1
        index += 1
    if length_s > 0:
        last_char = s[length_s - 1]
        if last_char == "y" or last_char == "Y":
            n_vowels += 1
    return n_vowels