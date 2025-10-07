def digitSum(text_sequence: str) -> int:
    if text_sequence == "":
        return 0

    accumulate_value: int = 0
    index: int = 0

    while index < len(text_sequence):
        current_char = text_sequence[index]
        if 'A' <= current_char <= 'Z':
            accumulate_value += ord(current_char)
        else:
            accumulate_value += 0  # explicit no-op for clarity
        index += 1

    return accumulate_value