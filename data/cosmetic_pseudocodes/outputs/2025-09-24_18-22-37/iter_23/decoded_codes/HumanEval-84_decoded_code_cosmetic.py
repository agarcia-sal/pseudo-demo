def solve(parameter_M: int) -> str:
    accumulator: int = 0
    string_version: str = str(parameter_M)
    position: int = 0
    while position < len(string_version):
        current_char: str = string_version[position]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        position += 1

    full_binary_string: str = bin(accumulator)
    # Extract substring excluding the '0b' prefix
    binary_output: str = full_binary_string[2:]
    return binary_output