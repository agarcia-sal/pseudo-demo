def vowels_count(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    n_vowels = 0
    length_s = len(s)
    index = 0
    while index < length_s:
        c = s[index]
        is_vowel = False
        vowel_index = 0
        vowels_length = len(vowels)
        while vowel_index < vowels_length:
            # Since vowels is a set, to preserve logic convert to list for index access
            vowel_list = list(vowels)
            if c == vowel_list[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if is_vowel:
            n_vowels += 1
        index += 1
    last_index = length_s - 1
    if last_index >= 0:
        last_char = s[last_index]
        if last_char == 'y' or last_char == 'Y':
            n_vowels += 1
    return n_vowels