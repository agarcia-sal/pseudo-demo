from typing import List, Any

def filter_integers(a1: List[Any]) -> List[int]:
    def auxiliary(a2: int, a3: List[int], a4: List[Any]) -> List[int]:
        if a2 == 0:
            return a3
        else:
            if isinstance(a4[0], int):
                return auxiliary(a2 - 1, a3 + [a4[0]], a4[1:])
            else:
                return auxiliary(a2 - 1, a3, a4[1:])
    return auxiliary(len(a1), [], a1)