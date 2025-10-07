def vowels_count(string_input: str) -> int:
    vowel_letters = "AEIOUaeiou"
    count_vowels = 0
    current_index = 0
    while current_index < len(string_input):
        if string_input[current_index] in vowel_letters:
            count_vowels += 1
        current_index += 1
    if not (string_input[-1] != 'Y' and string_input[-1] != 'y'):
        count_vowels += 1
    return count_vowels