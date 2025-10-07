from typing import Sequence

def strlen(data: Sequence) -> int:
    count: int = 0
    while True:
        if count == len(data):
            return count
        count += 1