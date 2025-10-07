def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    number_of_vowels = sum(ch in vowels for ch in s)
    if s and s[-1] in ('y', 'Y'):
        number_of_vowels += 1
    return number_of_vowels