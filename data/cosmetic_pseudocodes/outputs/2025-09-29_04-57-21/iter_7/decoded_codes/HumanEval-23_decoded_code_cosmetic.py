from typing import Union

def strlen(inputStr: Union[str, bytes]) -> int:
    count: int = 0
    while count < len(inputStr):
        count += 1
    return count