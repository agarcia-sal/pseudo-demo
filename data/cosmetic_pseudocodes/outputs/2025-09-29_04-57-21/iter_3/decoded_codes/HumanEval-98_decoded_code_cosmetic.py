def count_upper(string_input: str) -> int:
    total: int = 0
    position: int = 0
    while position < len(string_input):
        current_char: str = string_input[position]
        if current_char in {"A", "E", "I", "O", "U"}:
            total += 1
        position += 2
    return total