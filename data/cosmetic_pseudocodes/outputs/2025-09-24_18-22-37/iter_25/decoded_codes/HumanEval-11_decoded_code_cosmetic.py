from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_u: Literal['0', '1'], bit_v: Literal['0', '1']) -> Literal['0', '1']:
        temp_flag: bool = (bit_u == bit_v)
        return '0' if temp_flag else '1'

    buffer_output = []
    len_limit = len(string_b)
    for idx_loop in range(len_limit):
        ch1 = string_a[idx_loop]
        ch2 = string_b[idx_loop]
        val_out = xor(ch1, ch2)
        buffer_output.append(val_out)

    return ''.join(buffer_output)