def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    index = 0
    while index < len(s):
        c = s[index]
        is_vowel = False
        v_index = 0
        while v_index < len(vowels):
            if c == vowels[v_index]:
                is_vowel = True
                break
            v_index += 1
        if is_vowel:
            n_vowels += 1
        index += 1
    if len(s) > 0:
        last_char = s[len(s) - 1]
        if last_char == "y" or last_char == "Y":
            n_vowels += 1
    return n_vowels