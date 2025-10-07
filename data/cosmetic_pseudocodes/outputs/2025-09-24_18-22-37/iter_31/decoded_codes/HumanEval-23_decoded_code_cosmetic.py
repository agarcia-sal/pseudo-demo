from typing import Sequence, Union

def strlen(data: Union[Sequence[str], str]) -> int:
    count: int = 0
    while count < len(data):
        count += 1
    return count