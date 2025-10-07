def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for character in s if character in vowels)
    if s.endswith(('y', 'Y')):
        n_vowels += 1
    return n_vowels