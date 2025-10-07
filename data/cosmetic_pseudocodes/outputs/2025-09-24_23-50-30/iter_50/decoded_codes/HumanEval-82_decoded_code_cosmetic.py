from typing import Any


def prime_length(input_string: str) -> bool:
    class ResultHolder:
        def __init__(self) -> None:
            self.value: bool = False

    def check_divisor(current_divisor: int, max_divisor: int, str_len: int, result_ref: ResultHolder) -> None:
        if current_divisor > max_divisor:
            result_ref.value = True
            return
        if str_len % current_divisor == 0:
            result_ref.value = False
            return
        check_divisor(current_divisor + 1, max_divisor, str_len, result_ref)

    length_counter = 0
    for _ in input_string:
        length_counter += 1

    if length_counter < 2:
        return False

    result_holder = ResultHolder()
    check_divisor(2, length_counter - 1, length_counter, result_holder)
    return result_holder.value