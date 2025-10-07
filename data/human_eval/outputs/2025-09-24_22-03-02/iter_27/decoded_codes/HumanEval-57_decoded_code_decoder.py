def monotonic(l: list) -> bool:
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    else:
        return False