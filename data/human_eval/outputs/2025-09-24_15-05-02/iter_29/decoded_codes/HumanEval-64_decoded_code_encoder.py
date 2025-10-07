def vowels_count(string_input: str) -> int:
    vowels_characters = "aeiouAEIOU"
    number_of_vowels = sum(character in vowels_characters for character in string_input)
    if string_input and string_input[-1] in ('y', 'Y'):
        number_of_vowels += 1
    return number_of_vowels