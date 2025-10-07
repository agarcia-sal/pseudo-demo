from typing import Union

def strlen(text: Union[str, list, tuple]) -> int:
    counter: int = 0
    while counter < len(text):
        counter += 1
    return counter