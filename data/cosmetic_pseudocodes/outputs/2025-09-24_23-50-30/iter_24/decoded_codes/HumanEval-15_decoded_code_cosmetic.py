from typing import Callable


def string_sequence(integer_n: int) -> str:
    def helper(delta: int, acc: str) -> str:
        if delta > integer_n:
            return acc
        new_acc = str(delta) if acc == "" else acc + " " + str(delta)
        return helper(delta + 1, new_acc)
    return helper(0, "")