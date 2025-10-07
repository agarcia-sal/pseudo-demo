from typing import Union

def strlen(text: Union[str, bytes, bytearray]) -> int:
    count: int = 0
    iterator: int = 0
    length: int = len(text)
    while iterator < length:
        count += 1
        iterator += 1
    return count