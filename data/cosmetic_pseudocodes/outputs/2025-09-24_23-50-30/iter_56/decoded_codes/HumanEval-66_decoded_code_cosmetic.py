def digitSum(character_sequence: str) -> int:
    if character_sequence == "":
        return 0
    accumulator: int = 0
    position: int = 0
    length: int = len(character_sequence)
    while position < length:
        current_char: str = character_sequence[position]
        is_upper: bool = 'A' <= current_char <= 'Z'
        char_value: int = ord(current_char) if is_upper else 0
        accumulator += char_value
        position += 1
    return accumulator