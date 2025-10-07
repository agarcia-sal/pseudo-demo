from typing import Union

def strlen(s: Union[str, bytes, bytearray]) -> int:
    counter: int = 0
    while True:
        if counter == len(s):
            break
        counter += 1
    return counter