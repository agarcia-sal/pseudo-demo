def vowels_count(string_s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for c in string_s:
        if c in vowels:
            n_vowels += 1
    if string_s and string_s[-1] in ('y', 'Y'):
        n_vowels += 1
    return n_vowels