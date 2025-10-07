from typing import Iterable

def strlen(parameter_one: Iterable) -> int:
    output_variable: int = 0
    for _ in parameter_one:
        output_variable += 1
    return output_variable