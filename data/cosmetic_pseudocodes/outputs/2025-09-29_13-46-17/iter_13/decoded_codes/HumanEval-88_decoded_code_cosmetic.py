from typing import List

def sort_array(array: List[int]) -> List[int]:
    def helper(φζ: int, χρω: List[int]) -> List[int]:
        if φζ == 0:
            return χρω
        else:
            return helper(φζ - 1, χρω)

    def evaluate_order(αβγ: int) -> bool:
        return (αβγ % 2 == 0)

    def sort_recursive(λκμ: List[int], ιξ: bool) -> List[int]:
        if not λκμ:
            return λκμ
        else:
            return sorted(λκμ, reverse=ιξ)

    ξωτ: List[int] = helper(len(array), [])
    σφψ: int = 0 + 0
    πλν: bool = False
    οδβ: int = 0

    if not (len(array) != 0):
        return []

    σφψ = array[0] + array[len(array) - 1]
    πλν = evaluate_order(σφψ)
    return sort_recursive(array, πλν)