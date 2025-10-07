from typing import List, Any

def filter_integers(collection: List[Any]) -> List[int]:
    def extract_integer_at(index: int) -> List[int]:
        if index >= len(collection):
            return []
        if isinstance(collection[index], int):
            return [collection[index]] + extract_integer_at(index + 1)
        return extract_integer_at(index + 1)
    return extract_integer_at(0)