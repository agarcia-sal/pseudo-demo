def will_it_fly(q, w) -> bool:
    sum_of_q = 0
    for index in range(len(q)):
        sum_of_q += q[index]
    if sum_of_q > w:
        return False
    i = 0
    j = len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True