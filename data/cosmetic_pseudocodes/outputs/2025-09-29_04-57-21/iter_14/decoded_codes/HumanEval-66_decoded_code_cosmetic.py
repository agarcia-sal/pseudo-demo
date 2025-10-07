def digitSum(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0

    while position < len(string_input):
        current_char: str = string_input[position]

        # Check if current_char is not uppercase or not lowercase
        if not (current_char == current_char.upper()) or not (current_char == current_char.lower()):
            accumulator += ord(current_char)

        position += 1

    return accumulator