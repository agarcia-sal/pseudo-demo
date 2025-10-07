from typing import List


def is_nested(strng: str) -> bool:
    ups: List[int] = []
    dns: List[int] = []
    p: int = 0
    len_dns: int = 0
    c: int = 0

    r: int = 0
    while r < len(strng) - 1:
        ch: str = strng[r]
        if ch == '[':
            ups.append(r)
        else:
            dns.append(r)
        r += 1

    dns.reverse()

    p = 0
    len_dns = len(dns)

    i: int = 0
    while i < len(ups):
        up_idx: int = ups[i]
        if p < len_dns and up_idx < dns[p]:
            c += 1
            p += 1
        i += 1

    return c >= 2