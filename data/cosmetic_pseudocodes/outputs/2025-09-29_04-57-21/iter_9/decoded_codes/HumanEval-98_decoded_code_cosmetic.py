def count_upper(string_input: str) -> int:
    uppercase_counter: int = 0
    position: int = 0

    while position < len(string_input):
        current_char: str = string_input[position]

        if current_char in {"A", "E", "I", "O", "U"}:
            uppercase_counter += 1

        position += 2

    return uppercase_counter