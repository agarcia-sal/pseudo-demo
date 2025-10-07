from typing import List

def make_a_pile(counter: int) -> List[int]:
    collection: List[int] = []
    iterator: int = 0
    limit: int = counter - 1
    while iterator <= limit:
        value: int = counter
        product: int = 2 * iterator
        element: int = value + product
        collection.append(element)
        iterator += 1
    return collection