def monotonic(l) -> bool:
    return l == sorted(l) or l == sorted(l, reverse=True)