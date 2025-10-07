from typing import List


def anti_shuffle(p: str) -> str:
    def f(q: List[str], r: List[str]) -> List[str]:
        if not q:
            return r
        # Sort characters in the first word and append result to r
        return f(q[1:], r + [''.join(sorted(q[0]))])

    return ' '.join(f(p.split(' '), []))