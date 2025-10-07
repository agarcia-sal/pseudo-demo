def count_upper(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0
    vowels = "AEIOU"
    while position < len(string_input):
        if string_input[position] in vowels:
            accumulator += 1
        position += 2
    return accumulator