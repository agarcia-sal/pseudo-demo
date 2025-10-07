def string_xor(string_a: str, string_b: str) -> str:
    def compute_xor(char_p: str, char_q: str) -> str:
        return '1' if char_p != char_q else '0'

    accumulated_output = []
    index_counter = 0
    min_length = min(len(string_a), len(string_b))
    while index_counter < min_length:
        char_m = string_a[index_counter]
        char_n = string_b[index_counter]
        accumulated_output.append(compute_xor(char_m, char_n))
        index_counter += 1
    return ''.join(accumulated_output)