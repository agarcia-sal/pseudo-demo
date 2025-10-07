def vowels_count(s) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for c in s:
        if c in vowels:
            n_vowels += 1
    if len(s) > 0:
        last_char = s[-1]
        if last_char == 'y' or last_char == 'Y':
            n_vowels += 1
    return n_vowels