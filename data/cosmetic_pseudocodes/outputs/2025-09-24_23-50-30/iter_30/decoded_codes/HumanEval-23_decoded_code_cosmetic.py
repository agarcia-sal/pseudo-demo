from typing import Sequence

def strlen(sequence: Sequence) -> int:
    # The switch is effectively just returning length if non-negative, which length always is
    return len(sequence)