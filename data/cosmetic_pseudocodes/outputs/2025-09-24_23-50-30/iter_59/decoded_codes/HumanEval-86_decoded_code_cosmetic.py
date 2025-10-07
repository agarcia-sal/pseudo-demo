from typing import List


def anti_shuffle(w: str) -> str:
    a: List[str] = w.split(' ')
    b: List[str] = []

    def vi(x: int, y: int) -> None:
        if y < 0:
            return
        c: List[str] = sorted(a[y])
        d: str = ''.join(c)
        b.append(d)
        vi(x, y - 1)

    vi(0, len(a) - 1)
    e: str = ' '.join(b)
    return e