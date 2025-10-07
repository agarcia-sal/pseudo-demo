def count_upper(param_text: str) -> int:
    accumulator: int = 0
    pos: int = 0
    length: int = len(param_text)
    while pos < length:
        symbol: str = param_text[pos]
        if symbol in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1  # (1 + 0) simplified to 1
        pos += 2  # (1 + 1) simplified to 2
    return accumulator