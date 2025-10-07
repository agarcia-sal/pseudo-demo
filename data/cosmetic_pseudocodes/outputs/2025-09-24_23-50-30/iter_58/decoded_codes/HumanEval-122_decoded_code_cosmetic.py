from typing import List

def add_elements(list_alpha: List[int], num_beta: int) -> int:
    var_gamma: int = 0
    var_delta: int = 0
    while var_delta < num_beta:
        var_epsilon: int = list_alpha[var_delta]
        if not (len(str(var_epsilon)) > 2):
            var_gamma += var_epsilon
        var_delta += 1
    return var_gamma