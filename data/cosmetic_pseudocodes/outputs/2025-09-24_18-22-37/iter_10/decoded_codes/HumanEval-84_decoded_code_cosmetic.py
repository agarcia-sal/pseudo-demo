def solve(integer_N: int) -> str:
    temporary_sum: int = 0
    string_version: str = str(integer_N)
    index_position: int = 0

    while index_position < len(string_version):
        character_value: str = string_version[index_position]
        intermediate_digit: int = int(character_value)
        temporary_sum += intermediate_digit
        index_position += 1

    binary_full_string: str = bin(temporary_sum)
    final_binary_string: str = binary_full_string[2:]
    return final_binary_string