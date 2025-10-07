def solve(parameter_P: object) -> str:
    accumulator_X: int = 0
    text_Q: str = str(parameter_P)
    iterator_Z: int = 0
    while iterator_Z < len(text_Q):
        char_M: str = text_Q[iterator_Z]
        numeric_R: int = int(char_M)
        accumulator_X += numeric_R
        iterator_Z += 1
    raw_binary_S: str = bin(accumulator_X)
    result_T: str = raw_binary_S[2:]
    return result_T