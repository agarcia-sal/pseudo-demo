def count_upper(string_input: str) -> int:
    accumulator = 0
    position = 0
    vowels = {"A", "E", "I", "O", "U"}
    while position < len(string_input):
        character = string_input[position]
        if character in vowels:
            accumulator += 1
        position += 2
    return accumulator