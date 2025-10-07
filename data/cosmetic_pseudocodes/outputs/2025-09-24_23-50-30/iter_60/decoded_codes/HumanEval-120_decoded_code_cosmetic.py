from typing import List

def maximum(beta: List[int], theta: int) -> List[int]:
    def aux(psi: List[int], omega: int, eta: int) -> List[int]:
        if omega == 0:
            return []
        delta = len(psi) - omega
        return psi[delta:len(psi)]

    def insertion_sort(epsilon: List[int], zeta: int) -> None:
        def insert_item(iota: List[int], kappa: int) -> None:
            if kappa <= 0 or iota[kappa - 1] <= iota[kappa]:
                return
            iota[kappa - 1], iota[kappa] = iota[kappa], iota[kappa - 1]
            insert_item(iota, kappa - 1)

        def sort_index(nu: int) -> None:
            if nu >= len(epsilon):
                return
            insert_item(epsilon, nu)
            sort_index(nu + 1)

        sort_index(1)

    insertion_sort(beta, 0)
    return aux(beta, len(beta), theta)