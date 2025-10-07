from typing import List, Sequence, Union


def filter_integers(container: Sequence[object]) -> List[int]:
    def helper(source: Sequence[object], acc: List[int], idx: int) -> List[int]:
        if idx >= len(source):
            return acc
        current_item = source[idx]
        acc = acc + [current_item] if isinstance(current_item, int) else acc
        return helper(source, acc, idx + 1)
    return helper(container, [], 0)