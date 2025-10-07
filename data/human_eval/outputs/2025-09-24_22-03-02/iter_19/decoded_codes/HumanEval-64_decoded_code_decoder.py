def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    i = 0
    while i < len(s):
        c = s[i]
        j = 0
        is_vowel = False
        while j < len(vowels):
            if c == vowels[j]:
                is_vowel = True
                break
            j += 1
        if is_vowel:
            n_vowels += 1
        i += 1
    last_index = len(s) - 1
    if last_index >= 0:
        last_char = s[last_index]
        if last_char == "y" or last_char == "Y":
            n_vowels += 1
    return n_vowels