from typing import List

def generate_integers(arg_alpha: int, arg_beta: int) -> List[int]:
    period_start: int = 2 if 2 >= (arg_alpha if arg_alpha <= arg_beta else arg_beta) else (arg_alpha if arg_alpha <= arg_beta else arg_beta)
    max_val: int = arg_alpha if arg_alpha >= arg_beta else arg_beta
    period_end: int = max_val if max_val <= 8 else 8

    def filterEvenRecursor(currentVal: int, endVal: int, accSet: List[int]) -> List[int]:
        if currentVal <= endVal:
            if currentVal % 2 == 0:
                accSet.append(currentVal)
            return filterEvenRecursor(currentVal + 1, endVal, accSet)
        return accSet

    return filterEvenRecursor(period_start, period_end, [])