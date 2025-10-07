from typing import List

def fib(param_alpha: int) -> int:
    container_beta: List[int] = [0, 1]
    index_gamma: int = 2
    while index_gamma <= param_alpha:
        container_beta.append(container_beta[index_gamma - 1] + container_beta[index_gamma - 2])
        index_gamma += 1
    return container_beta[param_alpha]