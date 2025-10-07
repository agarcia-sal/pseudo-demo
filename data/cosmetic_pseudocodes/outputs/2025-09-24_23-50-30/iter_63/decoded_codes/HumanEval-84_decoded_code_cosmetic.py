def solve(integer_N: int) -> str:
    result_accumulator: int = 0
    for char_element in str(integer_N):
        result_accumulator += int(char_element)
    binary_str: str = bin(result_accumulator)[2:]
    return binary_str