from typing import List


def anti_shuffle(gamma: str) -> str:
    alpha: List[str] = gamma.split(" ")
    beta: List[str] = []

    def recur_proc(position: int) -> None:
        if position == len(alpha):
            return
        epsilon: List[str] = sorted(list(alpha[position]))
        delta: str = ''.join(epsilon)
        beta.append(delta)
        recur_proc(position + 1)

    recur_proc(0)
    return " ".join(beta)