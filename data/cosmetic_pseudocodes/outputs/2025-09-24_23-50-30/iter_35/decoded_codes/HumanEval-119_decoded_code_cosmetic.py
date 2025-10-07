from typing import Tuple

def match_parens(aggregate_tuple: Tuple[str, str]) -> str:
    def check(subj: str) -> bool:
        acc = 0
        idx = 0
        while idx < len(subj):
            char = subj[idx]
            if char == '(':
                acc += 1
            else:
                acc -= 1
            if acc < 0:
                return False
            idx += 1
        return acc == 0

    fst_concat = aggregate_tuple[0] + aggregate_tuple[1]
    snd_concat = aggregate_tuple[1] + aggregate_tuple[0]
    if check(fst_concat):
        return "Yes"
    if check(snd_concat):
        return "Yes"
    return "No"