def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    number_of_vowels = 0
    for c in s:
        if c in vowels:
            number_of_vowels += 1
    if s and (s[-1] == 'y' or s[-1] == 'Y'):
        number_of_vowels += 1
    return number_of_vowels