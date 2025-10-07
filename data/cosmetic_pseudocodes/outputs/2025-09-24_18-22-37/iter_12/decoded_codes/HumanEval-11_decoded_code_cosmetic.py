def string_xor(param_m: str, param_n: str) -> str:
    def xor(param_p: str, param_q: str) -> str:
        return '1' if param_p != param_q else '0'

    output_str = []
    max_len = len(param_m)
    for index_counter in range(max_len):
        temp_char_1 = param_m[index_counter]
        temp_char_2 = param_n[index_counter]
        temp_result = xor(temp_char_1, temp_char_2)
        output_str.append(temp_result)
    return ''.join(output_str)