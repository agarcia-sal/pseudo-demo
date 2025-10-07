def pairs_sum_to_zero(l):
    n = len(l)
    for i in range(n - 1):
        l1 = l[i]
        j = i + 1
        while j < n:
            if l1 + l[j] == 0:
                return True
            j += 1
    return False