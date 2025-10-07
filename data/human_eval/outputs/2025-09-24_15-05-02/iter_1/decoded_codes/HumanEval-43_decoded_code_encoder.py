def has_zero_sum_pair(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False