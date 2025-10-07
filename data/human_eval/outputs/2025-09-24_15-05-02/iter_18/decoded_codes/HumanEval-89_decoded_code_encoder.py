from typing import AnyStr


def encrypt(s: AnyStr) -> str:
    d: str = 'abcdefghijklmnopqrstuvwxyz'
    out: list[str] = []
    for c in s:
        if c in d:
            out.append(d[(d.index(c) + 4) % 26])
        else:
            out.append(c)
    return ''.join(out)