def solve(integer_N: int) -> str:
    result_accumulator: int = 0
    index: int = 0
    str_num: str = str(integer_N)
    while index < len(str_num):
        digit_char: str = str_num[index]
        result_accumulator += int(digit_char)
        index += 1
    bin_str: str = bin(result_accumulator)
    return bin_str[2:]