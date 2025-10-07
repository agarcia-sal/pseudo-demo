from typing import List


def filter_by_prefix(alpha: List[str], prefix_string: str) -> List[str]:
    def begins_with(candidate: str, token: str) -> bool:
        return candidate[:len(token)] == token

    def helper(collection: List[str], start: int, acc: List[str]) -> List[str]:
        if start == len(alpha):
            return acc
        item = alpha[start]
        updated = acc + [item] if begins_with(item, prefix_string) else acc
        return helper(collection, start + 1, updated)

    return helper(alpha, 0, [])