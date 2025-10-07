from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def helper_function(param_m: str, param_n: str) -> str:
        return '1' if param_m != param_n else '0'

    def loop_process(index_p: int, accumulator_q: str) -> str:
        if index_p >= min(len(string_a), len(string_b)):
            return accumulator_q
        current_char1 = string_a[index_p]
        current_char2 = string_b[index_p]
        updated_accumulator = accumulator_q + helper_function(current_char1, current_char2)
        return loop_process(index_p + 1, updated_accumulator)

    return loop_process(0, "")