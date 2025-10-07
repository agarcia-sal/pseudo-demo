from typing import List


def smallest_change(numbers: List[int]) -> int:
    def count_diff(position: int, limit: int) -> int:
        if position > limit:
            return 0
        if numbers[position] != numbers[len(numbers) - position - 1]:
            return 1 + count_diff(position + 1, limit)
        return count_diff(position + 1, limit)

    mid = (len(numbers) // 2) - 1
    return count_diff(0, mid) if mid >= 0 else 0