def solve(value_X: int) -> str:
    accumulator_Y: int = 0
    text_Z: str = str(value_X)
    cursor_W: int = 1
    while cursor_W <= len(text_Z):
        symbol_V: str = text_Z[cursor_W - 1]  # zero-based indexing adjustment
        digit_U: int = int(symbol_V)
        accumulator_Y += digit_U
        cursor_W += 1
    full_binary_S: str = bin(accumulator_Y)
    result_T: str = full_binary_S[2:]  # substring from index 3 (1-based) means index 2 (0-based)
    return result_T