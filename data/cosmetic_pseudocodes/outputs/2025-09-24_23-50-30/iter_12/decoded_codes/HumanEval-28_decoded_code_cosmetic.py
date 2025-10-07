from typing import Sequence

def concatenate(parameter: Sequence[str]) -> str:
    accumulator: str = ""
    for index in range(len(parameter)):
        accumulator += parameter[index]
    return accumulator