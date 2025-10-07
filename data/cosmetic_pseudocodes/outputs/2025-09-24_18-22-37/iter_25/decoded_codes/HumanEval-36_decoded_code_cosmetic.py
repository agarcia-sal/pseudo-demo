from typing import List


def fizz_buzz(param_x: int) -> int:
    var_alpha: List[int] = []
    var_beta = 0  # unused per pseudocode
    var_gamma = ""
    var_delta = 0  # unused per pseudocode

    var_omega = 0
    while var_omega < param_x:
        var_sigma = var_omega % 11
        var_tau = var_omega % 13
        if var_sigma == 0 or var_tau == 0:
            var_alpha.append(var_omega)
        var_omega += 1

    for var_phi in var_alpha:
        var_gamma += str(var_phi)

    var_nu = 0
    var_chi = 0
    while var_chi < len(var_gamma):
        var_psi = var_gamma[var_chi]
        if not (var_psi != '7'):
            var_nu += 1
        var_chi += 1

    return var_nu