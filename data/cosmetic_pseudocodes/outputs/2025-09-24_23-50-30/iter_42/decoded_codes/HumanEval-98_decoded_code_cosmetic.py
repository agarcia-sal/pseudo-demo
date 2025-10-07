from typing import Callable

def count_upper(string_input: str) -> int:
    count_result: int = 0

    def loop_iter(k: int) -> int:
        nonlocal count_result
        if k >= len(string_input):
            return k
        if string_input[k] in {"A", "E", "I", "O", "U"}:
            count_result += 1
        return loop_iter(k + 2)

    loop_iter(0)
    return count_result