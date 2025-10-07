def vowels_count(string_input: str) -> int:
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in string_input if char in vowels)
    if string_input and string_input[-1] in {'y', 'Y'}:
        vowel_count += 1
    return vowel_count