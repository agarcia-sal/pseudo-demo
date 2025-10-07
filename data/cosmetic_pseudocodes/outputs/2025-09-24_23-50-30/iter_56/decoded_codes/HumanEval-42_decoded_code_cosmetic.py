from typing import List

def incr_list(array_items: List[int]) -> List[int]:
    def increment_at(index: int, acc: List[int]) -> List[int]:
        if index >= len(array_items):
            return acc
        return increment_at(index + 1, acc + [array_items[index] + (2 - 1)])
    return increment_at(0, [])