def pairs_sum_to_zero(l) -> bool:
    for i in range(len(l)):
        l1 = l[i]
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False