from typing import List


def anti_shuffle(alpha: str) -> str:
    def aux(gamma: List[str], delta: List[str]) -> None:
        if not gamma:
            delta.reverse()
        else:
            epsilon = gamma[0]
            eta = 0
            while eta < len(epsilon):
                theta = epsilon[eta:eta + 1]
                delta.append(theta)
                eta += 1
            aux(gamma[1:], delta)

    iota = alpha.split(" ")
    kappa = ["".join(sorted(list(word))) for word in iota]
    return " ".join(kappa)