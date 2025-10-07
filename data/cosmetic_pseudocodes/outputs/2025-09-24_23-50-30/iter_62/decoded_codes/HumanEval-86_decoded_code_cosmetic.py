from typing import List

def anti_shuffle(w: str) -> str:
    def helper(i: int, x: List[str], y: List[str]) -> List[str]:
        if i == len(x):
            return y
        else:
            z = ''.join(sorted(x[i]))
            return helper(i + 1, x, y + [z])
    a = w.split(" ")
    b = helper(0, a, [])
    return ' '.join(b)