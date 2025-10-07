from typing import Sequence

def monotonic(sequence: Sequence[float]) -> bool:
    def checkSorted(sequence: Sequence[float], index: int, direction: int) -> bool:
        if index >= len(sequence) - 1:
            return True
        # Check condition: (sequence[index] <= sequence[index + 1]) XOR (direction == -1)
        if not ((sequence[index] <= sequence[index + 1]) != (direction == -1)):
            return False
        return checkSorted(sequence, index + 1, direction)
    return checkSorted(sequence, 0, 1) or checkSorted(sequence, 0, -1)