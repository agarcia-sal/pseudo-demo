def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for c in s:
        if c in vowels:
            n_vowels += 1
    if s.endswith('y') or s.endswith('Y'):
        n_vowels += 1
    return n_vowels