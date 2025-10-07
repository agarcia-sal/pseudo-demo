def vowels_count(s) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in vowels:
            n_vowels += 1
        i += 1
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels