def digitSum(string_input: str) -> int:
    accum: int = 0
    for current_char in string_input:
        if 'A' <= current_char <= 'Z':
            accum += ord(current_char)
    return accum