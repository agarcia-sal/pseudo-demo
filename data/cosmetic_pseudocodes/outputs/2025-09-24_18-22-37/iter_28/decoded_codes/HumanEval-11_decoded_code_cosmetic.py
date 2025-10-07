def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_one: str, char_two: str) -> str:
        if char_one == char_two:
            return '0'
        return '1'

    buffer_string = []
    idx_counter = 0
    max_len = min(len(string_a), len(string_b))
    while idx_counter < max_len:
        first_char = string_a[idx_counter]
        second_char = string_b[idx_counter]
        temp_char = xor(first_char, second_char)
        buffer_string.append(temp_char)
        idx_counter += 1

    return ''.join(buffer_string)