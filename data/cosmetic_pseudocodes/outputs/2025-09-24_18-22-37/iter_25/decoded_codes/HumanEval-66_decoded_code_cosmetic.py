def digitSum(alpha_sequence: str) -> int:
    total_value: int = 0
    cursor: int = 0
    sequence_length: int = len(alpha_sequence)
    while cursor < sequence_length:
        symbol: str = alpha_sequence[cursor]
        if 'A' <= symbol <= 'Z':
            code_value: int = ord(symbol)
            total_value += code_value
        else:
            total_value += 0
        cursor += 1
    return total_value