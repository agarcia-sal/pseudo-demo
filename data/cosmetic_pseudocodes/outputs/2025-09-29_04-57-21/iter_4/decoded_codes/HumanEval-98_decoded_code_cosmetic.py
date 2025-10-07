def count_upper(string_input: str) -> int:
    uppercase_vowels = "AEIOU"
    accumulator = 0
    position = 0

    while position < len(string_input):
        current_char = string_input[position]
        if current_char in uppercase_vowels:
            accumulator += 1
        position += 2

    return accumulator