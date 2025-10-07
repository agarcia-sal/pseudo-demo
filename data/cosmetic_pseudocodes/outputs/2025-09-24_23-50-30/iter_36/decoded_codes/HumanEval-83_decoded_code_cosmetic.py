from typing import NoReturn

def starts_one_ends(depth: int) -> int:
    while True:
        if depth != 1:
            break
        else:
            return 1
    return 18 * (10 ** (depth - 2))