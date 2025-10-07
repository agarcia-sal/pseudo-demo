from typing import Union

def strlen(str_input: Union[str, bytes]) -> int:
    count: int = 0
    length: int = len(str_input)
    while count < length:
        count += 1
    return count