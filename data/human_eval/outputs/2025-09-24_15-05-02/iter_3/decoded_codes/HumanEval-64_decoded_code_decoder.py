def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    number_of_vowels = 0

    for character in s:
        if character in vowels:
            number_of_vowels += 1

    if s and s[-1] in ('y', 'Y'):
        number_of_vowels += 1

    return number_of_vowels