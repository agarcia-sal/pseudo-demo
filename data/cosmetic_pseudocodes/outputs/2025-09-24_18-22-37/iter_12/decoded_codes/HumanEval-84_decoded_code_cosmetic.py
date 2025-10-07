def solve(parameter_x: int) -> str:
    accumulator_y: int = 0
    string_z: str = str(parameter_x)
    index_w: int = 0
    while index_w < len(string_z):
        temp_v: str = string_z[index_w]
        digit_u: int = int(temp_v)
        accumulator_y += digit_u
        index_w += 1
    prefix_removed_binary: str = bin(accumulator_y)[2:]
    return prefix_removed_binary