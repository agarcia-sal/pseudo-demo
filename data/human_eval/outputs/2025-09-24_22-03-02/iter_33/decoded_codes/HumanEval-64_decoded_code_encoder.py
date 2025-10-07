def vowels_count(s) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
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
    last_char = s[len(s) - 1]
    if last_char == 'y' or last_char == 'Y':
        n_vowels += 1
    return n_vowels