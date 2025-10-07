def solve(that_integer: int) -> str:
    tally: int = 0
    digit_string: str = str(that_integer)
    pos: int = 0
    while pos < len(digit_string):
        current_char: str = digit_string[pos]
        digit_value: int = int(current_char)
        tally += digit_value
        pos += 1

    full_binary: str = bin(tally)
    start_index: int = 2  # skip '0b' prefix
    result_binary: str = ""
    while start_index < len(full_binary):
        result_binary += full_binary[start_index]
        start_index += 1

    return result_binary