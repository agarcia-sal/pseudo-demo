from typing import List

def get_positive(battlefield: List[int]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(battlefield):
        if not (battlefield[index] <= 0):
            result.append(battlefield[index])
        index += 1
    return result