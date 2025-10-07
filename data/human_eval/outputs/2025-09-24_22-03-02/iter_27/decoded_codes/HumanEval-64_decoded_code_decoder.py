def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    index = 0
    while index < len(s):
        c = s[index]
        found_vowel = False
        vowel_index = 0
        while vowel_index < len(vowels):
            if c == vowels[vowel_index]:
                found_vowel = True
                break
            vowel_index += 1
        if found_vowel == True:
            n_vowels += 1
        index += 1
    if len(s) > 0:
        last_char = s[len(s) - 1]
        if last_char == 'y' or last_char == 'Y':
            n_vowels += 1
    return n_vowels