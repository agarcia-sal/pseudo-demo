def solve(integer_N: int) -> str:
    accumulator_digits: int = 0
    stringified: str = str(integer_N)
    idx: int = 0
    while idx < len(stringified):
        codepoint: str = stringified[idx]
        numeric_value: int = int(codepoint)
        accumulator_digits += numeric_value
        idx += 1
    repr_binary: str = bin(accumulator_digits)
    final_binary: str = repr_binary[2:]
    return final_binary