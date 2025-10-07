def solve(parameter_P: int) -> str:
    accumulator_Q: int = 0
    parameter_str: str = str(parameter_P)
    for index_R in range(1, len(parameter_str) + 1):
        temp_S: str = parameter_str[index_R - 1]  # adjusting 1-based to 0-based indexing
        value_T: int = int(temp_S)
        accumulator_Q += value_T
    temp_U: str = bin(accumulator_Q)
    result_V: str = temp_U[2:]  # substring from position 3 (1-based), index 2 (0-based) to end
    return result_V