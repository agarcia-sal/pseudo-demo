def vowels_count(input_string: str) -> int:
    vowel_characters: str = "AEIOUaeiou"
    count_vowels: int = 0
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        if current_char in vowel_characters:
            count_vowels += 1
        position += 1
    if input_string and input_string[-1] in ('y', 'Y'):
        count_vowels += 1
    return count_vowels