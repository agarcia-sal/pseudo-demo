def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_iter: str = str(integer_N)
    index_tracker: int = 0
    while index_tracker < len(digit_iter):
        current_symbol: str = digit_iter[index_tracker]
        accumulator += int(current_symbol)
        index_tracker += 1
    full_binary_str: str = bin(accumulator)
    trimmed_binary: str = full_binary_str[2:]
    return trimmed_binary