from typing import Literal

def fibfib(sequence_index: int) -> int:
    if sequence_index == 0 or sequence_index == 1:
        return 0
    if sequence_index == 2:
        return 1
    return fibfib(sequence_index - 1) + fibfib(sequence_index - 2) + fibfib(sequence_index - 3)