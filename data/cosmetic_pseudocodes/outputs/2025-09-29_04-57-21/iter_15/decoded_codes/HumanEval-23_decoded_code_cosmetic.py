from typing import Union

def strlen(inputText: Union[str, bytes]) -> int:
    count: int = 0
    while count < len(inputText):
        count += 1
    return count