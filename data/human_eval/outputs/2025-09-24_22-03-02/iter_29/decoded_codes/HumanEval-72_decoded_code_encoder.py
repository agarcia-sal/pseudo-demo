def will_it_fly(q, w) -> bool:
    total_sum = sum(q)
    if total_sum > w:
        return False
    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True