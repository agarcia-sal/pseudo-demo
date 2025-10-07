from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def recursiveloop(current_counter: int) -> int:
        if current_counter < integer_n:
            return (recursiveloop(current_counter + 1) * 2) % integer_p
        else:
            return 1

    result_accumulator: int = recursiveloop(0)
    return result_accumulator