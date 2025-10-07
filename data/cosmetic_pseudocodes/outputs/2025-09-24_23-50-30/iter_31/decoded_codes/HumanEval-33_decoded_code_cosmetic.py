from typing import List

def sort_third(beta: List[int]) -> List[int]:
    kappa: List[int] = beta[:]
    omega: List[int] = [kappa[lam] for lam in range(len(kappa)) if lam % 3 == 0]
    zeta: List[int] = qsort_asc(omega, 0)
    alpha: int = 0
    while alpha < len(kappa):
        if alpha % 3 == 0:
            kappa[alpha] = zeta[alpha // 3]
        alpha += 1
    return kappa

def qsort_asc(arr: List[int], start: int) -> List[int]:
    if len(arr) < 2:
        return arr
    pivot: int = arr[0]
    rest: List[int] = arr[1:]
    less_or_equal: List[int] = [x for x in rest if x <= pivot]
    greater: List[int] = [x for x in rest if x > pivot]
    return qsort_asc(less_or_equal, 0) + [pivot] + qsort_asc(greater, 0)