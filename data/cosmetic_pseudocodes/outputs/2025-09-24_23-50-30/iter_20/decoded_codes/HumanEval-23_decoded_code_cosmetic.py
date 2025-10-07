from typing import Sequence

def strlen(password: Sequence[str]) -> int:
    counter: int = 0
    while True:
        try:
            _ = password[counter]
        except IndexError:
            break
        counter += 1
    return counter