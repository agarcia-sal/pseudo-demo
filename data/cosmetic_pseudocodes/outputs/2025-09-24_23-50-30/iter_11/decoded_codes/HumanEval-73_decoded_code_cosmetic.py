from typing import List

def smallest_change(numbers: List[int]) -> int:
    count: int = 0
    half: int = (len(numbers) - 1) // 2
    pos: int = 0
    while pos <= half:
        if numbers[pos] != numbers[len(numbers) - (pos + 1)]:
            count += 1
        pos += 1
    return count