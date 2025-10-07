from typing import Callable, Optional, Sequence

def is_happy(param_lambda: Sequence[int]) -> bool:
    def func_theta(func_phi: Sequence[int]) -> Optional[bool]:
        func_sigma = len(func_phi)
        return False if func_sigma < 3 else None

    func_alpha: bool
    func_beta = len(param_lambda)
    func_gamma = 0
    func_delta = False
    while func_gamma <= func_beta - 3 and not func_delta:
        func_epsilon = param_lambda[func_gamma]
        func_zeta = param_lambda[func_gamma + 1]
        func_eta = param_lambda[func_gamma + 2]
        func_delta = (func_epsilon == func_zeta) or (func_zeta == func_eta) or (func_epsilon == func_eta)
        func_gamma += 1
    func_alpha = func_delta

    theta_result = func_theta(param_lambda)
    if theta_result is False:
        return False
    elif theta_result is None:
        return False if func_alpha else True
    else:
        # Should never happen, but for completeness:
        return False