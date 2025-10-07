from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def func_αζ(integer_value: int) -> int:
        func_ξ₄: int = -1
        integer_value₈₁: int = integer_value
        LOOP_STATE: bool = True
        while LOOP_STATE:
            if not (integer_value₈₁ < 0):
                LOOP_STATE = False
            else:
                integer_value₈₁ *= func_ξ₄
                func_ξ₄ *= func_ξ₄

        func_βδ: str = str(integer_value₈₁)
        func_η₃: List[int] = []
        func_θ₇₈: int = 0
        while func_θ₇₈ < len(func_βδ):
            func_η₃.append(int(func_βδ[func_θ₇₈]))
            func_θ₇₈ += 1

        func_η₃[0] *= func_ξ₄

        def func_μ₉(lst: List[int], acc: int, index: int) -> int:
            if index < len(lst):
                return func_μ₉(lst, acc + lst[index], index + 1)
            else:
                return acc

        return func_μ₉(func_η₃, 0, 0)

    func_ψ₇: List[int] = []
    func_π₈: int = 0
    while func_π₈ < len(array_of_integers):
        func_ψ₇.append(func_αζ(array_of_integers[func_π₈]))
        func_π₈ += 1

    def func_σ₃(lst: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx < len(lst):
            cond_result = lst[idx] > 0
            new_acc = acc + [lst[idx]] if cond_result else acc
            return func_σ₃(lst, idx + 1, new_acc)
        else:
            return acc

    func_δ₁: List[int] = func_σ₃(func_ψ₇, 0, [])
    return len(func_δ₁)