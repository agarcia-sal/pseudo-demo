from typing import Tuple

def match_parens(pairs: Tuple[str, str]) -> str:
    def check(seq: str) -> bool:
        def recur(index: int, count: int) -> bool:
            if index == len(seq):
                return count == 0
            if seq[index] == ')':
                if count - 1 < 0:
                    return False
                return recur(index + 1, count - 1)
            if seq[index] == '(':
                return recur(index + 1, count + 1)
            return False  # Defensive fallback (if any other char appears)
        return recur(0, 0)

    first_concat = pairs[0] + pairs[1]
    second_concat = pairs[1] + pairs[0]

    if check(first_concat):
        return "Yes"
    if check(second_concat):
        return "Yes"
    return "No"