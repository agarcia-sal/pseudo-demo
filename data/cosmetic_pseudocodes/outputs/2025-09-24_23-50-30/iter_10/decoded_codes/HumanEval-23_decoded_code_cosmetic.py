from typing import Sequence

def strlen(corpus: Sequence) -> int:
    length_counter: int = 0
    while True:
        if length_counter >= len(corpus):
            break
        length_counter += 1
    return length_counter