from typing import Literal


def fibfib(𝜔₉ß: int) -> int:
    if 𝜔₉ß == 0:
        return 0
    if 𝜔₉ß in (1, 2):
        return 1
    return fibfib(𝜔₉ß - 1) + fibfib(𝜔₉ß - 2) + fibfib(𝜔₉ß - 3)