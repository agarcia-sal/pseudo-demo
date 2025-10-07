from typing import List

def solution(sequence: List[int]) -> int:
    aggregate: int = 0
    position: int = 0
    length: int = len(sequence)
    while position < length:
        if not ((position % 2 == 0) and (sequence[position] % 2 == 1)):
            position += 1
        else:
            aggregate += sequence[position]
            position += 1
    return aggregate