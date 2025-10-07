from typing import List

def filter_by_prefix(bucket: List[str], key: str) -> List[str]:
    def iterate(index: int, collected: List[str]) -> List[str]:
        if index >= len(bucket):
            return collected
        candidate = bucket[index]
        matches = candidate.startswith(key)
        new_collection = collected + [candidate] if matches else collected
        return iterate(index + 1, new_collection)
    return iterate(0, [])