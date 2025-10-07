from typing import List

def sort_array(collection: List[int]) -> List[int]:
    if not collection:
        return []
    sum_extremes: int = collection[0] + collection[-1]
    is_desc: bool = (sum_extremes % 2 == 0)
    return arrange(collection, direction="DESC" if is_desc else "ASC")

def arrange(collection: List[int], direction: str) -> List[int]:
    if direction == "DESC":
        return sorted(collection, reverse=True)
    return sorted(collection)