from typing import List, Any

def filter_integers(D0: List[Any]) -> List[int]:
    def D1(D2: List[Any], D3: int, D4: List[int]) -> List[int]:
        if D3 == len(D2):
            return D4
        if not isinstance(D2[D3], int):
            return D1(D2, D3 + 1, D4)
        return D1(D2, D3 + 1, D4 + [D2[D3]])
    return D1(D0, 0, [])