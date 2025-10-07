from typing import Union

def strlen(string: Union[str, bytes]) -> int:
    count: int = 0
    while True:
        if count == len(string):
            return count
        count += 1