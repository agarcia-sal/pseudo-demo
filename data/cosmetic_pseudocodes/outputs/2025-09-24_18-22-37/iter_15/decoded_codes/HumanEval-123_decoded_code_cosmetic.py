from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    epsilon: int = alpha % 2
    if epsilon == 0:
        beta: List[int] = []
    else:
        beta = [alpha]

    delta: int = alpha

    while delta > 1:
        gamma: int = delta % 2

        if gamma == 0:
            kappa: int = delta // 2
            delta = kappa
        else:
            lambd: int = delta * 3  # 'lambda' is a keyword, renamed to 'lambd'
            mu: int = lambd + 1
            delta = mu

        nu: int = delta % 2
        if nu == 1:
            beta.append(delta)

    result: List[int] = beta

    i: int = 0
    while i < len(result) - 1:
        j: int = i + 1
        while j < len(result):
            if result[i] > result[j]:
                temp: int = result[i]
                result[i] = result[j]
                result[j] = temp
            j += 1
        i += 1

    return result