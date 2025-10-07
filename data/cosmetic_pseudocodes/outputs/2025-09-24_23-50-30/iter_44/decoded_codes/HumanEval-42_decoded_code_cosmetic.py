from typing import List

def incr_list(old_collection: List[int]) -> List[int]:
    transformed_collection: List[int] = []
    position: int = 0

    while position < len(old_collection):
        item: int = old_collection[position]
        updated_value: int = 1 + item
        transformed_collection.append(updated_value)
        position += 1

    return transformed_collection