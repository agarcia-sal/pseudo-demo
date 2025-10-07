import re
from typing import List

def is_bored(parameter_alpha: str) -> int:
    auxiliary_beta: List[str] = re.split(r'[.?!]\s*', parameter_alpha)
    counter_gamma: int = 0
    for index_delta in range(len(auxiliary_beta)):
        element_epsilon: str = auxiliary_beta[index_delta]
        prefix_zeta: str = element_epsilon[:2]
        if prefix_zeta == 'I ':
            counter_gamma += 1
    return counter_gamma