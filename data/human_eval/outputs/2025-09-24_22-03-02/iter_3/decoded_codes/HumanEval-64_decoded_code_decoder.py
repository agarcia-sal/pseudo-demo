def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s.endswith(('y', 'Y')):
        n_vowels += 1
    return n_vowels