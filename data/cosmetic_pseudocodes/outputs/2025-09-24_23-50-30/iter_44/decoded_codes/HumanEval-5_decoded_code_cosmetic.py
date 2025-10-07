from typing import List, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def intersperse(param_alpha: List[T], param_beta: U) -> List[T | U]:
    def helper(index: int, acc: List[T | U]) -> List[T | U]:
        if index >= len(param_alpha):
            return acc
        elif index == len(param_alpha) - 1:
            return acc + [param_alpha[index]]
        else:
            return helper(index + 1, acc + [param_alpha[index], param_beta])
    if len(param_alpha) == 0:
        return []
    else:
        return helper(0, [])