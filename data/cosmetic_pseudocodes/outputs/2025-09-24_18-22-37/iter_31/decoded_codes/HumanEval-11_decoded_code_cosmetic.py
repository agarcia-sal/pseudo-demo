from typing import Iterator, Tuple

def string_xor(input_str_m: str, input_str_n: str) -> str:
    def xor(bit_p: str, bit_q: str) -> str:
        if bit_p == bit_q:
            return '0'
        else:
            return '1'

    zipped_pairs: Iterator[Tuple[str, str]] = zip(input_str_m, input_str_n)
    aggregated_result = ''.join(
        xor(first_bit, second_bit) for first_bit, second_bit in zipped_pairs
    )
    return aggregated_result