from typing import Union

def strlen(text: Union[str, bytes]) -> int:
    counter: int = 0
    for _ in text:
        counter += 1
    return counter