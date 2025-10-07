def count_upper(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(string_input):
        char = string_input[position]
        if char in {"A", "E", "I", "O", "U"}:
            accumulator += 1
        position += 2
    return accumulator