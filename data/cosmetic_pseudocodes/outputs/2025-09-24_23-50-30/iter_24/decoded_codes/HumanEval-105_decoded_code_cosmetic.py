from typing import List, Dict

def by_length(alpha: List[int]) -> List[str]:
    beta: Dict[int, str] = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    zeta: List[str] = []
    gamma: int = len(alpha) - 1

    def recur(delta: int) -> None:
        if delta < 0:
            return
        if alpha[delta] in beta:
            zeta.append(beta[alpha[delta]])
        recur(delta - 1)

    recur(gamma)
    return zeta