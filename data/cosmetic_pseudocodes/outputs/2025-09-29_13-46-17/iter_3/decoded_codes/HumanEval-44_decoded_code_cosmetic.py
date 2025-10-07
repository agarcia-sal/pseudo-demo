from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    output_string: str = ""

    def recurse(current_number: int) -> None:
        nonlocal output_string
        if current_number <= 0:
            return
        recurse(current_number // integer_base)
        output_string += str(current_number % integer_base)

    recurse(integer_x)
    return output_string