def monotonic(l: list) -> bool:
    if l == sorted(l):
        return True
    else:
        reversed_sorted = sorted(l, reverse=True)
        if l == reversed_sorted:
            return True
        else:
            return False