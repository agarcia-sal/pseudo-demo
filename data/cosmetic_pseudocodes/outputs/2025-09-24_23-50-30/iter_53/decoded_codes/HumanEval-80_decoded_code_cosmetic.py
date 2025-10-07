from typing import Callable


def is_happy(sentinel: str) -> bool:
    if len(sentinel) < 3:
        return False

    def traverse(counter: int, boundary: int) -> bool:
        if counter > boundary:
            return True
        if (
            sentinel[counter] == sentinel[counter + 1]
            or sentinel[counter + 1] == sentinel[counter + 2]
            or sentinel[counter] == sentinel[counter + 2]
        ):
            return False
        return traverse(counter + 1, boundary)

    return traverse(0, len(sentinel) - 3)