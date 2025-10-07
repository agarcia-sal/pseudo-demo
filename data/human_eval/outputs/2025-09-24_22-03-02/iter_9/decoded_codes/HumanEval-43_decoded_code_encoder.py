def pairs_sum_to_zero(l):
    for i in range(len(l) - 1):
        l1 = l[i]
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False