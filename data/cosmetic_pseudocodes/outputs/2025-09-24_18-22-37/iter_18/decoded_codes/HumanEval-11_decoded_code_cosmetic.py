from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(inner_p: str, inner_q: str) -> str:
        return '1' if inner_p != inner_q else '0'

    aggregate_output = []
    iterator_m = 0
    length = len(string_a)
    while True:
        if iterator_m >= length:
            break
        val_1 = string_a[iterator_m]
        val_2 = string_b[iterator_m]
        temp_res = xor(val_1, val_2)
        aggregate_output.append(temp_res)
        iterator_m += 1

    return ''.join(aggregate_output)