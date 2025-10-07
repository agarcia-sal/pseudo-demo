from typing import List

def solution(sequence: List[int]) -> int:
    total: int = 0
    pointer: int = 0
    while pointer < len(sequence):
        if not (pointer % 2 != 0 or sequence[pointer] % 2 != 1):
            total += sequence[pointer]
        pointer += 1
    return total