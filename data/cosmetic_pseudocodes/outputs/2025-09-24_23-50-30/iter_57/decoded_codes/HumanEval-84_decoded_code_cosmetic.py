def solve(input_num: int) -> str:
    aggregate_value: int = 0
    idx: int = 0
    input_str = str(input_num)
    while idx < len(input_str):
        current_char: str = input_str[idx]
        aggregate_value += int(current_char)
        idx += 1
    full_binary: str = bin(aggregate_value)
    trimmed_binary: str = full_binary[2:-2] if len(full_binary) > 4 else ''
    return trimmed_binary