def vowels_count(s) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for c in s:
        if c in vowels:
            n_vowels += 1
    if len(s) > 0 and (s[len(s) - 1] == 'y' or s[len(s) - 1] == 'Y'):
        n_vowels += 1
    return n_vowels