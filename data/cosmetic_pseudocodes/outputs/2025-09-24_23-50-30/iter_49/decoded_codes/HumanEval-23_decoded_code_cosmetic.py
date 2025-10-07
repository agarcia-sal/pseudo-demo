from typing import Callable

def strlen(gamma: str) -> int:
    def compute_length(delta: int, epsilon: str) -> int:
        if epsilon == "":
            return delta
        else:
            return compute_length(delta + 1, epsilon[1:])
    return compute_length(0, gamma)