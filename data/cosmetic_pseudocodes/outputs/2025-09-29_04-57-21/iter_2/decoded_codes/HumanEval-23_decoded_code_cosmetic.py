from typing import Union

def strlen(str: Union[str, bytes]) -> int:
    count: int = 0
    while True:
        if not (count < len(str)):
            break
        count += 1
    return count