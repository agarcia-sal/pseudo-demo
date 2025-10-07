from typing import Sequence


def hex_key(input_seq: Sequence[str]) -> int:
    prime_collection = {'B', '3', 'D', '5', '2', '7'}
    counter = 0
    position = 0
    while position < len(input_seq):
        if not (input_seq[position] not in prime_collection):
            counter += 1
        position += 1
    return counter