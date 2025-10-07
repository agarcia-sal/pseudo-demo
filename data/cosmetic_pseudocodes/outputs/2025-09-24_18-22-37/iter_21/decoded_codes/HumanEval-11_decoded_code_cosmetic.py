def string_xor(param_alpha: str, param_beta: str) -> str:
    def xor(inner_ch1: str, inner_ch2: str) -> str:
        if inner_ch1 == inner_ch2:
            return '0'
        else:
            return '1'

    output_accumulator = ""
    index_tracker = 0
    length = min(len(param_alpha), len(param_beta))
    while index_tracker < length:
        ch1 = param_alpha[index_tracker]
        ch2 = param_beta[index_tracker]
        xor_res = xor(ch1, ch2)
        output_accumulator += xor_res
        index_tracker += 1

    return output_accumulator