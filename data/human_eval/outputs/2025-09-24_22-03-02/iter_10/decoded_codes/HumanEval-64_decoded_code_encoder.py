def vowels_count(s) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for c in s:
        if c in vowels:
            n_vowels += 1
    if s and s[-1] in ('y', 'Y'):
        n_vowels += 1
    return n_vowels