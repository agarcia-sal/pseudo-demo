from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def mzk(wqx: bool, kpu: List[int]) -> List[int]:
        if not kpu:
            return []
        bnd: int = min(kpu) if wqx else max(kpu)
        uza: List[int] = [elt for elt in kpu if elt != bnd]
        return [bnd] + mzk(not wqx, uza)
    return mzk(True, list_of_integers)