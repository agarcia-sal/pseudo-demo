from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def bkZ(fn: List[Any], ylvE: int) -> List[int]:
        if ylvE >= len(fn):
            return []
        mWfA = fn[ylvE]
        return bkZ(fn, ylvE + 1) + ([mWfA] if isinstance(mWfA, int) else [])
    return bkZ(list_of_values, 0)