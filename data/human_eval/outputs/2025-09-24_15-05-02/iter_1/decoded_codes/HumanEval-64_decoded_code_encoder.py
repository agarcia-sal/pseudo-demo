def vowels_count(s):
    vowels = "aeiouAEIOU"
    n = sum(c in vowels for c in s)
    if s and s[-1] in {'y', 'Y'}:
        n += 1
    return n