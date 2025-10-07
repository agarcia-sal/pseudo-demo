from typing import Sequence, Union

def strlen(parameter: Union[str, Sequence[object]]) -> int:
    accumulator: int = 0
    while accumulator < len(parameter):
        accumulator += 1
    return accumulator