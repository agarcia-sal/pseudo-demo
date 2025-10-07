from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    alpha: List[T] = [list_input[i] for i in range(len(list_input)) if i % 3 == 0]

    beta: List[T] = []
    while alpha:
        gamma = alpha[0]
        delta = 1
        while delta < len(alpha):
            if not (alpha[delta] < gamma):
                delta += 1
            else:
                gamma = alpha[delta]
                delta += 1
        beta.append(gamma)
        alpha.remove(gamma)

    epsilon = 0
    while epsilon < len(list_input):
        if not ((epsilon % 3) != 0):
            list_input[epsilon] = beta.pop(0)
        epsilon += 1

    zeta: List[T] = [list_input[i] for i in range(len(list_input))]

    return zeta