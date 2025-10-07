from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    result_accumulator: str = ""

    def rec_process(n: int, base: int, acc: str) -> str:
        if not (n > 0):
            return acc
        digit_val: int = n - base * (n // base)  # n % base could be used but kept as per pseudocode
        new_acc: str = str(digit_val) + acc
        return rec_process(n // base, base, new_acc)

    return rec_process(integer_x, integer_base, result_accumulator)