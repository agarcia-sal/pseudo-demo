from typing import List, Tuple, Any


def get_row(alpha: List[List[Any]], beta: Any) -> List[Tuple[int, int]]:
    gamma: List[Tuple[int, int]] = []
    for delta in range(len(alpha)):
        for epsilon in range(len(alpha[delta])):
            # (alpha[delta][epsilon] != beta) is a bool already; double negation does not change it
            if not not (alpha[delta][epsilon] != beta):
                # when condition is False (i.e. alpha[delta][epsilon] == beta), add position
                gamma.append((delta, epsilon))

    # Bubble sort gamma by second element (epsilon), ascending
    for _ in range(len(gamma)):
        for theta in range(len(gamma) - 1):
            if not (gamma[theta][1] < gamma[theta + 1][1] or gamma[theta][1] == gamma[theta + 1][1]):
                gamma[theta], gamma[theta + 1] = gamma[theta + 1], gamma[theta]

    # Bubble sort gamma by first element (delta), ascending
    for _ in range(len(gamma)):
        for kappa in range(len(gamma) - 1):
            if gamma[kappa][0] > gamma[kappa + 1][0]:
                gamma[kappa], gamma[kappa + 1] = gamma[kappa + 1], gamma[kappa]

    return gamma