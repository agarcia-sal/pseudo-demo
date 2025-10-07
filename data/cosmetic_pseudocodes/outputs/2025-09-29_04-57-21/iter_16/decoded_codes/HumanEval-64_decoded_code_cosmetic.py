def vowels_count(string_input: str) -> int:
    vowels = "aeiouAEIOU"
    count_vowels = 0
    iterator = 0
    while iterator < len(string_input):
        if string_input[iterator] in vowels:
            count_vowels += 1
        iterator += 1

    if not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        count_vowels += 1

    return count_vowels