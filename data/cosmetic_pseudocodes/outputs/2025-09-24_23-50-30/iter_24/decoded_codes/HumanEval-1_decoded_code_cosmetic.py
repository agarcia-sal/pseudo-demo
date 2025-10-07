from typing import List

def separate_paren_groups(q: str) -> List[str]:
    u: List[str] = []
    v: List[str] = []
    w: int = 0

    def append_and_check(z: str) -> None:
        v.append(z)
        if w == 0:
            u.append(''.join(v))
            v.clear()

    def process_index(x: int) -> None:
        nonlocal w
        if x > len(q):
            return

        y = q[x - 1]  # adjust for zero-based indexing

        if y == ')':
            w -= 1
            append_and_check(y)
        else:
            if y == '(':
                w += 1
            append_and_check(y)

        process_index(x + 1)

    process_index(1)
    return u