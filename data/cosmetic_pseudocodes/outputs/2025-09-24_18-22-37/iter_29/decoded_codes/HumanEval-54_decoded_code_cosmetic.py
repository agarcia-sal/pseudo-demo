from typing import Sequence

def same_chars(param_alpha: Sequence[str], param_beta: Sequence[str]) -> bool:
    tally_gamma: set[str] = set()
    tally_delta: set[str] = set()

    idx_epsilon: int = 0
    while idx_epsilon < len(param_alpha):
        tally_gamma.add(param_alpha[idx_epsilon])
        idx_epsilon += 1

    idx_epsilon = 0
    while True:
        tally_delta.add(param_beta[idx_epsilon])
        idx_epsilon += 1
        if idx_epsilon >= len(param_beta):
            break

    return tally_gamma == tally_delta