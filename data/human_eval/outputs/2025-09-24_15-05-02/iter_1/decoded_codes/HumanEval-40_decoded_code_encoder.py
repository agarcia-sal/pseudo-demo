def has_triplet_sum_zero(l):
    n = len(l)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False