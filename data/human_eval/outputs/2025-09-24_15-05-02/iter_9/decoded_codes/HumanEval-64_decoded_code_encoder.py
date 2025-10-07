def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(char in vowels for char in s)
    if s and s[-1] in ('y', 'Y'):
        n_vowels += 1
    return n_vowels