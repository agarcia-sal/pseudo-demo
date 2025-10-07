from typing import Sequence

def strlen(input_sequence: Sequence) -> int:
    result_count: int = 0
    while True:
        if result_count >= len(input_sequence):
            return result_count
        else:
            result_count += 1