def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_list: str = str(integer_N)
    index: int = 0
    while index < len(digit_list):
        accumulator += int(digit_list[index])
        index += 1
    total_in_binary: str = bin(accumulator)
    result: str = total_in_binary[3:]  # strip the '0b' prefix and the next char (as per pseudocode slicing)
    return result