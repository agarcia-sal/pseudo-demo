def string_xor(param_m: str, param_n: str) -> str:
    def xor(param_p: str, param_q: str) -> str:
        if param_p == param_q:
            return '0'
        else:
            return '1'

    accumulator: str = ""
    idx: int = 0
    length: int = len(param_m)
    while idx < length:
        char_1: str = param_m[idx]
        char_2: str = param_n[idx]
        temp_res: str = xor(char_1, char_2)
        accumulator += temp_res
        idx += 1
    return accumulator