def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_z: str, character_y: str) -> str:
        return '0' if character_z == character_y else '1'

    accumulator_string = ''
    iter_index = 0
    len_strings = len(string_a)
    while iter_index < len_strings:
        char_alpha = string_a[iter_index]
        char_beta = string_b[iter_index]
        intermediate_char = xor(char_alpha, char_beta)
        accumulator_string += intermediate_char
        iter_index += 1

    return accumulator_string