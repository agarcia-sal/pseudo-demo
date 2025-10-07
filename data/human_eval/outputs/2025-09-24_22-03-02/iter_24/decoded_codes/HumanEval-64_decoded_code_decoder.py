def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            n_vowels += 1
        i += 1
    if len(s) > 0 and (s[len(s) - 1] == 'y' or s[len(s) - 1] == 'Y'):
        n_vowels += 1
    return n_vowels