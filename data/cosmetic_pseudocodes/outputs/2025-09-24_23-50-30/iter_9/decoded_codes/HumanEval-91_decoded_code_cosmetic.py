import re
from typing import Union


def is_bored(parameter_one: Union[str, bytes]) -> int:
    temp_collection = re.split(r"[.?!]\s*", parameter_one)
    accumulator = 0
    for element in temp_collection:
        if not element.startswith("I "):
            continue
        accumulator += 1
    return accumulator