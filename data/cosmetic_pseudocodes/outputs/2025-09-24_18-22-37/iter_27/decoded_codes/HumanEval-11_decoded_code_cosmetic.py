def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        return '1' if character_p != character_q else '0'

    accumulated_result = []
    iterator_index = 0
    length = min(len(string_a), len(string_b))
    while iterator_index < length:
        first_char = string_a[iterator_index]
        second_char = string_b[iterator_index]
        computed_char = xor(first_char, second_char)
        accumulated_result.append(computed_char)
        iterator_index += 1
    return ''.join(accumulated_result)