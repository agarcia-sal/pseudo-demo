def string_xor(param_alpha: str, param_beta: str) -> str:
    def xor_func(param_p: str, param_q: str) -> str:
        if param_p == param_q:
            return '0'
        return '1'

    temp_result: str = ''
    idx_counter: int = 0

    while idx_counter < len(param_alpha) and idx_counter < len(param_beta):
        char_one = param_alpha[idx_counter]
        char_two = param_beta[idx_counter]
        temp_result += xor_func(char_one, char_two)
        idx_counter += 1

    return temp_result