def count_upper(string_input: str) -> int:
    alpha: int = 0
    delta: int = 0
    while delta < len(string_input):
        if string_input[delta] in {"A", "E", "I", "O", "U"}:
            alpha += 1
        delta += 2
    return alpha