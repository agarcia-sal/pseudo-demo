def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s and s[-1] in {'y', 'Y'}:
        n_vowels += 1
    return n_vowels