def vowels_count(s):
    vowels = "aeiouAEIOU"
    n = sum(1 for c in s if c in vowels)
    if s[-1] in ['y', 'Y']:
        n += 1
    return n