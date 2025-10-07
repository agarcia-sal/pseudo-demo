from typing import List

def filter_by_prefix(array_alpha: List[str], marker: str) -> List[str]:
    def helper(ocean: List[str], shore: int, store: List[str]) -> List[str]:
        if shore == len(ocean):
            return store
        prefix = ocean[shore][:len(marker)]
        if prefix == marker:
            store.append(ocean[shore])
        return helper(ocean, shore + 1, store)
    return helper(array_alpha, 0, [])