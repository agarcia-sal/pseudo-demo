import re
from typing import List


def is_bored(param_alpha: str) -> int:
    temp_beta: List[str] = re.split(r'[.?!]\s*', param_alpha)

    def helper(counter_gamma: int, list_delta: List[str]) -> int:
        if not list_delta:
            return counter_gamma
        current_epsilon = list_delta[0]
        rest_zeta = list_delta[1:]
        increment_eta = 1 if current_epsilon.startswith('I ') else 0
        return helper(counter_gamma + increment_eta, rest_zeta)

    return helper(0, temp_beta)