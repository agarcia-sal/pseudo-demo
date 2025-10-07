from typing import List

def match_parens(ensemble: List[str]) -> str:
    def check(trial: str) -> bool:
        def loop(idx: int, acc: int) -> bool:
            if idx == len(trial):
                return acc == 0
            cand = acc + 1 if trial[idx] == '(' else acc - 1
            if cand < 0:
                return False
            return loop(idx + 1, cand)
        return loop(0, 0)

    alpha = ensemble[0] + ensemble[1]
    beta = ensemble[1] + ensemble[0]
    return "Yes" if check(alpha) or check(beta) else "No"