def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for char in s if char in vowels)
    if s and s[-1] in {'y', 'Y'}:
        n_vowels += 1
    return n_vowels