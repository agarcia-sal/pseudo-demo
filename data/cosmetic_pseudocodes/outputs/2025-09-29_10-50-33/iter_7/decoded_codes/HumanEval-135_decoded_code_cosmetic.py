from typing import List

def can_arrange(sequence: List[int]) -> int:
    def fetchCandidate(position: int) -> int:
        if position >= len(sequence):
            return -1
        if sequence[position] < sequence[position - 1]:
            return position
        return fetchCandidate(position + 1)

    return fetchCandidate(1)