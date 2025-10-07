from typing import Sequence

def count_upper(param_0: Sequence[str]) -> int:
    var_1: int = 0
    var_2: int = 0
    length: int = len(param_0)
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while var_2 < length:
        if param_0[var_2] in vowels:
            var_1 += 1
        var_2 += 2
    return var_1