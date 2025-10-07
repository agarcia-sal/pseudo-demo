from typing import Sequence

def below_zero(indexed_values: Sequence[int]) -> bool:
    progress = 0
    while True:  # Equivalent of IterateOps label + GOTO
        if len(indexed_values) == 0:
            return False
        else:
            head = indexed_values[0]
            tail = indexed_values[1:]
            progress += head
            if progress < 0:
                return True
            else:
                indexed_values = tail