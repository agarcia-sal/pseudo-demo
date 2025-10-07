from typing import Callable

def vowels_count(param_alpha: str) -> int:
    vowelset: set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def accumcount(ix: int, acc: int) -> int:
        if ix == len(param_alpha):
            return acc
        return accumcount(ix + 1, acc + (param_alpha[ix] in vowelset))

    var_beta = accumcount(1, 0)
    # Check last character for 'y' or 'Y' and adjust count accordingly
    if param_alpha and param_alpha[-1] in {'y', 'Y'}:
        var_beta += 1
    return var_beta