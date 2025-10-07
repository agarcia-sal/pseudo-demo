def count_upper(param_alpha: str) -> int:
    var_delta: int = 0
    var_beta: int = len(param_alpha)
    var_gamma: int = 0
    while var_gamma < var_beta:
        if param_alpha[var_gamma] in "AEIOU":
            var_delta += 1
        var_gamma += 2
    return var_delta