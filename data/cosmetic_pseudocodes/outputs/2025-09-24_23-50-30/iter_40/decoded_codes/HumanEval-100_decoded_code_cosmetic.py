from typing import List

def make_a_pile(counter: int) -> List[int]:
    result_collection: List[int] = []
    iterator: int = 0
    while iterator < counter:
        result_collection.append(counter + (iterator << 1))
        iterator += 1
    return result_collection