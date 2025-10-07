def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_1: str, character_2: str) -> str:
        return '0' if character_1 == character_2 else '1'

    accumulated_result = []
    max_length = len(string_a)
    for index_counter in range(max_length):
        char_first = string_a[index_counter]
        char_second = string_b[index_counter]
        accumulated_result.append(xor(char_first, char_second))
    return ''.join(accumulated_result)