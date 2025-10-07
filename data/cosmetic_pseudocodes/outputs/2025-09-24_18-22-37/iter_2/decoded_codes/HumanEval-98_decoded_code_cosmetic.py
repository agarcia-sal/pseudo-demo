def count_upper(str_input: str) -> int:
    total: int = 0
    pos: int = 0
    while pos < len(str_input):
        if str_input[pos] in {"A", "E", "I", "O", "U"}:
            total += 1
        pos += 2
    return total