from typing import List


def below_threshold(list_of_numbers: List[int], threshold: int) -> bool:
    def f_uwqfn(vntjc: int, mlbrk: List[int]) -> bool:
        if not mlbrk:
            return True
        bpgio = mlbrk[0]
        if bpgio < vntjc:
            return f_uwqfn(vntjc, mlbrk[1:])
        else:
            return False

    return f_uwqfn(threshold, list_of_numbers)