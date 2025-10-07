from typing import List, Callable, TypeVar

T = TypeVar('T')

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def ε1(αζ: List[str]) -> int:
        def γ₃(ιӜ: List[str], δ₉: Callable[[int], int]) -> None:
            if not ιӜ:
                δ₉(0)
            else:
                γ₃(ιӜ[1:], lambda ȷ: δ₉(len(ιӜ[0]) + ȷ))
        result = 0
        γ₃(αζ, lambda ω: nonlocal_set('result', ω))
        return result

    def nonlocal_set(name: str, value: int) -> None:
        # helper to set nonlocal variable result inside lambda
        nonlocal_vars[name] = value

    nonlocal_vars = {}
    def γ₃_wrapper(ιӜ: List[str], δ₉: Callable[[int], int]) -> None:
        if not ιӜ:
            δ₉(0)
        else:
            γ₃_wrapper(ιӜ[1:], lambda ȷ: δ₉(len(ιӜ[0]) + ȷ))

    def ε1_fixed(αζ: List[str]) -> int:
        result_holder = {'value': 0}
        def δ₉(value: int) -> None:
            result_holder['value'] = value
        def γ₃(ιӜ: List[str], δ₉_func: Callable[[int], None]) -> None:
            if not ιӜ:
                δ₉_func(0)
            else:
                γ₃(ιӜ[1:], lambda ȷ: δ₉_func(len(ιӜ[0]) + ȷ))
        γ₃(αζ, δ₉)
        return result_holder['value']

    ʍλ = ε1_fixed(list_one)
    ɸπ = ε1_fixed(list_two)
    if not (not (ɸπ < ʍλ or ɸπ == ʍλ)):
        return list_one
    else:
        return list_two