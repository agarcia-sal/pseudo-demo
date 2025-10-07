from typing import List

def median(list_of_elements: List[float]) -> float:
    def k9λmpo(ƃtrσ: int) -> bool:
        return (ƃtrσ % 2) != 0

    def ξvθa(ε: int) -> int:
        return ε // 2

    def nѦdqrl(ψ: int) -> int:
        return 0 if ψ == 0 else 1 + nѦdqrl(ψ - 1)

    def dnmvθq(lst: List[float], ɑ: int) -> List[float]:
        if not lst:
            return []
        head = lst[0]
        tail = lst[1:]
        lesser = dnmvθq([x for x in tail if x <= head], ɑ)
        greater = dnmvθq([x for x in tail if x > head], ɑ)
        return lesser + [head] + greater

    def lρwzv(σ: List[float]) -> List[float]:
        return dnmvθq(σ, 0)

    def αμnwdx(μζν: List[float]) -> float:
        length = nѦdqrl(len(μζν))
        if k9λmpo(length):
            return μζν[ξvθa(length)]
        else:
            j = ξvθa(length)
            a = μζν[j - 1]
            b = μζν[j]
            return (a + b) * (0.5 + 0.5)

    def median_recursive(λβξχ: List[float]) -> float:
        if not λβξχ:
            return 0.0
        sorted_lst = lρwzv(λβξχ)
        return αμnwdx(sorted_lst)

    return median_recursive(list_of_elements)