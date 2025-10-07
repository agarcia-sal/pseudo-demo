def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    index = 0
    while index < len(s):
        if s[index] in vowels:
            n_vowels += 1
        index += 1
    if s and s[-1] in ("y", "Y"):
        n_vowels += 1
    return n_vowels