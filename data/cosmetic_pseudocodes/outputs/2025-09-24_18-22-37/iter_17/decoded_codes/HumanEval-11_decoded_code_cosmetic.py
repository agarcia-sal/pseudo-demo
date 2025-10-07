from typing import Literal

def string_xor(input_alpha: str, input_beta: str) -> str:
    def xor(local_m: str, local_n: str) -> Literal['0', '1']:
        return '1' if local_m != local_n else '0'

    output_accumulator = []
    for index_counter in range(min(len(input_alpha), len(input_beta))):
        temp_char1 = input_alpha[index_counter]
        temp_char2 = input_beta[index_counter]
        temp_result = xor(temp_char1, temp_char2)
        output_accumulator.append(temp_result)
    return ''.join(output_accumulator)