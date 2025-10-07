def count_upper(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0
    vowels = {"A", "E", "I", "O", "U"}
    while position < len(string_input):
        current_char = string_input[position]
        if current_char not in vowels:
            position += 2
            continue
        accumulator += 1
        position += 2
    return accumulator