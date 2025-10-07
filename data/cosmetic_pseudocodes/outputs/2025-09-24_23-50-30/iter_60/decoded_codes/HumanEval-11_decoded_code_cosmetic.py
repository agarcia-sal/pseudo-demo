from typing import Iterator, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_r: str, character_s: str) -> str:
        # Return '0' if characters are equal, else '1'
        if character_s == character_r:
            return '0'
        return '1'

    def accumulate(result_m: str, inputs_n: Iterator[Tuple[str, str]]) -> str:
        try:
            local_o = next(inputs_n)
        except StopIteration:
            return result_m
        result_m += xor(local_o[0], local_o[1])
        return accumulate(result_m, inputs_n)

    return accumulate("", iter(zip(string_a, string_b)))