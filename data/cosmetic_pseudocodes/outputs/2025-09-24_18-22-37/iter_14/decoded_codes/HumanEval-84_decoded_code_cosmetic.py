def solve(integer_U: int) -> str:
    accumulator_Z: int = 0
    string_V: str = str(integer_U)
    index_P: int = 0
    while index_P < len(string_V):
        temp_W: str = string_V[index_P]
        temp_Q: int = int(temp_W)
        accumulator_Z += temp_Q
        index_P += 1
    binary_S: str = bin(accumulator_Z)  # bin returns strings starting with '0b'
    result_M: str = binary_S[3:]  # substring from 3rd index (0-based) to end
    return result_M